import customtkinter as ctk
from tkinter import Canvas, Frame, Scrollbar, Label
import tkinter as tk
from PIL import Image, ImageTk

def show_status_interface(app, controller):
    for widget in app.winfo_children():
        widget.pack_forget()

    # Background Frame
    status_frame = ctk.CTkFrame(app, fg_color="#075E54")  # WhatsApp dark green
    status_frame.pack(fill="both", expand=True)

    # Background Image
    background_image = ImageTk.PhotoImage(Image.open("statusBG.png"))  # Replace with actual image path
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

    start_scheduler_button = ctk.CTkButton(header_frame, text="Start Scheduler", width=120, fg_color="#128C7E", hover_color="#128C1E", command=lambda: print("Scheduler Started"))
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
    schedule_entry = ctk.CTkEntry(creation_frame, width=300, placeholder_text="Time in the form HH:MM")
    schedule_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Schedule Button
    schedule_button = ctk.CTkButton(creation_frame, text="Schedule", width=100, fg_color="#25D366", hover_color="#128C7E", command=lambda: print("Message Scheduled"))
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

    headers = ["Media?", "Path or Content", "Media message", "Scheduled Time", "Actions"]
    for header in headers:
        header_label = ctk.CTkLabel(status_table, text=header, font=("Arial", 14, "bold"), text_color="#075E54")
        header_label.grid(row=0, column=headers.index(header), padx=55, pady=10)

    # Example Data
    example_data = [
        {"media": "False", "content_or_path": "Hello John!", "mediaText":"kdjhsdjgshdgh", "time": "2025-01-15 10:00 AM"},
        {"media": "False", "content_or_path": "Hello John!", "mediaText":"kdjhsdjgshdgh", "time": "2025-01-15 10:00 AM"},
        {"media": "False", "content_or_path": "Hello John!", "mediaText":"kdjhsdjgshdgh", "time": "2025-01-15 10:00 AM"},
        {"media": "True", "content_or_path": "I am the\ngod of war", "mediaText":"Roky boy", "time": "2025-04-15 21:23 AM"}
    ]

    for idx, row in enumerate(example_data):
        ctk.CTkLabel(status_table, text=row["media"], font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=0, padx=7, pady=5)
        ctk.CTkLabel(status_table, text=row["content_or_path"], font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=1, padx=7, pady=5)
        ctk.CTkLabel(status_table, text=row["mediaText"], font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=2, padx=7, pady=5)
        ctk.CTkLabel(status_table, text=row["time"], font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=3, padx=7, pady=5)
        ctk.CTkButton(status_table, text="Edit", width=50, fg_color="#25D366", hover_color="#128C7E").grid(row=idx+1, column=4, padx=2, pady=5)
        ctk.CTkButton(status_table, text="Delete", width=50, fg_color="#FF0000", hover_color="#CC0000").grid(row=idx+1, column=5, padx=2, pady=5)
