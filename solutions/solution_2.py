import numpy as np
import pandas as pd

data = pd.read_csv("input_2.txt", sep=" ", header=None)

# Part 1

pivot_tab = pd.pivot_table(data, values=1, index=0, aggfunc=np.sum)
final_course = (pivot_tab.loc['down'] - pivot_tab.loc['up']) * pivot_tab.loc['forward']

print(final_course)

# Part 2

aim = 0
depth = 0
forward = 0 

for i in range(len(data)):
    if data.iloc[i][0] == 'down':
        aim += data.iloc[i][1]
    if data.iloc[i][0] == 'up':
        aim -= data.iloc[i][1]
    if data.iloc[i][0] == 'forward':
        forward += data.iloc[i][1]
        depth += aim*data.iloc[i][1]
    
print(depth * forward)
        
        
        

    