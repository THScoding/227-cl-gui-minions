import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command():
    command = ["ping", "localhost", "-n", "4"]
    # Windows version to limit to 4 requests: command = ["ping", "localhost", "-n", "4"]
    # Mac version to limit to 4 requests:     command = ["ping", "localhost", "-n", "4"]
    
    subprocess.run(command)
    # 1. Create the main application window
    
window = tk.Tk()
window.title("ip config")
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 5):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        ping_btn = tk.Button(master=window, text="ping", command=do_command)
        ping_btn.grid(row=0,column=0)
        
                # creates the frame with label for the text box
        frame_URL = tk.Frame(window, pady=10,  bg="black") # change frame color
        frame_URL.grid(row=1,column=1)

        # decorative label
        url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
            compound="center",
            font=("comic sans", 14),
            bd=0, 
            relief=tk.FLAT, 
            cursor="heart",
            fg="mediumpurple3",
            bg="black")
        url_label.pack(side=tk.LEFT)
        url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
        url_entry.pack(side=tk.LEFT)

        frame = tk.Frame(window,  bg="black") # change frame color
        frame.grid(row=1,column=1)
        # Adds an output box to GUI.
        command_textbox = tksc.ScrolledText(window, height=10, width=100)
        command_textbox.grid(row=2,column=0)

window.mainloop()
