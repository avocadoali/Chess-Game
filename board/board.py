
board = []

counter = 0

for r in range(8):
    row = []
    for c in range(8):
        row.append(counter)
        counter += 1

    board.append(row)



# board[0][0] - unten links
# board[7][7] - oben rechts 
# board y  x 