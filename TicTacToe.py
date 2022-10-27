def check(pos):
    
    #Check the lines
    aux = 0
    while aux <= 6:
        if pos[aux] == pos[aux+1] == pos[aux+2] != ' ':
            print(pos[aux], 'won!')
            return True
        aux += 3

    #Check the columns
    for aux in range(3):
        if pos[aux] == pos[aux+3] == pos[aux+6] != ' ':
            print(pos[aux], 'won!')
            return True

    #Check the diagonals
    if (pos[0] == pos[4] == pos[8] != ' ') or (pos[6] == pos[4] == pos[2] != ' '): 
        print(pos[4], 'won!')
        return True

    return False

def place(pos, symbol):
    
    aux = int(input(f'Where do you want to position {symbol}? ')) - 1
    
    if pos[aux]  == ' ':
        pos[aux] = symbol
    else: 
        print('Position already occupied, choose another')
        place(pos, symbol)
    
    print(f'I  {pos[0]}  I  {pos[1]}  I  {pos[2]}  I\nI-----I-----I-----I\nI  {pos[3]}  I  {pos[4]}  I  {pos[5]}  I\nI-----I-----I-----I\nI  {pos[6]}  I  {pos[7]}  I  {pos[8]}  I\n')

    return check(pos)

pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
symbol = ['O', 'X']
print('Positions are numbered from 1 to 9\n'f'I  1  I  2  I  3  I\nI-----I-----I-----I\nI  4  I  5  I  6  I\nI-----I-----I-----I\nI  7  I  8  I  9  I\n')

for i in range(9): 

    if place(pos, symbol[0]) == True:
        break

    symbol[0], symbol[1] = symbol[1], symbol[0]
