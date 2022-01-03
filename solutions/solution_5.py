import numpy as np
import re

path = '../data/input_5.txt'

coords = []
reg = r"\d+"

with open(path, 'r') as f:
    for line in f:
        found = re.findall(reg, line)
        if found is not None:
            coords_to_int_list = list(map(int, found))
            coords.append(coords_to_int_list)

coords = np.transpose(np.array(coords))       
x1 = coords[0]
y1 = coords[1]
x2 = coords[2]
y2 = coords[3]

grid_size_y = np.max(np.append(y1,y2))
grid_size_x = np.max(np.append(x1,x2))

grid = np.zeros((grid_size_y+1, grid_size_x+1))

for X1,Y1,X2,Y2 in zip(x1,y1,x2,y2):
    if (X1 == X2):
        grid[min([Y1,Y2]):max([Y1,Y2])+1, X1:X1+1] +=1
    elif (Y1 == Y2):
        grid[Y1:Y1+1, min([X1,X2]):max([X1,X2])+1] +=1
             
overlap_count = len(np.argwhere(grid>1))

print(overlap_count)

# Part 2

grid_size_y = np.max(np.append(y1,y2))
grid_size_x = np.max(np.append(x1,x2))

grid = np.zeros((grid_size_y+1, grid_size_x+1))

for X1,Y1,X2,Y2 in zip(x1,y1,x2,y2):
    if (X1 == X2):
        grid[min([Y1,Y2]):max([Y1,Y2])+1, X1:X1+1] +=1
    elif (Y1 == Y2):
        grid[Y1:Y1+1, min([X1,X2]):max([X1,X2])+1] +=1
    else:
        for i,j in zip(range(min([X1,X2]),max([X1,X2])+1),
                        range(min([Y1,Y2]),max([Y1,Y2])+1)):
            grid[j][i] +=1
            
           

overlap_count = len(np.argwhere(grid>1))

print(overlap_count)