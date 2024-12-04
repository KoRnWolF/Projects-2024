from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#c62e2e"
GREEN = "#347928"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = "none"
timer_running = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global timer_running
    timer_running = False
    window.after_cancel(timer)
    canvas.itemconfig(counter_text, text=f"00:00")
    header_label.config(text="TIMER", fg = GREEN, bg= YELLOW, font=(FONT_NAME, 35, "bold"))
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if not timer_running: #check if timer is running
        if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            header_label.config(text="WORK SLAVE")
            final_countdown(work_sec)
        if reps == 8:
            header_label.config(text="LONG BREAK", fg=PINK)
            window.attributes("-topmost", True)
            window.attributes("-topmost", False)
            final_countdown(long_break_sec)
        if reps == 2 or reps == 4 or reps == 6:
            header_label.config(text="SHORT BREAK", fg=RED)
            window.attributes("-topmost", True)
            window.attributes("-topmost", False)
            final_countdown(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def final_countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.delete("counter")
    canvas.itemconfig(counter_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        global timer_running
        timer_running = True
        timer = window.after(1000, final_countdown, count - 1)
    if count == 0:
        timer_running = False
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✅︎"
        check_label.config(text=mark)

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

check_label = Label(bg = YELLOW, fg = GREEN)
check_label.grid(column = 1, row = 3)

window.mainloop()