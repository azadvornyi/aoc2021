import numpy as np
import pandas as pd

path = '../data/input_6.txt'

data = np.loadtxt(path, delimiter=',')
is_new = np.zeros(len(data))
days = 80

# Part 1

for day in range(days):
    data -= 1
    spawn_count = len(data[data == 0])
    data = np.append(data, np.ones(spawn_count)*9)
    data[data == -1] = 6
    
print(len(data[data < 9]))

# Part 2

data_indexed=np.zeros(9)
days = 256

for day in range(9):
    data_indexed[day] = len(data[data==day])
    
for i in range(days):
    first = data_indexed[0]
    for j in range(8):
        data_indexed[j] = data_indexed[j+1]
        if j == 6:
            data_indexed[j]+=first
    data_indexed[-1] = first
    
print(np.sum(data_indexed))
        
    
