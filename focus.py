#!/usr/bin/env python
import time
import tkinter as tk
from datetime import datetime


entries = []
index = 0
start = False

pressed = False
counter = 21600
running = False

def counter_label(label, task):
    def count():
        global window
        if running:
            global counter

            # To manage the intial delay.
            if counter==0:
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%M:%S")
                display=string

            label.config(text=display)   # Or label.config(text=display)
            label.after(1000, count)
            counter += 1

            task.config(text=str(entries[index][0]))

            if(tt.minute < entries[index][1]):
                label.config(fg="green")
            else:
                label.config(fg="red")


    # Triggering the start of the counter.
    count()

# start function of the stopwatch
def Start(label, task):
    global pressed, running, index, entries, time_button_text
    running=True
    if(pressed and label['fg'] == "green"):
        Stop()
    elif(pressed and label['fg'] == "red"):
        Reset(label)
        index += 1
        if(index > len(entries)-1):
            index = 0
    else:
        counter_label(label, task)
    if pressed:
        time_button_text.set("Stop")
    else:
        time_button_text.set("Start")
    pressed = not pressed

# Stop function of the stopwatch
def Stop():
    global running
    running = False

# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=21600

def submit_entry():
    global name_entry, time_entry
    if(name_entry.get() != '' and time_entry.get() != ''):
        entries.append((name_entry.get(), int(time_entry.get())))
    name_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

def update():
    global frame, window, entries, index, window
    submit_entry()
    rows = 2
    for entry in entries:
        tk.Label(frame, text=entry[0]).grid(row=rows, column=1)
        tk.Label(frame, text=entry[1]).grid(row=rows, column=2)
        rows += 1

window = tk.Tk()
window.title("Focus")
frame = tk.Frame(window)
frame.pack()


tk.Label(frame, text="Name").grid(row=0, column=0)
tk.Label(frame, text="Time").grid(row=0, column=2)
name_entry = tk.Entry(frame)
time_entry = tk.Entry(frame, width=2)

name_entry.grid(row=0, column=1)
time_entry.grid(row=0, column=4)

submit = tk.Button(frame, text="Submit", command=update)
submit.grid(row=0, column=5)

time_button_text = tk.StringVar()
time_button_text.set("Start")
current_task = tk.Label(frame, text="Task", fg="green")
current_task.grid(row=1, column=0, columnspan=2)
time_label = tk.Label(frame,text="Stopwatch", fg="green")
time_label.grid(row=1, column=2, columnspan=3)
time_button = tk.Button(frame, textvariable=time_button_text, command=lambda:Start(time_label, current_task))
time_button.grid(row=1, column=5)

window.mainloop()
