BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import json
import pandas
import random
import time

####################### cards ######################
french_data_dic = {}
try:
    french_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    fresh_french_data = pandas.read_csv("./data/french_words.csv")
    french_data_dic = fresh_french_data.to_dict(orient="records")
else:
    french_data_dic = french_data.to_dict(orient="records")


# print(french_data_dic)
current_card = {}


def flash_french_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_data_dic)
    french_word = current_card["French"]
    word_label.config(text=french_word)
    title_label.config(text="French")
    flip_timer = window.after(3000, func=flip_card)


def tick_card():
    global current_card, french_data_list
    known_french_word = current_card
    french_data_dic.remove(known_french_word)
    flash_french_card()
    words_remaining = pandas.DataFrame(french_data_dic)
    words_remaining.to_csv("data/words_to_learn", index=False)



def flip_card():
    global current_card
    title_label.config(text="English", bg=BACKGROUND_COLOR)
    english_word = current_card["English"]
    word_label.config(text=english_word, bg=BACKGROUND_COLOR)
    canvas.create_image(400, 400, image=back_card)


############################ UI #############################################
###### Creating exterior window
window = Tk()
window.config(width=1200, height=1000, bg=BACKGROUND_COLOR)
window.title("Flashy")
window.config(padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

## Creating window canvas

canvas = Canvas(width=800, height=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 400, image=card)
canvas.grid(column=0, row=1, columnspan=5, rowspan=8)

# adding labels

title_label = Label(text="", bg="white", font=("Ariel", 25, "italic"))
title_label.grid(column=2, row=3)

word_label = Label(text="", bg="white", font=("Ariel", 50, "bold"))
word_label.grid(column=2, row=4)

# add buttons


wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=flash_french_card)
wrong_button.grid(column=1, row=9)

flash_french_card()

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=tick_card )
right_button.grid(column=3, row=9)

print(french_data_dic)
####### main loop
window.mainloop()
