from tkinter import *

def create_window():
    """
    create a window, set the title, set the size, and set the padding
    """
    window.title("Miles to Kilometer Converter")  # set the title of the window
    window.minsize(width=200, height=100)  # set the minimum size of the window
    window.config(padx=20, pady=20)  # set the padding of the window
def create_labels():
    """
    create the labels, set the text, and place them on the screen
    """
    miles_label = Label(text="Miles") # create a label
    miles_label.grid(column=3, row=0) # place the label on the screen

    is_equal_to_label = Label(text="is equal to") # create a label
    is_equal_to_label.grid(column=0, row=1) # place the label on the screen

    zero_label.grid(column=1, row=1) # place the label on the screen

    km_label = Label(text="Km") # create a label
    km_label.grid(column=3, row=1) # place the label on the screen
def btn_clicked():
    """
    convert miles to km
    """
    mile = float(input.get())
    km = mile * 1.60934
    zero_label.config(text=round(km))
def create_btn():
    """
    create a button, set the text, and place it on the screen
    """
    button = Button(text="Calculate", command=btn_clicked) # create a button
    button.grid(column=1, row=3) # place the button on the screen
def create_textbox():
    """
    create a text box, set the text, and place it on the screen
    """
    input.insert(0, "0")
    input.grid(column=1, row=0)

window = Tk() # create a window equivalent to Screen() in turtle
zero_label = Label(text="0") # create a label
input = Entry(width=7) # create a text box
create_window() # call the function to create the window
create_labels() # call the function to create the labels
create_btn() # call the function to create the button
create_textbox() # call the function to create the text box
window.mainloop() # continuously run the program