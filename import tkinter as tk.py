import tkinter as tk
import subprocess
import threading

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

# --- Tkinter GUI Setup ---
window = tk.Tk()
window.title("Netstat Viewer")
window.geometry("800x600")

frame = tk.Frame(window)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a Text widget for output with a scrollbar
scrollbar = tk.Scrollbar(frame)
output_text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, state=tk.DISABLED)
scrollbar.config(command=output_text.yview)

# Pack the widgets
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a button to run the netstat command
run_button = tk.Button(window, text="Run netstat -an", command=lambda: run_netstat(output_text))
run_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
