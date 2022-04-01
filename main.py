# Podomoro timer
from tkinter import *
from math import floor

# CONSTANTS
PINK = "#F94892"
RED = "#E7305b"
GREEN = "#9BDE9c"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables
reps = 0
checks = ""
timer = None


# TIMER RESET
def reset_timer():
    global reps
    global timer
    window.after_cancel(str(timer))
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0


# TIMER MECHANISM
def start_timer():
    global reps
    global checks
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    if reps > 8:
        reps = 1
        checks = ""


# COUNTDOWN MECHANISM
def count_down(count):
    global reps
    global checks
    count_min = floor(count / 60)
    count_sec = (count % 60)
    # use of dynamic typing
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += "✓"
            check_marks.config(text=checks)


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36, "bold"))
start_button = Button(text="Start", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                      command=start_timer)
reset_button = Button(text="Reset", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                      command=reset_timer)

check_marks = Label(bg=YELLOW, fg=GREEN, highlightthickness=0)

timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_marks.grid(column=1, row=3)

window.mainloop()
