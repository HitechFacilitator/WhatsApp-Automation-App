from controller.messageController import *
from utils.oppenZapp import *
from multiprocessing import Process, Lock
import threading

if __name__ == "__main__" :
    lock = Lock()
    stop_event = threading.Event()

    createMessage("Rebec","Hello")
    # createMessage("Artino","Am Good","07:53")


    scheduleMessages(lock, stop_event)
    
