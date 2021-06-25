import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    pass_entry.delete(0, tk.END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    char_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char1 in range(nr_symbols)]
    number_list = [random.choice(numbers) for char2 in range(nr_numbers)]
    password_list = char_list + symbol_list + number_list

    random.shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(tk.END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        try:
            with open('password.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open('password.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('password.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        website_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

# ---------------------------- SEARCH WEBSITE ------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open('password.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="There is no data file!")
    else:
        if website in data:
            password = data[website_entry.get()]["password"]
            messagebox.showinfo(title="Info", message=f"Password for {website} is: {password}")
        else:
            messagebox.showerror(title="Error", message=f"There is no data for {website}.")
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Maker")
window.config(padx=30, pady=30)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = tk.Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()
website_button = tk.Button(text="Search", width=15, command=search)
website_button.grid(column=2,row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = tk.Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(tk.END, "mateuszstrzelecki21@gmail.com")

pass_label = tk.Label(text="Password")
pass_label.grid(column=0, row=3)
pass_entry = tk.Entry(width=33)
pass_entry.grid(column=1, row=3)
pass_button = tk.Button(text="Generate Password", command=generate_pass)
pass_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
