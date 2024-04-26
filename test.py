from tkinter import *


def key_pressed(event):
    global w, h, oval
    if event.keysym == 'Up':
        c.move(oval, 0, -10)
    if event.keysym == 'Down':
        c.move(oval, 0, 10)
    if event.keysym == 'Right':
        c.move(oval, 10, 0)
    if event.keysym == 'Left':
        c.move(oval, -10, 0)
    for i in range(4):
        if i % 2 == 0 and abs(canvas.coords(oval)[i]) >= w:
            move_wrap(c, oval, [0, -canvas.coords(oval)[i]])
        elif i % 2 != 0 and abs(canvas.coords(oval)[i]) >= h:
            move_wrap(c, oval, [-canvas.coords(oval)[i], 0])

def move_wrap(c, obj, move):
    c.move(obj, move[0], move[1])
    
            
master = Tk()
w = 600
h = 600
c = Canvas(master, width=w, height=h)
c.pack()
oval = c.create_oval(300, 300, 310, 310, fill='orange')

c.bind("<KeyPress>", key_pressed)
c.mainloop()