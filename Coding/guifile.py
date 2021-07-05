import tkinter as tk
from tkinter.constants import END
from typing import Text
# Creating main window
window = tk.Tk()
def click():
    data = e1.get()
    t1.delete("1.0", END)
    t1.insert(END, data)
   


entryInput = tk.StringVar()
e1 = tk.Entry(window, textvariable=entryInput)
e1.grid(row=0, column=0)

# e2 = tk.StringVar()
t1 = tk.Text(window, height=10, width=20)
t1.grid(row=0, column=1)

b1 = tk.Button(window, text='Click', command=click)
b1.grid(row=0, column=2)


# # convert function
# def unit_convert():
#     grams = float(entryInputvalue.get()) * 1000
#     # Tells python to start deleting from start to END
#     t1.delete("1.0", END)
#     t1.insert(END, grams)
#     pounds = float(entryInputvalue.get()) * 2.20462
#     t2.delete("1.0", END)
#     t2.insert(END, pounds)
#     ounces = float(entryInputvalue.get()) * 35.274
#     t3.delete("1.0", END)
#     t3.insert(END, ounces)


# # Adding lables
# lableOne = tk.Label(window, text='Kg:')
# lableOne.grid(row=0, column=0)
# lableTwo = tk.Label(window, text='Pounds:')
# lableTwo.grid(row=1, column=0)
# lableThree = tk.Label(window, text='Grams:')
# lableThree.grid(row=1, column=1)
# lablefour = tk.Label(window, text='Ounces:')
# lablefour.grid(row=1, column=2)

# convertButton = tk.Button(window, text = 'Convert', command=unit_convert)
# convertButton.grid(row = 0, column = 2)

# # Input field
# entryInputvalue = tk.StringVar()
# entryOne = tk.Entry(window, textvariable=entryInputvalue)
# entryOne.grid(row=0, column=1)

# # Output field

# t1=tk.Text(window,height=1, width=20)
# t1.grid(row=2,column=0)
 
# t2=tk.Text(window,height=1,width=20)
# t2.grid(row=2,column=1)
 
# t3=tk.Text(window,height=1,width=20)
# t3.grid(row=2,column=2)

# Executing main window
window.mainloop()

    