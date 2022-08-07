import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def starting():
    global reps, WORK_MIN

    reps += 1
    work_in_sec = WORK_MIN * 60
    short_break_in_sec = SHORT_BREAK_MIN * 60
    long_break_in_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_in_sec)
        title.config(text="Break", fg="red")

    elif reps % 2 == 0:
        count_down(short_break_in_sec)
        title.config(text="Break", fg="red")
    else:
        count_down(work_in_sec)
        title.config(text="Work", fg="red")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_in_min = math.floor(count / 60)
    count_in_sec = count % 60
    if count_in_sec == 0:
        count_in_sec = "00"
    elif count_in_sec < 10:
        count_in_sec = f"{count_in_sec:02}"
    canvas.itemconfig(timer_text, text=f"{count_in_min}:{count_in_sec}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        starting()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(0, work_session):
            marks += "✔"
            tick.config(text=marks, fg="green")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# setting up a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 134, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# setting up the buttons

title = Label(text="Timer", bg=YELLOW, fg="green", font=(FONT_NAME, 45, "bold"))
title.grid(column=1, row=0)

tick = Label(text="", bg=YELLOW, fg="green", font=(FONT_NAME, 45, "bold"))
tick.grid(column=1, row=5)

# buttons


start = Button(text="Start", command=starting, highlightthickness=0)
start.grid(column=0, row=3)


reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=3)

######## to loop the window ######
window.mainloop()
