import numpy as np

path = "../data/input_7.txt"

data = np.loadtxt(path, delimiter=',')

# Part 1

min_pos = min(data)
max_pos = max(data)

span = np.arange(min_pos, max_pos)
difference_sum = np.zeros(len(span))

for i in range(len(span)):
    difference_sum[i] = np.sum(abs(data-span[i]))
    
print(min(difference_sum))
    
    
# Part 2   

difference_sum = np.zeros(len(span))

for i, s in enumerate(span):
    fuel_spent = 0
    differenence = abs(data - s)
    for diff in differenence:
        fuel_spent += np.sum(np.arange(diff+1))
    difference_sum[i] = fuel_spent
    
print(min(difference_sum))