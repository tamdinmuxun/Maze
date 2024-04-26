from tkinter import *
from tkinter import Canvas
from random import *

seed(1)

root = Tk()

q = 100  # cell si
N = 5  # width (number of cells)
M = 3  # height (number of cells)
c = Canvas(root, width=q * N, height=q * M, bg="white")
c.pack()

#
# generate random maze   
#

visited = [0] * N  # 1 if the cell has already been visited
for i in range(N):
    visited[i] = [0] * M
vert_w = [0] * (N + 1)  # 1 if no vertical wall
for i in range(N + 1):
    vert_w[i] = [0] * M
hor_w = [0] * N  # 1 if no horizontal wall
for i in range(N):
    hor_w[i] = [0] * (M + 1)

vert_w[0][0] = 1
vert_w[N][M - 1] = 1

path_x = [0]  # path (to know where to return)
path_y = [0]
n_visited = 0
while n_visited < N * M or len(path_x) == 0:
    x = path_x[-1]
    y = path_y[-1]
    if visited[x][y] == 0:
        visited[x][y] = 1
        n_visited += 1

    next_x = []  # possible next positions
    next_y = []
    if x != 0 and visited[x - 1][y] != 1:
        next_x.append(x - 1)
        next_y.append(y)
    if x != N - 1 and visited[x + 1][y] != 1:
        next_x.append(x + 1)
        next_y.append(y)
    if y != 0 and visited[x][y - 1] != 1:
        next_x.append(x)
        next_y.append(y - 1)
    if y != M - 1 and visited[x][y + 1] != 1:
        next_x.append(x)
        next_y.append(y + 1)

    if len(next_x) > 0:  # if there is where to go
        way = randint(0, len(next_x) - 1)  # choose random way to go
        path_x.append(next_x[way])
        path_y.append(next_y[way])
        if next_y[way] != y:  # UP-DOWN
            if next_y[way] == y + 1:  # DOWN
                hor_w[x][y + 1] = 1
            else:  # UP
                hor_w[x][y] = 1
        else:  # LEFT-RIGHT
            if next_x[way] == x + 1:  # RIGHT
                vert_w[x + 1][y] = 1
            else:  # LEFT
                vert_w[x][y] = 1
    else:
        path_x.pop()  # remove from path if nowhere to go from here
        path_y.pop()  # (no need to return here)

for i in range(N + 1):
    for t in range(M):
        if vert_w[i][t] == 0:
            c.create_line(i * q, t * q, i * q, (t + 1) * q, width=3)
for i in range(N):
    for t in range(M):
        if hor_w[i][t] == 0:
            c.create_line(i * q, t * q, (i + 1) * q, t * q, width=3)

visited = [0] * N

for i in range(N):
    visited[i] = [0] * M

path = []
path.append([0, 0])

drawpath = []

while path[-1] != [N - 1, M - 1]:
    x, y = path[-1]
    if visited[x][y] == 0:
        visited[x][y] = 1

    next_x = []
    next_y = []

    if vert_w[x][y] == 1 and visited[x - 1][y] != 1 and x != 0 and y != 0:
        next_x.append(x - 1)
        next_y.append(y)
    if vert_w[x + 1][y] == 1 and visited[x + 1][y] != 1:
        next_x.append(x + 1)
        next_y.append(y)
    if hor_w[x][y] == 1 and visited[x][y - 1] != 1:
        next_x.append(x)
        next_y.append(y - 1)
    if hor_w[x][y + 1] == 1 and visited[x][y + 1] != 1:
        next_x.append(x)
        next_y.append(y + 1)

    if len(next_x) != 0:
        way = randint(0, len(next_x) - 1)
        path.append([next_x[way], next_y[way]])
        print(*path)
        if next_y[way] != y:
            if next_y[way] == y + 1:
                drawpath.append('down')
            else:
                drawpath.append('up')
        else:
            if next_x[way] == x + 1:
                drawpath.append('right')
            else:
                drawpath.append('left')

    else:
        path.pop()
        drawpath.pop()
    print(*drawpath)
print(*path)
print(*drawpath)

x = 0
y = 0
for i in range(len(drawpath)):
    if drawpath[i] == "right":
        c.create_line(x * q + q / 2, y * q + q / 2, (x + 1) * q + q / 2, y * q + q / 2, fill="red", width=2)
        x = x + 1
    if drawpath[i] == "left":
        c.create_line(x * q + q / 2, y * q + q / 2, (x - 1) * q + q / 2, y * q + q / 2, fill="red", width=2)
        x = x - 1
    if drawpath[i] == "up":
        c.create_line(x * q + q / 2, y * q + q / 2, x * q + q / 2, (y - 1) * q + q / 2, fill="red", width=2)
        y = y - 1
    if drawpath[i] == "down":
        c.create_line(x * q + q / 2, y * q + q / 2, x * q + q / 2, (y + 1) * q + q / 2, fill="red", width=2)
        y = y + 1

c.create_line(0, q / 2, 1 * q / 2, q / 2, fill="red", width=2)

c.create_line((N - 1) * q + q / 2, (M - 1) * q + q / 2, N * q, (M - 1) * q + q / 2, fill="red", width=2)

# for i in range(N):
#    for j in range(M):
#        if [i,j] in path == True:
#                      


mainloop()
