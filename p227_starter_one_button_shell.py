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

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        ping_btn = tk.Button(master=window, text="ping", command=do_command)
        ping_btn.grid(row=0,column=0)

window.mainloop()
