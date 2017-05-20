# create board for play
row1 = ['0','0','0']
row2 = ['0','0','0']
row3 = ['0','0','0']

# to reference the board
def showboard():
    print row1
    print row2
    print row3

# list for tracking choices
used = []

# to check if someone has won
def scorechecker():
    # Winning sequence on row1
    if row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O':
        print '%s 1 wins!' % (p1)
    if row1[0] == 'X'and row1[1] == 'X' and row1[2] == 'X':
        print '%s wins!' % (p2)
    # winning sequence row2
    if row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O':
        print '%s 1 wins!' % (p1)
    if row2[0] == 'X'and row2[1] == 'X' and row2[2] == 'X':
        print '%s wins!' % (p2)
    # winning sequence row3
    if row3[0] == 'O' and row3[1] == 'O' and row3[2] == 'O':
        print '%s 1 wins!' % (p1)
    if row3[0] == 'X'and row3[1] == 'X' and row3[2] == 'X':
        print '%s wins!' % (p2)
    # winning sequence diag 1
    if row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O':
        print '%s 1 wins!' % (p1)
    if row1[0] == 'X'and row2[1] == 'X' and row3[2] == 'X':
        print '%s wins!' % (p2)
    # winning sequence daig 2
    if row3[0] == 'O' and row2[1] == 'O' and row1[2] == 'O':
        print '%s 1 wins!' % (p1)
    if row3[0] == 'X'and row2[1] == 'X' and row1[2] == 'X':
        print '%s wins!' % (p2)
    else:
        pass

# for player 1's placements
def scorekeeperp1(user_input):
    if user_input == 1:
        row3[0]= 'O'
    if user_input == 2:
        row3[1]= 'O'
    if user_input == 3:
        row3[2]= 'O'
    if user_input == 4:
        row2[0]='O'
    if user_input == 5:
        row2[1]='O'
    if user_input == 6:
        row2[2]='O'
    if user_input == 7:
        row1[0]='O'
    if user_input == 8:
        row1[1]='O'
    if user_input == 9:
        row1[2]='O'
        
# for player 2's placements
def scorekeeperp2(user_input):
    if user_input == 1:
        row3[0]= 'X'
    if user_input == 2:
        row3[1]= 'X'
    if user_input == 3:
        row3[2]= 'X'
    if user_input == 4:
        row2[0]='X'
    if user_input == 5:
        row2[1]='X'
    if user_input == 6:
        row2[2]='X'
    if user_input == 7:
        row1[0]='X'
    if user_input == 8:
        row1[1]='X'
    if user_input == 9:
        row1[2]='X'

# Player 1's space chekcer 
def p1turn(user_input):
    while user_input in used:
        print 'Sorry, please choose another space. This one has already been taken.'
        user_input = input()
    if user_input not in used:
        used.append(user_input)
        scorekeeperp1(user_input)
        showboard()
    else:
        pass
