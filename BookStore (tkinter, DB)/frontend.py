from tkinter import *
import backend

# Creating main window
window = Tk()
# Adding title to the window
window.wm_title("Book Store Database System")

def get_selected_row(event):
    try:
      global selected_tuple
      index = lb1.curselection()[0]
      selected_tuple = lb1.get(index)
      e1.delete(0,END)
      e1.insert(END, selected_tuple[1])
      e3.delete(0,END)
      e3.insert(END, selected_tuple[3])
      e2.delete(0,END)
      e2.insert(END, selected_tuple[2])
      e4.delete(0,END)
      e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

    


# View button function
def view_book():
    lb1.delete(0, END)
    for row in backend.view_data():
        lb1.insert(END, row)
# Search button function
def search_book():
    lb1.delete(0, END)
    for row in backend.search_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lb1.insert(END,row)
# Add button function
def add_book():
    backend.insert_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lb1.delete(0, END)
    lb1.insert(END, (title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
# Delete button fucntion:
def delete_book():
    backend.delete_data(selected_tuple[0])
# Update button function
def update_book():
    backend.update_data(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
def close_window():
    window.destroy()



# Adding lables
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)
l2 = Label(window, text='Author')
l2.grid(row=1, column=0)
l3 = Label(window, text='Year')
l3.grid(row=0, column=2)
l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

# Adding entryfields
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=1, column=1)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=0, column=3)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


# Adding Buttons
b1 = Button(window, width= 8,text='View all', command=view_book)
b1.grid(row=2, column=3)
b2 = Button(window, width= 8, text='Search', command=search_book)
b2.grid(row=3, column=3)
b3 = Button(window, width= 8, text='Add', command=add_book)
b3.grid(row=4, column=3)
b4 = Button(window, width= 8,text='Update',command=update_book)
b4.grid(row=5, column=3)
b5 = Button(window, width= 8, text='Delete', command=delete_book)
b5.grid(row=6, column=3)
b6 = Button(window, width= 8,text='Close', command=close_window)
b6.grid(row=7, column=3)

# Adding listbox
lb1 = Listbox(window, height=6, width=35)
lb1.grid(row=2, column=0, rowspan=6, columnspan=2)
lb1.bind('<<ListboxSelect>>',get_selected_row)

# Add Scroll bar
sb1 = Scrollbar(window)
sb1.grid(row=2, rowspan=6, column=2)

# Connecting the scroll bar to the listbox
lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

# Executing main window
window.mainloop()
