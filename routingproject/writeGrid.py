from random import randint

grid_file = open("grid.py","wb")

grid = [[randint(1,100) for i in range(1,6)] for i in range(1,6)]

grid_file.write(grid)
grid_file.close()
print("New grid written to grid.py")
