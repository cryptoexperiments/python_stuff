from tkinter import *
from random import randint

root = Tk()

# root.resizable(width=False, height=False)
root.minsize(width=1024, height=600)
root.maxsize(width=1024, height=600)
# root.attributes("-fullscreen", True)  # window full screen

frame = Frame(root)
labelText = StringVar()
label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me", height=10, width=20, font="Arial 20", foreground="blue", background="black")
label.pack()
button.pack()
frame.pack()


def clock():
    labelText.set(randint(0, 90))
    # time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    # lab.config(text=time)
    # lab['text'] = time
    root.after(100, clock)  # run itself again after 1000 ms


clock()
root.mainloop()
