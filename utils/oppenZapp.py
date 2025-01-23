import pyautogui
from time import *

def verifyOppenZapp() :
    try :
        pyautogui.locateCenterOnScreen("controller/image/chat_open.png", confidence=0.8)
    except Exception as e:
        try :
            pyautogui.locateCenterOnScreen("controller/image/channel_open.png", confidence=0.8)
        except Exception as e:
            try :
                pyautogui.locateCenterOnScreen("controller/image/status_open.png", confidence=0.8)
            except Exception as e:
                try :
                    pyautogui.locateCenterOnScreen("controller/image/community_open.png", confidence=0.8)
                except Exception as e:
                    try :
                        pyautogui.locateCenterOnScreen("controller/image/call_open.png", confidence=0.8)
                    except Exception as e:
                        print("WhatsApp Isn't Openned")
                        raise
    print("WhatsApp is openned")

def OppenWhatsapp(web=True) :
    if web:
        try:
            pyautogui.click(pyautogui.locateCenterOnScreen('controller/image/firefox.png', confidence=0.7))
        except Exception as e:
            pyautogui.hotkey("win")
            sleep(1)
            pyautogui.write('firefox', interval=0.03)
            sleep(1)
            pyautogui.press('enter')
        sleep(1.5)
        # pyautogui.hotkey("win", "up")
        pyautogui.hotkey("win", "right")
        sleep(0.5)
        # pyautogui.click(x=450, y=100) 
        pyautogui.click(x=1200, y=95) 
        pyautogui.write('https://web.whatsapp.com/\n', interval=0.03)
        sleep(2)
        try:
            while pyautogui.locateCenterOnScreen('controller/image/loading_bar1.png', confidence=0.8) :
                sleep(0.5)
                # print("loading bar 1")
        except Exception as e:
            sleep(0.5)
        sleep(0.5)
        try:
            pyautogui.locateCenterOnScreen('controller/image/loading_chat.png', confidence=0.8)
            print("Whatsapp is loading chats .............................")
            while pyautogui.locateCenterOnScreen('controller/image/loading_chat.png', confidence=0.8) :
                sleep(0.5)
                # print("loading chat")
        except Exception as e:
            try:
                while pyautogui.locateCenterOnScreen('controller/image/loading_bar2.png', confidence=0.8) :
                    # print("loading bar 2")
                    sleep(0.5)
            except Exception as e:
                sleep(0.5)
    else:
        pyautogui.hotkey("win")
        sleep(1)
        pyautogui.write('WhatsApp', interval=0.03)
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.hotkey("win", "up")
    sleep(1)


    

def OppenClosedZapp(web):
    try:
        verifyOppenZapp()
        return True
    except Exception as e:
        sleep(0.5)
        OppenWhatsapp(web)
        return False


