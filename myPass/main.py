from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.delete(0, END)#Clears password if generate is clicked again
    pass_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }
    #Check if any entries are empty
    if len(website) == 0 or len(password) == 0:
        empty_error = messagebox.showerror(title = "Empty Fields Error", message="Please do not leave any fields empty!")

    else:

        confirm_save = messagebox.askyesno(title= "Save Profile", message = f"Website : {website}\n"
                                                                            f"Email : {email}\n"
                                                                            f"Password : {password}")
        if confirm_save:
            with open("password_file.json", "r") as pass_file:
                #Read old data - from json to python dict
                data = json.load(pass_file)
                #Update old data with new data - normal python dict
                data.update(new_data)

            with open("password_file.json", "w") as pass_file:
                json.dump(data, pass_file, indent=4)

                pass_file.close()
                pyperclip.copy(password)#Copy password to clipboard

            web_entry.delete(0, END)
            pass_entry.delete(0, END)
            web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("myP4ss")
window.config(padx=50, pady=50)
#Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column = 1, row = 0)
#Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
#Entries
web_entry = Entry(width=35)
web_entry.grid(column = 1, row = 1, columnspan = 2)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(0, "@gmail.com")
pass_entry = Entry(width=22)
pass_entry.grid(column = 1, row = 3)
#Buttons
gen_pass = Button(text="Generate Password", command=gen_password)
gen_pass.grid(column = 1, row = 4)
add_profile = Button(text="Add", width = 10, command=save_password)
add_profile.grid(column = 1, row = 5)



window.mainloop()