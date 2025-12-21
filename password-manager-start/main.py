import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    new_data = {website:{
        "email":email,
        "password":password,
    }}

    if website == "" or password == "":
        # showinfo
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:  \nEmail: {email} "
        #                                               f"\nPassword: {password} \nIs it ok to save?") # True or False
        #
        # if is_ok:
        #     with open("data.txt", "a", encoding="utf-8") as file:
        #         file.write(f"{website} | {email} | {password}\n")
        #     website_entry.delete(0, tk.END)
        #     password_entry.delete(0, tk.END)
        #     website_entry.focus()
        # else:
        #     website_entry.focus()
        try:
            with open("data.json", "r", encoding="utf-8") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w", encoding="utf-8") as data_file:
                # saving new data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w", encoding="utf-8") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", encoding="utf-8") as data_file:
            # reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data.keys():
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exists.")
    finally:
        website_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Configuração das colunas
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.columnconfigure(2, weight=1)


# Espaçamento padrão
PADX = 10
PADY = 6

# Canvas (logo)
canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
padlock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=padlock_img)
canvas.image = padlock_img  # evita garbage collector
canvas.grid(column=0, row=0, columnspan=3, pady=(10,20))

# labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e", padx=PADX, pady=PADY)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e", padx=PADX, pady=PADY)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e", padx=PADX, pady=PADY) # sticky"e" -> Alinha os labels à direita, deixando tudo organizado.

# entries
website_entry = tk.Entry(window, width=30)
website_entry.grid(column=1, row=1, padx=PADX, pady=PADY)
website_entry.focus()

email_entry = tk.Entry(window, width=40)
email_entry.grid(column=1, row=2, columnspan=2, padx=PADX, pady=PADY)
email_entry.insert(0, "marconebsb@gmail.com")

password_entry = tk.Entry(window, width=21)
password_entry.grid(column=1, row=3, padx=PADX, pady=PADY)

# buttons
search_button = tk.Button(window, text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, padx=PADX, pady=PADY)

generate_password_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, padx=PADX, pady=PADY)

add_button = tk.Button(window, text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, pady=(15, 0))




# always in the end
window.mainloop()
