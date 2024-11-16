import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Setup the UI
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")

# Labels
length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=5)

# Entry for password length
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Entry to display password
password_entry = tk.Entry(window, width=30)
password_entry.pack(pady=5)

# Button to copy password
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_password)
copy_button.pack(pady=10)

# Run the app
window.mainloop()
