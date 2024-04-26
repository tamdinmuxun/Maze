import tkinter


def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
        canvas.itemconfig(oval, fill='green')
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    if event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    if event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    for i in range(4):
        if abs(canvas.coords(oval)[i] - 310 - 10*2**0.5) > 100:
            canvas.itemconfig(oval, fill='red')

        
# Допишите сюда необходимый текст


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()