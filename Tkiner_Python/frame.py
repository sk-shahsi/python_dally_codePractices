import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("My application")

my_frame = ttk.Frame()
my_frame.pack(side="left",fill="both",expand=True)

lable1 = tk.Label(my_frame, text="Hello World",bg="black",fg="white")
lable1.pack(side="left",fill="both",expand=True)




lable2= tk.Label(text="How are you??",bg="red")
lable2.pack(side="top",fill="both",expand=True)



Lable3 = tk.Label(text="Have a nice day!!!",bg="pink")
Lable3.pack(side="top",fill="both",expand=True)


window.mainloop()