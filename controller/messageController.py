import pyautogui
from time import *
import threading
import datetime
import schedule
from model.db import Session, Message, Status, ScheduledOperation
from utils.oppenZapp import *

oppene=False # serve as a flag to determine if whatsapp is already oppene or not

def createMessage(contact, msg, time=""):
    session = Session()
    if time == "":
        time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%H:%M")

    if not contact or not msg:
        pyautogui.alert("Enter atleast the Receiver name or number\nand the message you wanna send")
        return
    
    allStatus = session.query(Status).all()
    allMessages = session.query(Message).all()

    for statu in allStatus:
        if statu.send_time == time :
            alertMsg = "Can't create the message '"+msg+"' to be delivered to '"+contact+"'\n A Status has already been planned at that same time"
            # pyautogui.alert()
            print("Task with thesame time already exist")
            return alertMsg
    for messag in allMessages:
        if messag.send_time == time :
            alertMsg = "Can't create the message '"+msg+"' to be delivered to '"+contact+"'\n A Message has already been planned at that same time"
            # pyautogui.alert()
            print("Task with thesame time already exist")
            return alertMsg

    # Create a new message
    new_message = Message(
        receiver = contact,
        content = msg,
        send_time = time
    )
    session.add(new_message)
    session.commit()

    # Schedule the message
    scheduled_message = ScheduledOperation(
        message_id=new_message.id,
        current_status="In Process"
    )
    session.add(scheduled_message)
    session.commit()

    print("Message and scheduled message added successfully!")


def sendMessages(lock, contact, msg):
    global oppene
    app = False
    with lock:
        print(f"[{datetime.datetime.now()}] Sending message to {contact}...")
        try:
            sleep(0.5)
            oppene = OppenClosedZapp(True)
            sleep(1)

            try:
                pyautogui.click(pyautogui.locateOnScreen('controller/image/chat_unread.png', confidence=0.8))
            except Exception as e:
                try:
                    pyautogui.click(pyautogui.locateOnScreen('controller/image/chat_read.png', confidence=0.8))
                except Exception as e:
                    try:
                        pyautogui.click(pyautogui.locateOnScreen('controller/image/burger_line.png', confidence=0.8))
                        pyautogui.press("Enter")
                    except Exception as e:
                        sleep(0.5)
                    
            sleep(1)
            try:
                pyautogui.click(pyautogui.locateOnScreen('controller/image/search_icon.png', confidence=0.8))
            except Exception as e:
                try:
                    pyautogui.click(pyautogui.locateOnScreen('controller/image/reset_seachBar.png', confidence=0.8))
                except Exception as e:
                    pyautogui.hotkey("ctrl","f")
                    pyautogui.hotkey("ctrl","a")
                    pyautogui.hotkey("backspace")
                    app = True

            sleep(1)
            pyautogui.write(contact, interval=0.05) 
            if app:
                pyautogui.hotkey("down")
            pyautogui.press('enter')
            sleep(0.5)
            pyautogui.write(msg, interval=0.3)
            pyautogui.press('enter')
            print(f"[{datetime.datetime.now()}] Message sent!")
        except Exception as e:
            pyautogui.alert("The Automation process could not continue\nAn Error was encountered\n !! Verify your Internet connection !!")
            print("Couldn't send the message to "+contact)
            print(f"Error running scheduled tasks: {e}")

def scheduleMessages(lock, stop):
    session = Session()  # Create a session
    now = datetime.datetime.utcnow()
    pending_messages = session.query(Message).all()

    for message in pending_messages:
        # Schedule the Message
        scheduleTableVal = session.query(ScheduledOperation).filter(ScheduledOperation.message_id == message.id).first()
        sendTime = message.send_time
        schedule.every().day.at(sendTime).do(
            sendMessages,
            lock=lock,
            contact=message.receiver,
            msg=message.content
        )

        scheduleTableVal.current_status = "Completed"
        session.commit()

    print("Message Scheduler is running. Waiting to send messages...\n\n")

    while not stop.is_set():
        try:
            schedule.run_pending()
            sleep(1)
        except Exception as e:
            print(f"Error running scheduled tasks: {e}")
            sleep(1)

def start_scheduler(lock, stop):
    stop.clear()  # Ensure the stop event is not set
    thread1 = threading.Thread(target=scheduleMessages, args=(lock, stop), daemon=True)
    thread1.start()

def stop_scheduler(stop):
    stop.set()
    print("Message Scheduler stopped!")

def getAllMessages():
    session = Session()
    allMessages = session.query(Message).all()
    return allMessages

