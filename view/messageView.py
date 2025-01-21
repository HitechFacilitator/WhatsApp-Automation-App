import customtkinter as ctk
from tkinter import Canvas, Frame, Scrollbar, Label
import tkinter as tk
import threading
from multiprocessing import Lock
from time import sleep
from PIL import Image, ImageTk
from controller.messageController import *
from utils.notifications import *

def show_message_interface(app, controller):
    lock = Lock()
    # Create a threading Event to signal when to stop the scheduler
    stop_event = threading.Event()

    for widget in app.winfo_children():
        widget.pack_forget()
    
    # Background Frame
    message_frame = ctk.CTkFrame(app, fg_color="#075E54")  # WhatsApp dark green
    message_frame.pack(fill="both", expand=True)

    # Background Image
    background_image = ImageTk.PhotoImage(Image.open("view/messageBG.png"))  # Replace with actual image path
    background_label = Label(message_frame, image=background_image)
    background_label.image = background_image
    background_label.place(relwidth=1, relheight=1)

    # Header Section
    header_frame = ctk.CTkFrame(message_frame, fg_color="#25D366", height=80, corner_radius=10)  # WhatsApp green
    header_frame.pack(fill="x", pady=10)

    back_button = ctk.CTkButton(header_frame, text="Back", width=80, fg_color="#075E54", hover_color="#128C7E", command=lambda: controller.show_home())
    back_button.pack(side="left", padx=10, pady=20)

    header_label = ctk.CTkLabel(header_frame, text="Message Dashboard", font=("Arial", 24, "bold"), text_color="white")
    header_label.pack(side="left", padx=20)

    stop_scheduler_button = ctk.CTkButton(header_frame, text="Stop Scheduler", width=120, fg_color="#128C7E", hover_color="#128C1E", command=lambda: stop_scheduler(stop_event))
    stop_scheduler_button.pack(side="right", padx=10, pady=20)
    start_scheduler_button = ctk.CTkButton(header_frame, text="Start Scheduler", width=120, fg_color="#128C7E", hover_color="#128C1E", command=lambda: start_scheduler(lock, stop_event))
    start_scheduler_button.pack(side="right", padx=10, pady=20)

    # Message Creation Section
    creation_frame = ctk.CTkFrame(message_frame, fg_color="#DCF8C6", corner_radius=15, width=800, height=200)  # Light green background
    creation_frame.pack(pady=20, padx=20)

    # Recipient Field
    recipient_label = ctk.CTkLabel(creation_frame, text="Recipient:", font=("Arial", 14), text_color="#075E54")
    recipient_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    recipient_entry = ctk.CTkEntry(creation_frame, width=300,placeholder_text="The recipient Number or it WhatsApp Name")
    recipient_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Message Field
    message_label = ctk.CTkLabel(creation_frame, text="Message:", font=("Arial", 14), text_color="#075E54")
    message_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    message_entry = ctk.CTkTextbox(creation_frame, height=80, width=300)
    message_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Schedule Time Field
    schedule_label = ctk.CTkLabel(creation_frame, text="Schedule Time:", font=("Arial", 14), text_color="#075E54")
    schedule_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    scheduleTime_entry = ctk.CTkEntry(creation_frame, width=300, placeholder_text="Time in the form HH:MM")
    scheduleTime_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Schedule Button
    schedule_button = ctk.CTkButton(creation_frame, text="Schedule", width=100, fg_color="#25D366", hover_color="#128C7E", command=lambda: add_a_message(recipient_entry.get(), message_entry.get("1.0", "end"), scheduleTime_entry.get(), message_table, stop_event))
    schedule_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

    # Card Section
    card_frame = ctk.CTkFrame(message_frame, fg_color="#DCF8C6", corner_radius=15, width=800, height=400)  # Light green background
    card_frame.pack(pady=5, padx=5, fill="x", expand=True)

    title_label = ctk.CTkLabel(card_frame, text="Scheduled Messages", font=("Arial", 20, "bold"), text_color="#075E54")
    title_label.pack(pady=10)

    # Add Scrollable Area for Status Table
    table_canvas = Canvas(card_frame, bg="white", highlightthickness=0)
    table_canvas.pack(side="left", fill="both", expand=True)

    table_scrollbar = Scrollbar(card_frame, orient="vertical", command=table_canvas.yview)
    table_scrollbar.pack(side="right", fill="y")

    table_canvas.configure(yscrollcommand=table_scrollbar.set)
    table_canvas.bind('<Configure>', lambda e: table_canvas.configure(scrollregion=table_canvas.bbox("all")))

    message_table = ctk.CTkFrame(table_canvas, fg_color="white")
    table_canvas.create_window((0, 0), window=message_table, anchor="nw")

    display_message_table(message_table)

def add_a_message(recip, msg, time, message_table, stop_event):
    if not recip:
        on_notify("The Receiver name or number is needed", "red")
        return
    if msg == "\n":
        on_notify("The message content field is empty", "red")
        return
    flag = createMessage(recip, msg, time)
    # print(flag)
    if flag != "" and flag != None:
        on_notify(flag, "orange", 400,115)
        return
    show_notification("Schedule Message\nCreated Successfully\nRestart the scheduler\nIf started !!", 3, "yellow")
    stop_scheduler(stop_event)
    display_message_table(message_table)

def display_message_table(message_table):
    headers = ["Recipient", "Message", "Scheduled Time", "Actions"]
    for header in headers:
        header_label = ctk.CTkLabel(message_table, text=header, font=("Arial", 14, "bold"), text_color="#075E54")
        header_label.grid(row=0, column=headers.index(header), padx=65, pady=5)

    allMessages = getAllMessages()

    idx=0
    for msg in allMessages:
        ctk.CTkLabel(message_table, text=msg.receiver, font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=0, padx=5, pady=5)
        ctk.CTkLabel(message_table, text=msg.content, font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=1, padx=5, pady=5)
        ctk.CTkLabel(message_table, text=msg.send_time, font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=2, padx=5, pady=5)
        ctk.CTkButton(message_table, text="Edit", width=50, fg_color="#25D366", hover_color="#128C7E").grid(row=idx+1, column=3, padx=2, pady=5)
        ctk.CTkButton(message_table, text="Delete", width=50, fg_color="#FF0000", hover_color="#CC0000").grid(row=idx+1, column=4, padx=2, pady=5)
        idx=idx+1

