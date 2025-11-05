import tkinter as tk


window = tk.Tk()
window.title("My Application")
window.minsize(width=400, height=300)


label = tk.Label(window, text="Hello World!")
label.pack(side="bottom")

label.config(font=("Courier New",25,"underline"))


window.mainloop()