import tkinter as tk

#Creating a new window and configurations
window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20) # distância da borda

# Labels
my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold")) #normal, bold, italic (facultativo)
# my_label["text"] = "This is New Text"
my_label.config(text="Next Text")
# my_label.pack() #side="left", right, botton
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(pady=50, padx=50)

# Buttons
def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    my_label["text"] = new_text
#calls button_clicked when pressed
button = tk.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

#calls button_clicked when pressed
new_button = tk.Button(text="Click Me", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)

# Entries
entry = tk.Entry(width=30)
#Add some text to begin with
# entry.insert(tk.END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
# entry.pack()
entry.grid(column=3,row=3)


# # Text
# text = tk.Text(height=5, width=30)
# #Puts cursor in textbox
# text.focus()
# #Adds some text to begin with
# text.insert(tk.END, "Example of multi-line text entry.")
# #Gets current value in textbox at line1, character 0
# print(text.get("1.0", tk.END))
# text.pack()
#
#
# # Spinbox
# def spinbox_used():
#     #gets the current value in spinbox
#     print(spinbox.get())
# spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # Scale
# def scale_used(value):
#     print(value)
# scale = tk.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# checked_state = tk.IntVar()
# checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
# radio_state = tk.IntVar()
# radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton3 = tk.Radiobutton(text="Option3", value=3, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
# radiobutton3.pack()
#
# # Listbox
# def listbox_used(event):
#     #Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
# listbox = tk.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(tk.END, item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# sempre no final
window.mainloop()