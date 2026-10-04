# Build a GUI based Digital clock
import tkinter as tk
from time import strftime   # Gives current date and time using time module and date module but using strftime we choose date and time according to our choice.

# now create a root window using tkinter module in which we display our elements.
root = tk.Tk()
root.title("Digital Clock")

# Label element --> show text or images
def time():
    string = strftime("%H:%M:%S  %p \n %D")
    label.config(text=string)
    label.after(1000,time)   # by using this we can update our current date and time.

# Now we create a label object and place on the root window.

label = tk.Label(root, font=('calibri',50, 'bold'), background='yellow', foreground='black')
# using pack method we can arrange the elements in window.
label.pack(anchor='center')
time()
# mainloop() method --> it is a method of tkinter module which place the window on a loop.

root.mainloop()
