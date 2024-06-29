from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg="#FFE8C5")

label = Label(text="Timer", fg='green', bg="#FFE8C5", font=("Arial", 16, "bold"))
label.grid(column=2, row=1)

start_button = Button(text="Start")
start_button.grid(column=1, row=3)

stop_button = Button(text="Stop")
stop_button.grid(column=3, row=3)

canvas = Canvas(width=400, height=300, bg="#FFE8C5", highlightthickness=0)
image_url = PhotoImage(file="tomato.png")
canvas.create_image(200, 150, image=image_url)
canvas.create_text(200, 174, text="00:00", fill="white", font=("Ariel", 15, "bold"))
canvas.grid(column=2, row=2)

label2 = Label(text="✔", fg='green', bg="#FFE8C5", font=("Arial", 16, "bold"))
label2.grid(column=2, row=4)

window.mainloop()
