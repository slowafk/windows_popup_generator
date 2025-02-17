import tkinter as tk
from tkinter import messagebox

def show_popup():
    title = title_entry.get()
    message = message_entry.get("1.0", tk.END).strip()
    
    # Show a Windows 95-style messagebox
    messagebox.showinfo(title, message)

# Create the main window
root = tk.Tk()
root.title("Win95 Pop-Up Generator")
root.geometry("300x250")

# Title Input
tk.Label(root, text="Title:").pack()
title_entry = tk.Entry(root)
title_entry.pack(fill='x', padx=10)

# Message Input
tk.Label(root, text="Message:").pack()
message_entry = tk.Text(root, height=5)
message_entry.pack(fill='x', padx=10)

# Generate Button
tk.Button(root, text="Show Pop-Up", command=show_popup).pack(pady=10)

# Run the app
root.mainloop()
