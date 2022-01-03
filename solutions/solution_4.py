import numpy as np
from os import sys
path = "../data/input_4.txt"

with open(path, "r") as f:
    rnd_numbers = f.readline().rstrip()
    
rnd_numbers = list(map(int, rnd_numbers.split(',')))

bingo_boards = np.loadtxt(path, skiprows=1, usecols=(0,1,2,3,4))

borad_width = len(bingo_boards[0])
n_boards = int(len(bingo_boards)/borad_width)

for board in range(n_boards):
    this_board = bingo_boards[5*board:5*board+5, :]
# needs reworking     
for i, rnd_number in enumerate(rnd_numbers):
    rnd_numer_drawn = set(rnd_numbers[:i+1])
    
    for board in range(n_boards):
        this_board = bingo_boards[5*board:5*board+5, :]
        flat_board = set(this_board.flatten())
        
        for row, col in zip(this_board, np.transpose(this_board)):
            if (len(set(row) & rnd_numer_drawn) == borad_width):
                crossed_numbers = flat_board & rnd_numer_drawn
                uncrossed_numbers = flat_board - crossed_numbers
                final_score = list(rnd_numer_drawn)[-1] * np.sum(list(uncrossed_numbers))
                print(final_score)
                exit() 
            if (len(set(col) & rnd_numer_drawn) == borad_width):
                crossed_numbers = flat_board & rnd_numer_drawn
                uncrossed_numbers = flat_board - crossed_numbers
                final_score = rnd_number * np.sum(list(uncrossed_numbers))
                print(final_score)
                exit()
