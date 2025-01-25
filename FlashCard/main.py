from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flasher")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="e:/pycharm/Projects/FlashCard/images/card_front.png")
canvas.create_image(400,270, image=card_front)
canvas.grid(column=0, row=0,columnspan=2)

#Canvas Text
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

#Canvas Buttons
right_image = PhotoImage(file="e:/pycharm/Projects/FlashCard/images/right.png")
right_btn = Button(image=right_image, highlightthickness=0)
right_btn.grid(column=1, row=1)

wrong_image = PhotoImage(file="e:/pycharm/Projects/FlashCard/images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0)
wrong_btn.grid(column=0, row=1)


window.mainloop()