import customtkinter as ctk
from tkinter import Label, Text
from PIL import Image, ImageTk
import cv2
import time
import threading

def play_video(app, video_path, on_complete):
    video_label = Label(app)
    video_label.pack(fill="both", expand=True)

    cap = cv2.VideoCapture(video_path)

    def stream_video():
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (app.winfo_width(), app.winfo_height()))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
                video_label.configure(image=frame)
                video_label.image = frame
            else:
                break
        cap.release()
        video_label.pack_forget()
        on_complete()

    threading.Thread(target=stream_video, daemon=True).start()

def show_home_interface(app, controller):
    for widget in app.winfo_children():
        widget.pack_forget()

    # Background Image
    bg_image = ImageTk.PhotoImage(Image.open("homeBG.png"))  # Replace with actual path
    bg_label = Label(app, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(relwidth=1, relheight=1)

    # Top Slider
    slider_frame = ctk.CTkFrame(app, height=300, fg_color="transparent")
    slider_frame.place(relx=0.5, rely=0.2, anchor="center")

    # Slider Images with Text Overlay
    slide_images = ["slide1.png", "slide2.png", "slide3.png"]  # Replace with actual paths
    slide_texts = [
        "Automate Your WhatsApp Experience 🌟\nPlan, schedule, and let WASAM do the rest!",
        "Keep Your WhatsApp Status Fresh 🔄\nPost statuses automatically, exactly when you want!",
        "Never Forget to Message! 📅\nSchedule WhatsApp messages effortlessly and stay connected.",
    ]
    slide_index = 0

    def update_slide():
        nonlocal slide_index
        slide_index = (slide_index + 1) % len(slide_images)
        img = Image.open(slide_images[slide_index]).resize((900, 300))
        img = ImageTk.PhotoImage(img)
        slider_label.configure(image=img)
        slider_label.image = img
        slider_text_label.configure(text=slide_texts[slide_index])
        app.after(3000, update_slide)

    slider_label = Label(slider_frame)
    slider_label.pack(fill="both", expand=True)

    slider_text_label = ctk.CTkLabel(slider_frame, text="", font=("Arial", 16, "bold"), text_color="white")
    slider_text_label.pack()

    update_slide()

    # Bottom Section Divided into 3 Parts
    bottom_frame = ctk.CTkFrame(app, fg_color="transparent")
    bottom_frame.place(relx=0.5, rely=0.7, anchor="center")

    # Text Area in the Middle
    text_card = ctk.CTkFrame(bottom_frame, corner_radius=10, fg_color="gray17", width=300, height=400)
    text_card.pack(side="left", padx=20, pady=20)

    text_header = ctk.CTkLabel(text_card, text="\n\nWASAM (WhatsApp Automated Status and Message) \n\nlets you schedule WhatsApp messages \nand statuses effortlessly.\nDecide the time, and WASAM sends your messages \nor posts your statuses automatically.\nPerfect for staying connected, organized, \nand on top of your communication game.\n\n\nSave time. Stay connected. Choose WASAM.\n\n\n", font=("Arial", 18, "bold"))
    text_header.pack(pady=10)

    # Message Card
    message_card = ctk.CTkFrame(bottom_frame, corner_radius=10, fg_color="gray30", width=300, height=400)
    message_card.pack(side="left", padx=20, pady=20)

    msg_header = ctk.CTkLabel(message_card, text="Automated Messages", font=("Arial", 18, "bold"))
    msg_header.pack(pady=10)

    msg_img = ImageTk.PhotoImage(Image.open("message_image.png").resize((250, 150)))  # Replace with actual path
    msg_image = Label(message_card, image=msg_img, bg="gray30")
    msg_image.image = msg_img
    msg_image.pack(pady=10)

    msg_button = ctk.CTkButton(message_card, text="Here We Go", command=lambda: controller.show_message_dashboard())
    msg_button.pack(pady=10)

    # Status Card
    status_card = ctk.CTkFrame(bottom_frame, corner_radius=10, fg_color="gray30", width=300, height=400)
    status_card.pack(side="left", padx=20, pady=20)

    status_header = ctk.CTkLabel(status_card, text="Post Status", font=("Arial", 18, "bold"))
    status_header.pack(pady=10)

    status_img = ImageTk.PhotoImage(Image.open("status_image.png").resize((250, 150)))  # Replace with actual path
    status_image = Label(status_card, image=status_img, bg="gray30")
    status_image.image = status_img
    status_image.pack(pady=10)

    status_button = ctk.CTkButton(status_card, text="Here We Go", command=lambda: controller.show_status_dashboard())
    status_button.pack(pady=10)
