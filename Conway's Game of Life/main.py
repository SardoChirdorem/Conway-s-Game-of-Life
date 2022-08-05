"""
This is an implementation of Conway's Game of Life with python and tkinter. The game of life was first invented by
Cambridge mathematician John Horton Conway in the 1970s.

It is a two-dimensional cellular automaton. The environment is a grid with vertical and horizontal axes. The grid
usually extends to infinity, but I have implemented it in a bounded space.

The rules of the game are as follows:

> Each cell in the grid has two states: alive or dead. These are denoted by different colours.
> Each cell has eight neighbours, corresponding to the eight directions north, south, east, west, north-west,
north-east, south-west, south-east.
> Given an initial configuration of alive and dead cells, any alive cell will survive to the next generation only if
it has two or three alive neighbours.
> Any alive cell that has four or more than four alive neighbours will die in the next generation. Alternately, any
alive cell with less than two neighbours will also die.
> Any dead cell that has exactly three neighbours will come to life in the next generation.

This simple set of rules has yielded a fascinating model which has been fancied by various mathematicians for many
years. What initial configuration will converge to a stable state and which of them will grow without bounds is an
active area of study.
"""

import tkinter as tk
import random

GRID_SIZE = 650
WINDOW_SIZE = (677, 650)
WINDOW_BG = "#00e7fc"
ALIVE_CELL_BG = "#dffc03"
DEAD_CELL_BG = "#01043b"

def locator(arr,i,k):

    arr[i][k].config(bg = "red")

def counter(arr,i,k):

    a = []
    corset = [
        (i,k+1),
        (i,k-1),
        (i+1,k),
        (i-1,k),
        (i+1,k+1),
        (i-1,k-1),
        (i+1,k-1),
        (i-1,k+1)
    ]
    for h in corset:
        if -1 in h or GRID_SIZE//10 in h:
            a.append(DEAD_CELL_BG)
        else:
            a.append(arr[h[0]][h[1]].cget("bg"))

    return a.count(ALIVE_CELL_BG)

def conway():

    f = []
    for r in range(GRID_SIZE//10):
        t = []
        for y in range(GRID_SIZE//10):
            t.append(counter(BUTTON_ARRAY,r,y))
        f.append(t)



    for m in range(GRID_SIZE//10):
        for p in range(GRID_SIZE//10):
            if f[m][p] == 3:
                BUTTON_ARRAY[m][p].config(bg=ALIVE_CELL_BG)
            elif f[m][p] == 2:
                pass
            elif f[m][p] >= 4 or f[m][p] < 2:
                BUTTON_ARRAY[m][p].config(bg=DEAD_CELL_BG)

def cleaner(st):

    return list(map(int, st.split(",")))

def changeColour(bttn):

    if bttn.cget("bg") == ALIVE_CELL_BG:
        bttn.config(bg = DEAD_CELL_BG)
    else:
        bttn.config(bg = ALIVE_CELL_BG)

def reset(arr):

    for x in arr:
        x.config(bg = DEAD_CELL_BG)

def rand_con():

    for r in range(2113):
        BUTTON_LIST[random.randint(0, 4224)].config(bg=ALIVE_CELL_BG)


root = tk.Tk()
root.minsize(WINDOW_SIZE[1],WINDOW_SIZE[0])
root.maxsize(WINDOW_SIZE[1],WINDOW_SIZE[0])
root.title("Conway's Game of Life")
root.iconbitmap("conway.ico")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

horizontal_offset = int((screen_width/2) - (WINDOW_SIZE[1]/2))
vertical_offset = int((screen_height/2) - (WINDOW_SIZE[0]/2))

root.geometry(str(WINDOW_SIZE[1]) + "x" + str(WINDOW_SIZE[0]) + "+" + str(horizontal_offset) + "+" + str(vertical_offset))


BUTTON_LIST = []
for l in range(0,GRID_SIZE,10):
    for n in range(0,GRID_SIZE,10):

        my_frame = tk.Frame(root, height = 9, width = 9)
        my_frame.pack_propagate(False)
        my_frame.place(x = l, y = n, anchor = "nw")


        my_button = tk.Button(my_frame, bg = DEAD_CELL_BG, bd = 0)
        my_button.config(command = lambda my_button = my_button: changeColour(my_button))
        my_button.pack(fill = "both", expand = True)

        BUTTON_LIST.append(my_button)


BUTTON_ARRAY = []
for q in range((GRID_SIZE//10)):
    temp = []
    for w in range((GRID_SIZE//10)):
        temp.append(BUTTON_LIST[(GRID_SIZE//10)*w+q])
    BUTTON_ARRAY.append(temp)


next_gen = tk.Button(root, text = "Next Generation", bg = "black", fg = "white", command = conway)
next_gen.place(x = 5, y = GRID_SIZE)

res = tk.Button(root, text = "Reset", bg = "black", fg = "white", command = lambda: reset(BUTTON_LIST))
res.place(x = 165, y = GRID_SIZE)

rand_button = tk.Button(root, text = "Random", bg = "black", fg = "white", command = rand_con)
rand_button.place(x = 260, y = GRID_SIZE)

entry_wid = tk.Entry(root, bg = "grey", fg = "white")
entry_wid.place(x = 396, y = GRID_SIZE)

button_locator = tk.Button(
    root,
    text = "Locate at coordinates",
    bg = "black",
    fg = "white",
    command = lambda: locator(BUTTON_ARRAY, cleaner(entry_wid.get())[0], cleaner(entry_wid.get())[1])
)
button_locator.place(x = 520, y = GRID_SIZE)

root.mainloop()
