# https:
from utils.oppenZapp import *
from multiprocessing import Process, Lock

from controller.messageController import *
from controller.statusController import *

if __name__ == "__main__" :
    # lock = Lock()
    createStatus("/home/hitechangel/Pictures/chat2.png", True, "My App")
    createMessage("Rebec","Hello")
    # createMessage("Rebec","Hello")
    createMessage("Artino","Am Good","04:28")

    # createStatus("/home/hitechangel/Pictures/chat3.png", True, "My App 3", "04:29")

    # scheduleMessages(lock)
    
    # process1 = Process(target=scheduleStatus, args=(lock,))
    # print("Status scheduled ok")
    # process2 = Process(target=scheduleMessages, args=(lock,))
    # print("Message scheduled ok")

    # # Start the processes
    # process1.start()
    # process2.start()

    # # Wait for both processes to complete
    # process1.join()
    # process2.join()
    
    
    # lok=False
    # OppenClosedZapp(lok)
    # OppenWhatsapp() 
    # verifyOppenZapp()
    # sendMessages("prince","loki")
    # createStatus("/home/hitechangel/Pictures/chat2.png", True, "My App")
    
    # scheduleStatus()
    
    # createMessage("Python","Testing connection with database","00:36")
    # sleep(3)
    # scheduleMessages()
