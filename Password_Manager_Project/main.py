import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password2.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def file():
    website1 = website.get()
    email1 = email.get()
    password1 = password2.get()

    if len(website1) == 0 or len(email1) == 0 or len(password1) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you don't have any fields empty.")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email1} "

                                                              f"Password: {password1} \nIs it ok to save?")
        if is_ok:
            with open("file2.txt", "a") as f:
                f.write(f"{website1}|{email1}|{password1}\n")
                website.delete(0, tk.END)
                password2.delete(0, tk.END)

        # messagebox.showinfo(title="Title", message="Message")


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
# window.config(width=200, height=200)
window.title("Password Manager")
window.config(padx=50, pady=50)

img = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
# Labels
Label_Website = tk.Label(text="Website:")
Label_Website.grid(column=0, row=1)

Label_Email = tk.Label(text="Email/Username:")
Label_Email.grid(column=0, row=2)

Label_Password = tk.Label(text="Password:")
Label_Password.grid(column=0, row=3)

# Entry
website = tk.Entry(width=35)
website.grid(row=1, column=1, columnspan=2)
website.focus()
email = tk.Entry(width=35)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, "gm@gmail.com")
password2 = tk.Entry(width=21)
password2.grid(row=3, column=1)

# Button

Button_generate = tk.Button(text="Generate Password", command=password_generator)
Button_generate.grid(row=3, column=2)

Button_Add = tk.Button(text="Add", width=36, command=file)
Button_Add.grid(row=4, column=1, columnspan=2)

window.mainloop()
