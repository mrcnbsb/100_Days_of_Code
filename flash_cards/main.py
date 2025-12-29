import tkinter as tk

import pandas
from random import choice

current_card = None
to_learn = {}
# ---------- CONSTANTS ----------
BACKGROUND_COLOR = "#B1DDC6"

# ---------- CREATE NEW FLASH CARDS ----------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global  current_card, flit_timer
    window.after_cancel(flit_timer)
    canvas.itemconfig(card_background, image=card_front_img)
    current_card = choice(to_learn) # {'English': 'you', 'Português': 'você'}
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card['English'], fill="black")
    #canvas.itemconfig(card_phrase, text=f"'{current_card}['phrase']'", fill="black")
    flit_timer = window.after(3000, func=flip_card)

# ---------- CREATE TRANSLATE ----------
def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="Português", fill="white")
    canvas.itemconfig(card_word, text=current_card['Português'], fill="white")
    #canvas.itemconfig(card_phrase, text=f"'{current_card}['translate']'", fill="white")

# ---------- SAVE THE PROGRESS ----------
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------- USER INTERFACE (UI) ----------
# janela principal
window = tk.Tk()
window.title("English Flash Cards")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR, highlightthickness=0)

flit_timer = window.after(3000, func=flip_card)

# Canvas (logo)
canvas = tk.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
#card_phrase = canvas.create_text(400, 376, text="'This is a phrase.'", font=("Courier", 40))
canvas.grid(column=0, row=0, columnspan=2, pady=10)

# buttons
unknown_img = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=unknown_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_img = tk.PhotoImage(file="images/right.png")
check_button = tk.Button(image=check_img, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)

next_card()



# always in the end
window.mainloop()