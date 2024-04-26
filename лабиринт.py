from tkinter import *
from tkinter import Canvas
from random import *
root = Tk()
q = 10
N  = 100
M  = 50
c = Canvas(root,width=q*N,height=q*M,bg="white")
c.pack()
visited = [0] * N
for i in range (N):
    visited[i] = [0]*M
vert_w = [0] * (N+1)
for i in range (N+1):
    vert_w[i] = [0]*M
hor_w = [0]*N
for i in range (N):
    hor_w[i] = [0]*(M+1)


vert_w[0][0]=1
vert_w[N][M-1]=1

path_x = [0]
path_y = [0]
n_visited = 0
while n_visited < N*M or len(path_x)==0:
    x = path_x[-1]
    y = path_y[-1]
    if visited[x][y] == 0:
        n_visited += 1
        visited[x][y] = 1
    next_x = []
    next_y = []
    if x != 0 and visited[x-1][y] != 1:
        next_x.append(x-1)
        next_y.append(y)
    if x != N-1 and visited[x+1][y] != 1:
        next_x.append(x+1)
        next_y.append(y)
    if y != 0 and visited[x][y-1] != 1 :
        next_x.append(x)
        next_y.append(y-1)
    if y != M-1 and visited[x][y+1] != 1 :
        next_x.append(x)
        next_y.append(y+1)
    if len(next_x) > 0:
        way = randint(0,len(next_x)-1)
        path_x.append(next_x[way])
        path_y.append(next_y[way])
        if next_y[way] != y :#UP-DOWN
            if  next_y[way] == y+1: #DOWN
                hor_w[x][y+1] = 1
            else: #UP
                hor_w[x][y] = 1
        else: #LEFT-RIGHT
            if  next_x[way] == x+1: #RIGHT
                vert_w[x+1][y] = 1
            else: #LEFT
                vert_w[x][y] = 1
    else:
        path_x.pop()
        path_y.pop()

# visited = [0] * N
# for i in range(N):
#     visited[i] = [0] * M
# path = []
# path.append([0, 0])

# while path[-1] != [N-1, M-1]:
#     x, y = path[-1]
#     next_y = []
#     next_x = []
#     if vert_w[x][y] == 1:
#         next_x.append(x-1)
#         next_y.append(y)
#     if vert_w[x+1][y] == 1:

for i in range (N+1):
    for t in range (M):
        if vert_w[i][t] == 0:
            c.create_line(i*q,t*q,i*q,(t+1)*q,width=3)
for i in range (N):
    for t in range (M):
        if hor_w[i][t] == 0:
            c.create_line(i*q,t*q,(i+1)*q,t*q,width=3)
            

mainloop()
