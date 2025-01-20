import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import threading
from tkinter import PhotoImage, Label
from homeView import show_home_interface, play_video
from messageView import show_message_interface
from statusView import show_status_interface

class AppController:
    def __init__(self, root):
        self.root = root

    def show_home(self):
        show_home_interface(self.root, self)

    def show_message_dashboard(self):
        show_message_interface(self.root, self)

    def show_status_dashboard(self):
        show_status_interface(self.root, self)


# Main Application
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("WhatsApp Automation")
    app.geometry("1140x750")
    app.iconphoto(False, PhotoImage(file="app_logo.png"))  # Replace with actual logo path
    ctk.set_appearance_mode("dark")
    app.resizable(False, False)  # Prevent window resizing

    controller = AppController(app)
    play_video(app, "welcome_video.mp4", controller.show_home)
    # controller.show_home()  # Start with the home interface

    app.mainloop()


