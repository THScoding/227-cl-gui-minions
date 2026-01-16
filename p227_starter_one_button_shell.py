import subprocess
import threading
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename   
    
def do_command():
    subprocess.call("ping localhost")
    
def do_command(command):
    global command_textbox, url_entry
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="ping", command=do_command)
ping_btn.pack()
# CODE TO ADD
# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", 
    command=lambda:do_command("ping"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    bg="white", activebackground="gray")
ping_btn.pack() 
#save button

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

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

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()
# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

# Create a Text widget for output with a scrollbar
scrollbar = tk.Scrollbar(frame)
output_text = tksc.ScrolledText(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, state=tk.DISABLED)
scrollbar.config(command=output_text.yview)

# Pack the widgets
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# Create a button to run the netstat command
run_button = tk.Button(root, text="Run netstat -an", command=lambda: run_netstat(output_text))
run_button.pack(pady=10)


def run_netstat(output_widget):
    command = ['netstat', '-an'] 
    
    # Clear previous output 
    output_widget.config(state=tk.NORMAL)
    output_widget.delete('1.0', tk.END)
    output_widget.insert(tk.END, "Running netstat -an...\\n")
    output_widget.config(state=tk.DISABLED)

    def execute_command():
        try:
            # Use subprocess.Popen to capture output
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
            
            # Read and display output line by line
            for line in iter(process.stdout.readline, ''):
                output_widget.config(state=tk.NORMAL)
                output_widget.insert(tk.END, line)
                output_widget.see(tk.END) # Auto-scroll to the bottom
                output_widget.config(state=tk.DISABLED)
            
            process.stdout.close()
            process.wait()
            
            output_widget.config(state=tk.NORMAL)
            output_widget.insert(tk.END, "\\nCommand finished.\\n")
            output_widget.config(state=tk.DISABLED)

        except FileNotFoundError:
            output_widget.config(state=tk.NORMAL)
            output_widget.insert(tk.END, f"Error: '{command[0]}' command not found. Make sure it is in your system's PATH.\\n")
            output_widget.config(state=tk.DISABLED)
        except Exception as e:
            output_widget.config(state=tk.NORMAL)
            output_widget.insert(tk.END, f"An error occurred: {e}\\n")
            output_widget.config(state=tk.DISABLED)

    # Start the command execution in a new thread
    thread = threading.Thread(target=execute_command)
    thread.start()

def mSave():
    filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
    if filename is None:
        return
    text_to_save = ""
    file = open (filename, mode = 'w')
    text_to_save = output_text.get("1.0", tk.END) + "/n" + command_textbox.get("1.0", tk.END)
    file.write(text_to_save)
    file.close()
    
ping_btn = tk.Button(frame, text="Save output", command=mSave)
ping_btn.pack()
    
root.mainloop()
