import numpy as np

# Part 1
data = np.loadtxt('input_1.txt')

increased = 0 
comparison = data[0]

for dat in data[1:]:
    if dat > comparison:
        increased += 1
    comparison = dat

print(increased)
   
# Part 2
increased = 0 
w_len = 3
window_sum = np.sum(data[:w_len])

for i in range(len(data)-w_len):
    next_sum = np.sum(data[i+1:i+w_len+1])
    if  next_sum > window_sum:
        increased += 1
    window_sum = next_sum
   

    
print(increased)        
    



