import tkinter as tk

from Tkiner_Python.butten_property_lable import window

label = tk.Label(text="Hello World")
label.pack()
window.mainloop()

label=tk.Label(text="Hello World")
label.pack()
window.mainloop()
def function_button():
   input_text = user_entery.get()

   label.config(text=input_text)
#Taking user input Entery!!
user_entery=tk.Entry(width=20)
user_entery.pack()
user_entery.get()


#Button
button = tk.Button(text="click",command=function_button)
button.pack()



window.mainloop()


