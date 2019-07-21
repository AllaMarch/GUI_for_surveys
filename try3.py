from tkinter import *





window = Tk()

window.geometry('350x200')
window.title("Welcome to the survey app")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)


btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)



window.mainloop()
