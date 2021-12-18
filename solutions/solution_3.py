import numpy as np
import pandas as pd

# Part 1

matrix = []
gamma=[]
epsilon=[]

def bin_to_dec(L, is_list):
    _sum = 0
    if is_list:
        for power, bit in enumerate(L[::-1]):
            _sum += int(bit)*2**power 
        return _sum
    else:
        n_bits = len(L.iloc[0])
        bit_counter = n_bits
        for bit in range(n_bits):
            bit_counter -= 1
            _sum += L[bit].values[0]*2**bit_counter
        return _sum

with open('../data/input_3.txt') as f:
    for line in f:
        matrix.append(list(line.rstrip()))


for h, i in enumerate(matrix):
    for k, j in enumerate(i):
        matrix[h][k] = int(j)

matrix_length =len(matrix)
sum_of_columns = np.sum(matrix, axis=0)

for col in sum_of_columns:
    if col >= matrix_length/2:
        gamma.append('1')
        epsilon.append('0')
    else:    
        gamma.append('0')
        epsilon.append('1')
        

gamma_sum = bin_to_dec(gamma, True)
epsilon_sum = bin_to_dec(epsilon, True)
ship_power = epsilon_sum*gamma_sum
print(ship_power)   

# Part 2

matrix_width = len(matrix[0])
matrixDF = pd.DataFrame(matrix, columns=range(matrix_width))
oxygenMatrix = matrixDF
scrubberRating = matrixDF

for bit in range(matrix_width):
    this_bit_mode = oxygenMatrix[bit].mode().values[-1]
    matrix_mask = oxygenMatrix[bit].loc[oxygenMatrix[bit] == this_bit_mode].index.values
    oxygenMatrix = oxygenMatrix.iloc[matrix_mask]
    oxygenMatrix = oxygenMatrix.reset_index(drop=True)
    if len(oxygenMatrix)==1:
            break

    
for bit in range(matrix_width):
    this_bit_mode = (scrubberRating[bit].mode().values[-1]+1) %2
    matrix_mask = scrubberRating[bit].loc[scrubberRating[bit] == this_bit_mode].index.values
    scrubberRating = scrubberRating.iloc[matrix_mask]
    scrubberRating = scrubberRating.reset_index(drop=True)    
    if len(scrubberRating)==1:
        break
    
Orating = bin_to_dec(oxygenMatrix, False)
CO2rating = bin_to_dec(scrubberRating, False)
lifeSupportRating = Orating * CO2rating
print(lifeSupportRating)
