import tkinter as tk
import random

# set the size of the grid
GRID_SIZE = 30

# create the grid
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# randomly fill the grid with 1's and 0's
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        grid[row][col] = random.randint(0, 1)

# create the Tkinter window
window = tk.Tk()
window.title("Game of Life")

# create the canvas to display the grid
canvas = tk.Canvas(window, width=500, height=500, bg='white')
canvas.pack()

# draw the initial grid
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        if grid[row][col] == 1:
            canvas.create_rectangle(col*16, row*16, col*16+16, row*16+16, fill='black')

# define the update function
def update():
    global grid
    new_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if row+i < 0 or row+i >= GRID_SIZE or col+j < 0 or col+j >= GRID_SIZE:
                        continue
                    if grid[row+i][col+j] == 1:
                        count += 1
            if grid[row][col] == 1:
                if count < 2 or count > 3:
                    new_grid[row][col] = 0
                else:
                    new_grid[row][col] = 1
            else:
                if count == 3:
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = 0
    grid = new_grid
    canvas.delete('all')
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 1:
                canvas.create_rectangle(col*16, row*16, col*16+16, row*16+16, fill='black')
    window.after(100, update)

# start the update loop
window.after(100, update)

# start the Tkinter event loop
window.mainloop()
