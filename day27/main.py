import tkinter

window = tkinter.Tk()
window.title("My App")
window.minsize(640, 640)

my_label = tkinter.Label(text="I am a label", font=("Arial",24))
my_label.pack(side = "left")



window.mainloop()