import tkinter as tk
import tkinter.font as tfont
from tkinter import ttk

#TK
window  = tk.Tk()
window.title("TKinter Python")
window.minsize(width=400,height=300)

coustom_font = tfont.Font(family="Time New Roman",size=20,weight="bold")

label = ttk.Label(text="Hello World",font=coustom_font,padding=15)

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
quit_button.pack(pady=10)

sep = ttk.Separator(window, orient="horizontal")
sep.pack(fill="x")

text = tk.Text(height=5, width=30)
text.focus() # for cursor
text.pack(pady=10)
text.insert("1.0","Enter your comment") #defult text

text_data=text.get("1.0","end")
print(text_data)

def text_function():
    text_data = text.get("1.0","end")
    print(text_data)






# text["state"]="disabled"
# def enabled_text():
#     text["state"]="normal"
# enabled_button = ttk.Button(text="Enable", command=enabled_text)
# enabled_button.pack()
#2# check_option = tk.IntVar()
# def check_option():
#     print(check_option.get())
# check_button = ttk.Checkbutton(text="Agree with term & Condition",
#                                variable=check_option,command=check_option)
# check_button.pack()

#RadioButton
def get_radio_value():
    print(radio_value.get())

radio_value = tk.StringVar()
option_1 = ttk.Radiobutton(window, text="Male", variable=radio_value, value="Option 1")
option_2 = ttk.Radiobutton(window, text="Female", variable=radio_value, value="Option 2")
option_1.pack(fill="x")
option_2.pack(fill="x")

#combobox

select_countery = tk.StringVar()
countries = ttk.Combobox(window, textvariable=select_countery,values=("india","japan"))
countries["state"] = "readonly"
countries.pack()

def display_countery():
    print(select_countery.get())
countries.bind("<<ComboboxSelected>>", display_countery)


#Listbox
food_item = ("pizza","Burger","Garlc Breade","Nachos")
fav_food = tk.StringVar(value=food_item)
food_list=tk.Listbox(listvariable=fav_food,height=5,selectmode="extended")
food_list.pack()

def get_favfood():
    print(fav_food.get())

food_list.bind("<<ListboxSelected>>", get_favfood)

#Spinbox
counter = tk.IntVar(value=10)
spin_box = ttk.Spinbox(window, from_=0, to=20)
spin_box.pack()



window.mainloop()