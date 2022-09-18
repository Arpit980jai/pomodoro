import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    new_window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    # timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    label.config(text="Timer")
    check_mark.config(text="")
    global Reps
    Reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global Reps
    Reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if Reps == 8:
        count_down(long_break_sec)
        label.config(text="Break",font=(FONT_NAME, 45,"bold"),fg=RED,bg=YELLOW)
    elif Reps % 2==0:
        count_down(short_break_sec)
        label.config(text="Break", font=(FONT_NAME, 45, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        label.config(text="Work", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count / 60)
    count_sec=count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global  timer
        timer= new_window.after(1000,count_down,count-1)
    else:
        start_timer()
        check=math.floor(Reps/2)
        mark=""
        for _ in range(check):
            mark+="✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

new_window = Tk()
new_window.title("Pomodoro")
new_window.config(padx=100,pady=100,bg=YELLOW)

label=Label()
label.config(text="Timer",font=(FONT_NAME, 45,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)


canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



button_start=Button()
button_start.config(text="Start",command=start_timer)
button_start.grid(column=0,row=2)

button_end=Button()
button_end.config(text="Reset",command=reset_timer)
button_end.grid(column=2,row=2)


check_mark=Label(text="",fg=GREEN,font=(FONT_NAME,20,"bold"),bg=YELLOW)
check_mark.grid(column=1,row=2)






new_window.mainloop()


