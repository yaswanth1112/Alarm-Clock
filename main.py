from time import strftime
import pygame
from tkinter import Label, Tk, StringVar, Button, messagebox, Entry
from datetime import datetime

# Initialize Pygame for audio playback
pygame.mixer.init()

# Constants for audio file
ALARM_SOUND = 'alarm.wav'  # Ensure this file exists in the directory

# Create main window
window = Tk()
window.title("Clock and Alarm")
window.geometry("400x200")
window.configure(bg="green")
window.resizable(False, False)

# Create StringVar to hold dynamic greetings
greeting_var = StringVar()

# Create clock label
clock_label = Label(
    window, bg="black", fg="green", font=("Arial", 30, "bold"), relief="flat"
)
clock_label.place(x=50, y=20)

# Create greeting label
greeting_label = Label(
    window, bg="green", fg="white", font=("Arial", 20, "italic"), relief="flat"
)
greeting_label.place(x=50, y=120)

# Create alarm time entry
alarm_time_entry = Entry(window, font=("Arial", 14))
alarm_time_entry.place(x=50, y=160)

# Create set alarm button
def set_alarm():
    global alarm_time  # Declare alarm_time as global
    alarm_time = alarm_time_entry.get()
    if not alarm_time:
        messagebox.showerror("Input Error", "Please enter a time for the alarm.")
    else:
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

set_alarm_button = Button(window, text="Set Alarm", command=set_alarm)
set_alarm_button.place(x=250, y=155)

# Initialize alarm time variable
alarm_time = None

def update_label():
    global alarm_time  # Declare alarm_time as global to modify it
    current_time = strftime("%H:%M:%S\n%d-%m-%Y")
    clock_label.configure(text=current_time)
    
    # Update greeting based on time
    now = datetime.now()
    hour = now.hour
    if 5 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    elif 18 <= hour < 22:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"
    greeting_var.set(greeting)
    greeting_label.configure(text=greeting_var.get())
    
    # Check if it's time for the alarm
    if alarm_time and strftime("%H:%M") == alarm_time:
        pygame.mixer.music.load(ALARM_SOUND)
        pygame.mixer.music.play()
        messagebox.showinfo("Alarm", "Alarm ringing!")
        alarm_time = None  # Clear alarm after it rings

    # Schedule the update function to be called again
    clock_label.after(1000, update_label)  # Update every second

# Start the update loop
update_label()

# Start the Tkinter event loop
window.mainloop()
