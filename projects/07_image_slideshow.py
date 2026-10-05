# Requirements -> python and code editor and PIL python library(for image loading, precising and manipulating)
# Tkinter -> which is graphical user interface library which helps in creating labels, buttons.
# some iter tools [use a cycle() function which allow iterate in infinite loop] and time module() in which we use sleep() function for stopping program just 1-2 seconds.

import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk
import time
import os

# now we create a root window in which we show the slide show.
root = tk.Tk()
# use root object title method ans pass title as string
root.title("Image Slide Show Viewer")

# Now we tell the file path(list of image path)  Here "r" means raw string.
image_paths = [
    r"C:\Users\Anuj Mishra\Downloads\WhatsApp Image 2026-10-05 at 4.44.56 PM.jpeg",
    r"C:\Users\Anuj Mishra\Downloads\WhatsApp Image 2026-10-05 at 4.44.57 PM.jpeg",
    r"C:\Users\Anuj Mishra\Downloads\WhatsApp Image 2026-10-05 at 4.44.58 PM.jpeg"
]

# now resize images -> use open() method of image class in pil module
image_size =(1080,1080)
images=[Image.open(path). resize(image_size) for path in image_paths]

# use photo image method of image class in pil module which gives the photo image object
photo_images = [ImageTk.PhotoImage(image) for image in images]
# Pack labels into root window
label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

# for repeating the slide show, we use cycle() function from itertools.

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

# Now create a button add it to the root window which will start the slide show when clicked.
play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()