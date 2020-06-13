board = [0, 1, 2, 
         3, 4, 5, 
         6, 7, 8]

available_places = [0,1,2,3,4,5,6,7,8]

def Draw_Board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()

def Player_1():
    print("Player#1, Enter your desired board location: ")
    location = int(input())
    
    if board[location] != 'X' and board[location] != 'O':
        board[location] = 'X'
        available_places.remove(location)
    else:
        print('Oops! You missed your chance. This spot is taken, please choose somewhere else')
    

def Player_2():
    print("Player#2, Enter your desired board location: ")
    location = int(input())
    
    if board[location] != 'X' and board[location] != 'O':
        board[location] = 'O'
        available_places.remove(location)
    else:
        print('Oops! You missed your chance. This spot is taken, please choose somewhere else')

def Winner_Check(X_or_O):
    if board[0] == X_or_O and board[1] == X_or_O and board[2] == X_or_O:
        return True
    if board[3] == X_or_O and board[4] == X_or_O and board[5] == X_or_O:
        return True
    if board[6] == X_or_O and board[7] == X_or_O and board[8] == X_or_O:
        return True
    if board[0] == X_or_O and board[3] == X_or_O and board[6] == X_or_O:
        return True
    if board[1] == X_or_O and board[4] == X_or_O and board[7] == X_or_O:
        return True
    if board[2] == X_or_O and board[5] == X_or_O and board[8] == X_or_O:
        return True
    
    # Diagonal terms
    if board[0] == X_or_O and board[4] == X_or_O and board[8] == X_or_O:
        return True
    if board[2] == X_or_O and board[4] == X_or_O and board[6] == X_or_O:
        return True
    if (len(available_places) == 0):
        print("No available places. Game ends in draw")
        return False
        
