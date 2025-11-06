import tkinter as tk
import tkinter.font as tfont
from tkinter import ttk

#TK
window  = tk.Tk()
window.title("TKinter Python")
window.minsize(width=400,height=300)

coustom_font = tfont.Font(family="Time New Roman",size=20,weight="bold")

label = ttk.Label(text="Hello World",font=coustom_font)

label.pack()

#label.config(Font=("Courier New",25))
label["text"] ="Have a nice day!"

label.config(text="My new app")

def function_button():
    input_text = user_input.get()
    label.config(text=input_text)

#Taking user input using Entery
user_input = ttk.Entry(width=30)
user_input.pack()

#Button
button = ttk.Button(text="Click Me", command=function_button)
button.pack()

quit_button = ttk.Button(text="Quit", command=window.destroy)
quit_button.pack()

window.mainloop()