import numpy as np
import re
# import matplotlib as mpl
# mpl.use('TkAgg')
import matplotlib.pyplot as plt

path = "../data/input_13.txt"

x_val, y_val = np.loadtxt(path, unpack=True, comments=[" ", "f"], delimiter=",")

# Part 1

folds = []   

with open(path, 'r') as f:
    for line in f:
        reg = r"[x|y]\=\d+"
        found =re.search(reg, line)
        if found is not None:
            folds.append(found.group())

        
for fold in folds[:1]:
    if 'x' in fold:
        fold = fold.replace('x=','')
        fold = int(fold)
        for i in range(len(x_val)):
            if  x_val[i]> fold:
                x_val[i] = fold*2 - x_val[i]
    elif 'y' in fold:
        fold = fold.replace('y=','')
        fold = int(fold)
        for i in range(len(y_val)):
            if  y_val[i]> fold:
                y_val[i] = fold*2 - y_val[i]    

mapped = zip(x_val, y_val)
print(len(set(mapped)))

# Part 2

for fold in folds:
    if 'x' in fold:
        fold = fold.replace('x=','')
        fold = int(fold)
        for i in range(len(x_val)):
            if  x_val[i]> fold:
                x_val[i] = fold*2 - x_val[i]
    elif 'y' in fold:
        fold = fold.replace('y=','')
        fold = int(fold)
        for i in range(len(y_val)):
            if  y_val[i]> fold:
                y_val[i] = fold*2 - y_val[i]            
                

plt.scatter(x_val, -y_val)
plt.show()