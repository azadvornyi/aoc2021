import numpy as np

path = "../data/input_7.txt"

data = np.loadtxt(path, delimiter=',')

min_pos = min(data)
max_pos = max(data)

span = np.arange(min_pos, max_pos)
difference_sum = np.zeros(len(span))

for i in range(len(span)):
    difference_sum[i] = np.sum(abs(data-span[i]))
    
print(min(difference_sum))
    