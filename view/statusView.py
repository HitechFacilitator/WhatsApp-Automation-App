import customtkinter as ctk
from tkinter import Canvas, Frame, Scrollbar, Label
import tkinter as tk
import threading
from PIL import Image, ImageTk
from controller.statusController import *
from multiprocessing import Lock
from utils.notifications import *

running2 = False

def show_status_interface(app, controller):
    lock = Lock()
    # Create a threading Event to signal when to stop the scheduler
    stop_event2 = threading.Event()

    for widget in app.winfo_children():
        widget.pack_forget()

    if not running2:
        on_notify("NB \nAutomated Status is not available for the Whatsapp Destop App\nOnly Available on WhatsApp Web" ,"white", 500, 150)

    # Background Frame
    status_frame = ctk.CTkFrame(app, fg_color="#075E54")  # WhatsApp dark green
    status_frame.pack(fill="both", expand=True)

    # Background Image
    background_image = ImageTk.PhotoImage(Image.open("view/statusBG.png"))  # Replace with actual image path
    background_label = Label(status_frame, image=background_image)
    background_label.image = background_image
    background_label.place(relwidth=1, relheight=1)

    # Header Section
    header_frame = ctk.CTkFrame(status_frame, fg_color="#25D366", height=80, corner_radius=10)  # WhatsApp green
    header_frame.pack(fill="x", pady=10)

    back_button = ctk.CTkButton(header_frame, text="Back", width=80, fg_color="#075E54", hover_color="#128C7E", command=lambda: controller.show_home())
    back_button.pack(side="left", padx=10, pady=20)

    header_label = ctk.CTkLabel(header_frame, text="Status Dashboard", font=("Arial", 24, "bold"), text_color="white")
    header_label.pack(side="left", padx=20)

    if running2:
        startScheduler_label = ctk.CTkLabel(header_frame, text="Scheduler is running.......", font=("Arial", 14), text_color="red")
        startScheduler_label.pack(side="right", padx=10, pady=20)
    stop_scheduler_button = ctk.CTkButton(header_frame, text="Stop Scheduler", width=120, fg_color="#128C7E", hover_color="#128C1E", command=lambda: stopScheduler(stop_event2, controller))
    stop_scheduler_button.pack(side="right", padx=10, pady=20)
    start_scheduler_button = ctk.CTkButton(header_frame, text="Start Scheduler", width=120, fg_color="#128C7E", hover_color="#128C1E", command=lambda: startScheduler(lock, stop_event2, controller))
    start_scheduler_button.pack(side="right", padx=10, pady=20)

    # Status Creation Section
    creation_frame = ctk.CTkFrame(status_frame, fg_color="#DCF8C6", corner_radius=15, width=800, height=200)
    creation_frame.pack(pady=1, padx=20)

    title1_label = ctk.CTkLabel(creation_frame, text="Media Content Status", font=("Arial", 18), text_color="blue")
    title1_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Recipient Field
    file_label = ctk.CTkLabel(creation_frame, text="Select File:", font=("Arial", 14), text_color="#075E54")
    file_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    file_entry = ctk.CTkEntry(creation_frame, width=300, placeholder_text="Media Path")
    file_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    statusMsg_label = ctk.CTkLabel(creation_frame, text="Status Message:", font=("Arial", 14), text_color="#075E54")
    statusMsg_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    statusMsg_entry = ctk.CTkTextbox(creation_frame, height=10, width=300)
    statusMsg_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    title2_label = ctk.CTkLabel(creation_frame, text="Text Content Status", font=("Arial", 18), text_color="blue")
    title2_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Status Text Field
    text_label = ctk.CTkLabel(creation_frame, text="Status Text:", font=("Arial", 14), text_color="#075E54")
    text_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    text_entry = ctk.CTkTextbox(creation_frame, height=80, width=300)
    text_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Match the Canvas background to the frame's color for a "transparent" look
    frame_bg_color = creation_frame.cget("fg_color")  # Get the frame's background color
    # Embed a standard tkinter Canvas in the CTkFrame
    canvas = tk.Canvas(creation_frame, highlightthickness=0, bg=frame_bg_color)
    canvas.grid(row=5, column=0, columnspan=2, sticky="nsew")  # Span across two columns
    # Draw a line across the canvas
    canvas_width = 450
    canvas_height = 15
    line_start_x = 0
    line_start_y = canvas_height // 2
    line_end_x = canvas_width
    line_end_y = canvas_height // 2
    # Set canvas size to match the frame
    canvas.config(width=canvas_width, height=canvas_height)
    canvas.create_line(line_start_x, line_start_y, line_end_x, line_end_y, fill="black", width=5)

    # Schedule Time Field
    schedule_label = ctk.CTkLabel(creation_frame, text="Schedule Time:", font=("Arial", 14), text_color="#075E54")
    schedule_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    scheduleTime_entry = ctk.CTkEntry(creation_frame, width=300, placeholder_text="Time in the form HH:MM")
    scheduleTime_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Schedule Button
    schedule_button = ctk.CTkButton(creation_frame, text="Schedule", width=100, fg_color="#25D366", hover_color="#128C7E", command=lambda: add_a_status(stop_event2, status_table, file_entry.get(),statusMsg_entry.get("1.0", "end"),text_entry.get("1.0", "end"),scheduleTime_entry.get()))
    schedule_button.grid(row=7, column=1, padx=10, pady=10, sticky="e")

    nb_label = ctk.CTkLabel(creation_frame, text="NB\nYou cannot create two status schedule type\n(i.e Media and Text status type) at a time", font=("Arial", 14), text_color="brown")
    nb_label.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    # Card Section with Scrollbar
    card_frame = ctk.CTkFrame(status_frame, fg_color="#DCF8C6", corner_radius=10, width=800, height=400)  # Light green background
    card_frame.pack(pady=5, padx=5, fill="x", expand=True)

    title_label = ctk.CTkLabel(card_frame, text="Scheduled Status", font=("Arial", 20, "bold"), text_color="#075E54")
    title_label.pack(pady=10)

    # Add Scrollable Area for Status Table
    table_canvas = Canvas(card_frame, bg="white", highlightthickness=0)
    table_canvas.pack(side="left", fill="both", expand=True)

    table_scrollbar = Scrollbar(card_frame, orient="vertical", command=table_canvas.yview)
    table_scrollbar.pack(side="right", fill="y")

    table_canvas.configure(yscrollcommand=table_scrollbar.set)
    table_canvas.bind('<Configure>', lambda e: table_canvas.configure(scrollregion=table_canvas.bbox("all")))

    status_table = ctk.CTkFrame(table_canvas, fg_color="white")
    table_canvas.create_window((0, 0), window=status_table, anchor="nw")

    display_status_table(status_table)

