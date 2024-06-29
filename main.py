"""
---------------------------------------
    * Course: 100 Days of Code - Dra. Angela Yu
    * Author: Noah Louvet
    * Day: 28 - Pomodoro Timer
    * Subject: Tkinter GUI
---------------------------------------
"""

from tkinter import *
import math
from tkinter import simpledialog

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")

    # title_label "Timer"
    title_label.config(text="Timer", fg=GREEN)

    # reset check
    checkmark_label.config(text="")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="LONG BREAK", fg=RED)
    elif reps % 9 == 0:
        button_control()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="RELAX", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = count // 60
    count_sec = ("{:02d}".format(count % 60))

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
        window.attributes('-topmost', 0)
    else:
        # brings window into focus whether in bg or minimized
        window.attributes('-topmost', 1)
        window.state("normal")

        start_timer()
        ticks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            ticks += "✔"
            checkmark_label.config(text=ticks)


# ---------------------------- BUTTON SWITCH ------------------------------- #

def button_control():
    if control_button.cget("text") == "Start":
        start_timer()
        control_button.config(text="Reset")

    elif control_button.cget("text") == "Reset":
        reset_timer()
        control_button.config(text="Start")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.update_idletasks()
WORK_MIN = simpledialog.askinteger(title="Study Time", prompt="How many minutes are the study sessions?", parent=window)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), highlightthickness=0)
title_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), highlightthickness=0)
checkmark_text = checkmark_label.config(text="")
checkmark_label.grid(column=1, row=3)

control_button = Button(text="Start", command=button_control)
control_button.grid(column=1, row=1, pady=(0, 20), sticky="s")
control_button.config(padx=10, pady=5)

window.mainloop()
