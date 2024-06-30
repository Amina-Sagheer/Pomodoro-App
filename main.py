from tkinter import *

i = 0
TIMER = None

def count_down(count):

    if count >= 0:
        minutes = count // 60
        seconds = count % 60
        final_count = f"{minutes:02}:{seconds:02}"
        canvas.itemconfig(timer, text=final_count)
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)

def reset():
    canvas.itemconfig(timer, text="00:00")
    window.after_cancel(TIMER)


def start_timer():
    def start_work():
        global i
        i += 1
        count_down(25 * 60)  # 25 minutes of work
        window.after(25 * 60 * 1000, start_break)

    def last_session():
        count_down(20 * 60)  # 25 minutes of work

    def start_break():
        count_down(5 * 60)  # 5 minutes of short break
        window.after(5 * 60 * 1000, start_work)

    # Start the first work session
    if i == 4:
        last_session()
    else:
        start_work()


window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg="#FFE8C5")

label = Label(text="Timer", fg='green', bg="#FFE8C5", font=("Arial", 16, "bold"))
label.grid(column=2, row=1)

canvas = Canvas(width=400, height=300, bg="#FFE8C5", highlightthickness=0)
image_url = PhotoImage(file="tomato.png")
canvas.create_image(200, 150, image=image_url)
timer = canvas.create_text(200, 174, text="00:00", fill="white", font=("Ariel", 15, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=3, row=3)

label2 = Label(text="✔", fg='green', bg="#FFE8C5", font=("Arial", 16, "bold"))
label2.grid(column=2, row=4)

window.mainloop()
