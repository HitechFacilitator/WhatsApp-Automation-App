import customtkinter as ctk
from tkinter import Label
from PIL import Image, ImageTk

def show_message_interface(app, controller):
    for widget in app.winfo_children():
        widget.pack_forget()
    
    # Background Frame
    message_frame = ctk.CTkFrame(app, fg_color="#075E54")  # WhatsApp dark green
    message_frame.pack(fill="both", expand=True)

    # Background Image
    background_image = ImageTk.PhotoImage(Image.open("messageBG.png"))  # Replace with actual image path
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

    start_scheduler_button = ctk.CTkButton(header_frame, text="Start Scheduler", width=120, fg_color="#128C7E", hover_color="#128C1E", command=lambda: print("Scheduler Started"))
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
    schedule_entry = ctk.CTkEntry(creation_frame, width=300, placeholder_text="Time in the form HH:MM")
    schedule_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Schedule Button
    schedule_button = ctk.CTkButton(creation_frame, text="Schedule", width=100, fg_color="#25D366", hover_color="#128C7E", command=lambda: print("Message Scheduled"))
    schedule_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

    # Card Section
    card_frame = ctk.CTkFrame(message_frame, fg_color="#DCF8C6", corner_radius=15, width=800, height=400)  # Light green background
    card_frame.pack(pady=20, padx=20)

    title_label = ctk.CTkLabel(card_frame, text="Scheduled Messages", font=("Arial", 20, "bold"), text_color="#075E54")
    title_label.pack(pady=10)

    # Table/List for Messages
    message_table = ctk.CTkFrame(card_frame, fg_color="white", corner_radius=10)
    message_table.pack(fill="both", expand=True, padx=10, pady=10)

    headers = ["Recipient", "Message", "Scheduled Time", "Actions"]
    for header in headers:
        header_label = ctk.CTkLabel(message_table, text=header, font=("Arial", 14, "bold"), text_color="#075E54")
        header_label.grid(row=0, column=headers.index(header), padx=5, pady=5)

    # Example Data
    example_data = [
        {"recipient": "John", "message": "Hello John!", "time": "2025-01-15 10:00 AM"},
        {"recipient": "Doe", "message": "Meeting Reminder", "time": "2025-01-16 02:00 PM"}
    ]

    for idx, row in enumerate(example_data):
        ctk.CTkLabel(message_table, text=row["recipient"], font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=0, padx=5, pady=5)
        ctk.CTkLabel(message_table, text=row["message"], font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=1, padx=5, pady=5)
        ctk.CTkLabel(message_table, text=row["time"], font=("Arial", 12), text_color="#075E54").grid(row=idx+1, column=2, padx=5, pady=5)
        ctk.CTkButton(message_table, text="Edit", width=50, fg_color="#25D366", hover_color="#128C7E").grid(row=idx+1, column=3, padx=2, pady=5)
        ctk.CTkButton(message_table, text="Delete", width=50, fg_color="#FF0000", hover_color="#CC0000").grid(row=idx+1, column=4, padx=2, pady=5)
