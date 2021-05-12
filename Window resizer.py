from tkinter import *

root = Tk()
root.geometry("400x200")

# properties function
def resizer() :
     width  = width_value.get()
     height = height_value.get()
     root.geometry(f"{width}x{height}")

root.title("Window Resizer by Omkar Gharat" )
Label(text = "Window Resizer " , font = "comicsansms 11 bold ", fg = "red", pady = 20).grid(column = 2)

# Labels and grid

Label(root , text = "Width : ",font = "comicsansms 11" ).grid(row = 1 , column = 1)
Label(root , text = "Height : ",font = "comicsansms 11" ).grid(row = 2 , column = 1)

# Input values
width_value = StringVar()
height_value = StringVar()

# Entry values
width_entry = Entry(root , textvariable = width_value).grid(row = 1 , column = 2)
height_entry = Entry(root , textvariable = height_value).grid(row =2, column = 2)

# Button
Button(text = "APPLY" , command = resizer , pady = 2 , font = "comicsans 11 bold").grid(column = 2)

# final line
root.mainloop()
