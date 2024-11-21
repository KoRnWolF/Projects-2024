from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#c62e2e"
GREEN = "#347928"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    final_countdown(WORK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def final_countdown(workmin):
    mins, secs = divmod(workmin, 5)
    canvas.delete("counter")
    canvas.itemconfig(counter_text, text=workmin)
    if workmin > 0:
        window.after(1000, final_countdown, workmin - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pommy App")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column = 1, row = 1)
counter_text = canvas.create_text(100,130, text="00:00", fill = "white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="START", bg="green", fg="white" , command=start_timer)
start_button.grid(column = 0, row = 2)


reset_button = Button(text="RESET", bg="green", fg="white", command=reset_timer)
reset_button.grid(column = 2, row = 2)

header_label = Label(text="TIMER", fg = GREEN, bg= YELLOW, font=(FONT_NAME, 35, "bold"))
header_label.grid(column = 1, row = 0)

check_label = Label(text="✅︎",bg = YELLOW, fg = GREEN)
check_label.grid(column = 1, row = 3)

window.mainloop()