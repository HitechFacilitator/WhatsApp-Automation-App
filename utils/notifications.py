import customtkinter as ctk
import threading

def show_notification(message, duration=3):
    # Create a top-level window for the notification
    notification = ctk.CTkToplevel()
    notification.geometry("400x200")
    notification.title("Notification")
    notification.resizable(False, False)
    
    # Center the notification on the screen
    notification.update_idletasks()
    screen_width = notification.winfo_screenwidth()
    screen_height = notification.winfo_screenheight()
    window_width = 300
    window_height = 100
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    notification.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Add a message to the notification
    message_label = ctk.CTkLabel(notification, text=message, font=("Arial", 16), text_color="green")
    message_label.pack(pady=10, padx=5)

    # Automatically close the notification after the specified duration
    threading.Thread(target=lambda: (notification.after(duration * 1000, notification.destroy)), daemon=True).start()


def on_notify(message, color, wid=300, heigh=100):
    notification = ctk.CTkToplevel()
    notification.geometry("300x300")
    notification.title("Notification")
    notification.resizable(False, False)

    # Center the notification on the screen
    notification.update_idletasks()
    screen_width = notification.winfo_screenwidth()
    screen_height = notification.winfo_screenheight()
    window_width = wid
    window_height = heigh
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    notification.geometry(f"{window_width}x{window_height}+{x}+{y}")

    message_label = ctk.CTkLabel(notification, text=message, font=("Arial", 16), text_color=color)
    message_label.pack(pady=10)

    # Add close button
    close_button = ctk.CTkButton(notification, text="Close", command=notification.destroy)
    close_button.pack(pady=10)


