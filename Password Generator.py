import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")

def accept_click():
    username = username_entry.get()
    password = generated_password_entry.get()
    messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password}")

def reset_click():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Password Generator")

# Heading
heading_label = tk.Label(window, text="Password Generator", font=("Arial", 20, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

# Common width for labels
label_width = 18

# Username
username_label = tk.Label(window, text="Enter user name:", anchor="w", width=label_width)
username_label.grid(row=1, column=0, padx=10, pady=5)

username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1, padx=10, pady=5)

# Password Length
length_label = tk.Label(window, text="Enter password length:", anchor="w", width=label_width)
length_label.grid(row=2, column=0, padx=10, pady=5)

length_entry = tk.Entry(window)
length_entry.grid(row=2, column=1, padx=10, pady=5)

# Generate Button
generate_button = tk.Button(window, text="GENERATE PASSWORD", command=generate_password_click, bg="blue", fg="white", font=("Arial", 12, "bold"))
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Generated Password
generated_password_label = tk.Label(window, text="Generated Password:", anchor="w", width=label_width)
generated_password_label.grid(row=4, column=0, padx=10, pady=5)

generated_password_entry = tk.Entry(window)
generated_password_entry.grid(row=4, column=1, padx=10, pady=5)

# Accept Button
accept_button = tk.Button(window, text="Accept", command=accept_click, bg="blue", fg="white", font=("Arial", 12, "bold"))
accept_button.grid(row=5, column=0, padx=10, pady=10)

# Reset Button
reset_button = tk.Button(window, text="Reset", command=reset_click, bg="blue", fg="white", font=("Arial", 12, "bold"))
reset_button.grid(row=5, column=1, padx=10, pady=10)

# Lock the screen from expanding
window.resizable(width=False, height=False)

window.mainloop()
