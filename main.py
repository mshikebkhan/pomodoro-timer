from tkinter import *
import math

# ---- CONSTANTS ----  #
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---- TIME RESET ----  #
def reset_timer():
    window.after_cancel(timer)
    heading.config(text="Work")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global reps
    reps = 0
    start_button.config(state="normal")  # ✅ Re-enable Start Button on Reset

# ---- TIMER MECHANISM ----  #
def start_timer():
    global reps
    reps += 1
    start_button.config(state="disabled")  # ✅ Disable Start Button when clicked

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        heading.config(text="Big Break!!")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        heading.config(text="Break!")
        count_down(short_break_sec)
    else:
        heading.config(text="Work")
        count_down(work_sec)

# ---- COUNTDOWN MECHANISM ---- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check.config(text=mark)

# ---- UI SETUP ----  #
window = Tk()
window.iconbitmap("tomato.ico")
window.title("Pomodoro Timer")
window.config(padx=70, pady=20, bg=YELLOW)

heading = Label(text="Work", font=(FONT_NAME, 28, "bold"), background=YELLOW)
heading.pack()

canvas = Canvas(width=200, height=180, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 90, image=tomato_img)
timer_text = canvas.create_text(100, 105, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.pack()

check = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check.pack(side="bottom")

reset_button = Button(text="Reset", command=reset_timer)
reset_button.pack(side="left")

start_button = Button(text="Start", command=start_timer)
start_button.pack(side="right")

window.mainloop()
