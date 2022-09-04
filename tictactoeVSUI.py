import random

free_spaces = [0,1,2,3,4,5,6,7,8]
currdepth = 0

def winner_checker(board):
    if(    (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') 
        or (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') 
        or (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') 
        or (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') 
        or (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X')
        or (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X')
        or (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') 
        or (board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X')):
        return 1
    elif(  (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') 
        or (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') 
        or (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') 
        or (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') 
        or (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O')
        or (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O')
        or (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') 
        or (board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O')):
        return -1
    else:
        return 0


def solve(board,currdepth,maxdepth,free_spaces):
    global memo,bestmove
    key = str(board[0]) + ',' + str(board[1]) + ',' + str(board[2])
    # if key in memo:
    #     return memo[key]

    winner = winner_checker(board)
    if winner != 0:
        return winner
    elif winner == 0 and currdepth >= 9:
        return 0

    temp_free_spaces = list(free_spaces)
    ans_max = -2
    ans_min = 2
    a = -2 
    b = 2 
    perm_curr_depth = currdepth
    randlist = list(free_spaces)
    while(randlist != []):
        index = random.choice(randlist)
        randlist.remove(index)
        temp_free_spaces.remove(index)
        if(index<3):
            i = 0
            j = index
        elif(index<6):
            i = 1
            j = index - 3 
        elif(index<9):
            i = 2 
            j = index - 6 

        if( currdepth%2 == 0 ):
            board[i][j] = 'X'
            key = str(board[0]) + ',' + str(board[1]) + ',' + str(board[2])
            temp_ans_max = ans_max
            ans_max = max(ans_max,solve(board,currdepth+1,maxdepth,temp_free_spaces))
            board[i][j] = ' '
            memo[key] = ans_max
            if(ans_max != temp_ans_max):
                bestmove[0] = i 
                bestmove[1] = j 
                a = i 
                b = j 

        elif( currdepth%2 != 0 ):
            board[i][j] = 'O'
            key = str(board[0]) + ',' + str(board[1]) + ',' + str(board[2])
            temp_ans_min = ans_min
            ans_min = min(ans_min,solve(board,currdepth+1,maxdepth,temp_free_spaces))
            board[i][j] = ' '
            memo[key] = ans_min
            if(ans_min != temp_ans_min):
                bestmove[0] = i 
                bestmove[1] = j 
                a = i 
                b = j 

        temp_free_spaces = list(free_spaces)
    
    bestmove[0] = a 
    bestmove[1] = b 
    if( currdepth%2 == 0 ):
        return ans_max
    elif( currdepth%2 != 0 ):
        return ans_min

    return 0


def main(index,board):
    global memo,bestmove,free_spaces,currdepth
    bestmove = [0,0]
    memo = {}

    maxdepth = 9

    if(index<3):
        i = 0
        j = index
    elif(index<6):
        i = 1
        j = index - 3 
    elif(index<9):
        i = 2 
        j = index - 6

    board[i][j] = 'X'
    currdepth += 1
    free_spaces.remove(index)
    ans = solve(board,currdepth,maxdepth,free_spaces)
    currdepth += 1
    if (currdepth-1)%2 == 0 and board[bestmove[0]][bestmove[1]] == ' ':
        board[bestmove[0]][bestmove[1]] = 'X'
    elif (currdepth-1)%2 != 0 and board[bestmove[0]][bestmove[1]] == ' ':
        board[bestmove[0]][bestmove[1]] = 'O'

    print(board[0])
    print(board[1])
    print(board[2])
    print('')
    
    winner = winner_checker(board)
    if winner == 1:
        print("X wins!")
        quit(0)
    elif winner == -1:
        print("O wins!")
        quit(0)
    elif winner == 0 and currdepth >= 9:
        print("Tie")
        quit(0)

    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != ' ':
                try:
                    free_spaces.remove(counter)
                except:
                    a = 1
            counter += 1

    if bestmove[0] == 0:
        ans = bestmove[1]
    elif bestmove[0] == 1:
        ans = bestmove[1] + 3
    elif bestmove[0] == 2:
        ans = bestmove[1] + 6
    
    return ans,list(board)


if __name__ == '__main__':
    global board
    board = [
             [' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']
            ]
    main(0,board)