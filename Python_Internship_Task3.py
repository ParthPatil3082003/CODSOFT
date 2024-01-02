import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Invalid length. Please enter a positive integer.")
            return

        password = generate_password(length)
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the password length.")

# Create main window
window = tk.Tk()
window.title("Password Generator By Parth Patil")

# Entry widget for user input
entry_length = tk.Entry(window, width=10)
entry_length.grid(row=0, column=0, padx=10, pady=10)

# Button to generate and display password
generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=0, column=1, padx=10, pady=10)

# Label to display the generated password
result_label = tk.Label(window, text="Generated Password: ")
result_label.grid(row=1, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()
