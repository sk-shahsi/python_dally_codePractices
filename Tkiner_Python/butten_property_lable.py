import tkinter as tk
import tkinter.font as tkFont
window = tk.Tk()
window.title("My Application")
window.minsize(width=400, height=300)
custom_font = tkFont.Font(family="Courier New", size=20, weight="bold")

label = tk.Label(text="Hello world!", font=custom_font)
label.pack()

label["text"] = "Have a nice day!"
label.config(text="My new app")
counter=0
def function_button():
    global counter
    counter += 1
    label.config(text=f"The button got clicked {counter} time!!")
#label.config(text="The button got clicked!")

#BUtton
button  = tk.Button( text="Click Me", command=function_button)
button.pack()

window.mainloop()



