import tkinter
import smtplib

def send_email(subject, body):
    sender_email = "mailerautomailer@gmail.com"
    sender_password = "cdlo zsww jkgy adie"
    recipient_email = "henno.steyn@trade-link.co.za"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(sender_email, sender_password)
            email_message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient_email, email_message)
            server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")



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

calculate_button = tkinter.Button(text="Calculate", command = send_email("Hello", "This is working"))
calculate_button.grid(column = 1, row = 2)





window.mainloop()