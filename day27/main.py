import tkinter

window = tkinter.Tk()
window.title("My App")
window.minsize(500, 300)
window.config(padx=20, pady=20)

def clicked_button():
    my_label.config(text=user_input.get())

def button2():
    print("button2 pressed")

my_label = tkinter.Label(text="I am a label", font=("Arial",24))
my_label.config(text="New Text")
my_label.grid(column = 0, row = 0)

button = tkinter.Button(text="Click Me", command = clicked_button)
button.grid(column = 1, row = 1)
button2 = tkinter.Button(text="Button2", command = button2)
button2.grid(column = 2, row = 0)

user_input = tkinter.Entry(width=40)
user_input.grid(column = 3, row = 2)




window.mainloop()