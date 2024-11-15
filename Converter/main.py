import tkinter

window = tkinter.Tk()
window.title("Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def calculate():
    if variable.get() == "Miles":
        new_text = float(user_input.get())*1.609
        result.config(text = round(new_text, 2))

    if variable.get() == "Lightyear":
        new_text = float(user_input.get())*9.461*pow(10,12)
        result.config(text = round(new_text))

user_input = tkinter.Entry()
user_input.grid(column = 1, row = 0)
user_input.focus()

variable = tkinter.StringVar(window)
variable.set("Miles") # default value
user_list = tkinter.OptionMenu(window, variable, "Miles", "Lightyear")
user_list.grid(column = 2, row = 0)

equal = tkinter.Label(text = "is equal to")
equal.grid(column = 0, row = 1)

km_label = tkinter.Label(text = "Km")
km_label.grid(column = 2, row = 1)

result = tkinter.Label(text="0")
result.grid(column=1, row=1)

calculate_button = tkinter.Button(text="Calculate", command = calculate)
calculate_button.grid(column = 1, row = 2)





window.mainloop()