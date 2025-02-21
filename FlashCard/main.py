from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flasher")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

def pull_word():
    random_num = random.randint(0,len(df_list))
    # english_word = (df_list[2]['English'])
    canvas.itemconfig(title, text="French")
    french_word = (df_list[random_num]['French'])
    canvas.itemconfig(word, text=french_word)

df = pandas.read_csv("data/french_words.csv")
df_list = df.to_dict('records')
first_random_num = random.randint(0, len(df_list))
first_french_word = (df_list[first_random_num]['French'])

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,270, image=card_front)
canvas.grid(column=0, row=0,columnspan=2)

#Canvas Text
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=first_french_word, font=("Ariel", 60, "bold"))

#Canvas Buttons
right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command = pull_word)
right_btn.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command = pull_word)
wrong_btn.grid(column=0, row=1)


window.mainloop()