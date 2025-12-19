import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_numbers + password_symbols

    # password_list.extend(password_letters)
    # password_list.extend(password_numbers)
    # password_list.extend(password_symbols)

    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        # showinfo
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:  \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?") # True or False

        if is_ok:
            with open("data.txt", "a", encoding="utf-8") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            website_entry.focus()
        else:
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
padlock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=padlock_img)
canvas.grid(column=1, row=0)

# labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

# entries
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "marconebsb@gmail.com")

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)

# buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)



# always in the end
window.mainloop()