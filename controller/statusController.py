import os
import pyautogui
from time import *
import datetime
import schedule
from model.db import Session, Status, Message, ScheduledOperation
from utils.oppenZapp import *

oppened = False

def createStatus(content, media=True, text="", time=""):
    pyautogui.alert("NB : Automated Status is not available for the Whatsapp Destop App\n\tOnly Available on WhatsApp Web")

    session = Session()
    if time == "":
        time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%H:%M")

    allStatus = session.query(Status).all()
    allMessages = session.query(Message).all()

    for statu in allStatus:
        if statu.send_time == time :
            pyautogui.alert("Can't create the status with content '"+content+"'\n A Status has already been planned at that same time")
            print("Task with thesame time already exist")
            return
    for messag in allMessages:
        if messag.send_time == time :
            pyautogui.alert("Can't create the status with content '"+content+"'\n A Message has already been planned at that same time")
            print("Task with thesame time already exist")
            return
    
    # Create a new status
    new_status = Status(
        content_or_path = content,
        send_time = time,
        mediaText = text,
        media = media,
    )
    session.add(new_status)
    session.commit()

    # Schedule the status
    scheduled_status = ScheduledOperation(
        operation="status",
        status_id=new_status.id,
    )
    session.add(scheduled_status)
    session.commit()

    print("status and scheduled status added successfully!")

def postStatus(lock, content, text, media):
    global oppened
    with lock :
        print(f"[{datetime.datetime.now()}] Posting media located at '{content}'...")
        sleep(1)
        try:
            oppened = OppenClosedZapp()
            sleep(1)

            try :
                pyautogui.click(pyautogui.locateOnScreen("controller/image/status_read.png", confidence=0.8))
            except Exception as e:
                print("Exception Caught : Couldn't found the status_read image")
                try :
                    pyautogui.click(pyautogui.locateCenterOnScreen("controller/image/status_select.png", confidence=0.8))
                except Exception as e:
                    print("Exception Caught : Couldn't found the status_select image")
                    try :
                        pyautogui.click(pyautogui.locateOnScreen("controller/image/status_unread.png", confidence=0.8))
                    except Exception as e:
                        print("Exception Caught : Couldn't found the status_unread image")
                        raise
        
            sleep(1)
            pyautogui.click(pyautogui.locateCenterOnScreen("controller/image/status_add.png", confidence=0.8))
            pyautogui.press("down")
            if media == True:
                pyautogui.press("enter")
                print("Navigating to file explorer...")
                if os.path.exists(content):
                    pyautogui.hotkey('ctrl', 'l')
                    sleep(1)
                    pyautogui.write(content, interval=0.08) 
                    pyautogui.press("enter")
                    sleep(3)
                    pyautogui.write(text, interval=0.08) 
                else:
                    print("Status File path does not exist")
                    raise
                    return
            else:
                pyautogui.press("down")
                pyautogui.press("enter")
                sleep(1)
                pyautogui.write(content, interval=0.08) 
                
            print("Posting status............")
            try:
                pyautogui.click(pyautogui.locateOnScreen("controller/image/postImg_button.png", confidence=0.8))
                print("Status posted successfully!")
            except Exception as e:
                print("Exception Caught : Post button not found.")
                raise
                
        except Exception as e:
            pyautogui.alert("The Automation process could not continue\nAn Error was encountered\n !! Verify your Internet connection !!")
            print("Exception Primary :An Error was encountered when posting the status : \n ")
            print(f"Error running scheduled tasks: {e}")
            return

def scheduleStatus(lock):
    session = Session()  # Create a session
    now = datetime.datetime.utcnow()
    pending_status = session.query(Status).all()

    for status in pending_status:
        # Schedule the Status
        scheduleTableVal = session.query(ScheduledOperation).filter(ScheduledOperation.status_id == status.id).first()
        sendTime = status.send_time
        schedule.every().day.at(sendTime).do(
            postStatus,
            lock=lock,
            content=status.content_or_path,
            text=status.mediaText,
            media=status.media
        )

        scheduleTableVal.current_status = "Completed"
        session.commit()

    print("Status Scheduler is running. Waiting to post status...\n\n")

    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            print(f"Error running scheduled tasks: {e}")
            sleep(1)

def getAllStatus():
    session = Session()
    allStatus = session.query(Status).all()
    return allStatus

