from controller.statusController import *
from utils.oppenZapp import *
from multiprocessing import Process, Lock

if __name__ == "__main__" :
    lock = Lock()
    stop_event = threading.Event()

    # createStatus("/home/hitechangel/Pictures/chat3.png", True, "My App 3", "07:51")
    # createStatus("Finally\nI did It\n\n :)", False, "", "19:56")
    createStatus("/home/hitechangel/Pictures/chat2.png", True, "My App")
    
    scheduleStatus(lock, stop_event)
    