def add_a_status(stop_event2, status_table, path="", msg="", text="", time=""):
    if path and text != "\n":
        on_notify("Look at the NB below the Schedule Button", "red")
        return
    elif text != "\n" and msg != "\n":
        on_notify("Look at the NB below the Schedule Button\nFields of different types can't\n be filled simultaneously", "red")
        return
    if not path and msg == "\n" and text == "\n":
        on_notify("What do you want us to post?\n Your fields are empty", "red")
        return
    if path:
        flag = createStatus(path, True, msg, time)
        if flag != "" and flag != None:
            on_notify(flag, "orange", 400, 115)
            return
        show_notification("Schedule Status\nCreated Successfully", 2)
        stop_scheduler(stop_event2)
    elif text != "\n" :
        flag = createStatus(text, False, "", time)
        if flag != "" and flag != None:
            on_notify(flag, "orange", 400, 115)
            return
        stop_scheduler(stop_event2)
    else:
        print("...............")
    display_status_table(status_table)
    show_notification("Schedule Status\nCreated Successfully\nRestart the scheduler\nIf started !!", 3, "yellow")

def startScheduler(lock, stop_event2, controller):
    global running2
    running2 = True
    controller.show_status_dashboard()
    # show_notification("Message scheduler running ........", 2, "red")
    start_scheduler(lock, stop_event2)

def stopScheduler(stop_event2, controller):
    global running2
    running2 = False
    controller.show_status_dashboard()
    stop_scheduler(stop_event2)

def display_status_table(status_table):
    headers = ["Media?", "Path or Content", "Media message", "Scheduled Time", "Actions"]
    for header in headers:
        header_label = ctk.CTkLabel(status_table, text=header, font=("Arial", 14, "bold"), text_color="#075E54")
        header_label.grid(row=0, column=headers.index(header), padx=55, pady=10)

    allStatus = getAllStatus()

    idx=0
    for stat in allStatus:
        ctk.CTkLabel(status_table, text=stat.media, font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=0, padx=7, pady=5)
        ctk.CTkLabel(status_table, text=stat.content_or_path, font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=1, padx=7, pady=5)
        ctk.CTkLabel(status_table, text=stat.mediaText, font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=2, padx=7, pady=5)
        ctk.CTkLabel(status_table, text=stat.send_time, font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=3, padx=7, pady=5)
        ctk.CTkButton(status_table, text="Edit", width=50, fg_color="#25D366", hover_color="#128C7E").grid(row=idx+1, column=4, padx=2, pady=5)
        ctk.CTkButton(status_table, text="Delete", width=50, fg_color="#FF0000", hover_color="#CC0000").grid(row=idx+1, column=5, padx=2, pady=5)
        idx=idx+1
