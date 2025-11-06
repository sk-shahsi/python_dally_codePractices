import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("My application")

lable = tk.Label(window, text="Hello World",bg="red",fg="white")
lable.pack()
window.mainloop()
lable.pack()

lable2= tk.Label(text="How are you??",bg="red")
lable2.pack()

lable2.pack()

Lable3 = tk.Label(text="Have a nice day!!!")
Lable3.pack()
window.mainloop()