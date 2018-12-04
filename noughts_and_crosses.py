# from IPython.display import clear_output


def displayboard(board):
    print('\n'*100)
    # clear_output()
    print('|'.join(board[1:4]))
    print('---|---|---')
    print('|'.join(board[4:7]))
    print('---|---|---')
    print('|'.join(board[7:]))


def turn(player):
    choice = input(f'\n{player} select your square: ')
    if board[int(choice)] == '   ':
        return int(choice)
    else:
        return False


def wincheck():
    if board[1] == board[2] and board[1] == board[3] and board[1] != '   ':
        return board[1]
    elif board[4] == board[5] and board[4] == board[6] and board[4] != '   ':
        return board[4]
    elif board[7] == board[8] and board[7] == board[9] and board[7] != '   ':
        return board[7]
    elif board[1] == board[4] and board[1] == board[7] and board[1] != '   ':
        return board[1]
    elif board[2] == board[5] and board[2] == board[8] and board[2] != '   ':
        return board[2]
    elif board[3] == board[6] and board[3] == board[9] and board[3] != '   ':
        return board[3]
    elif board[1] == board[5] and board[1] == board[9] and board[1] != '   ':
        return board[1]
    elif board[3] == board[5] and board[3] == board[7] and board[3] != '   ':
        return board[3]
    else:
        return False


def game_over_check(win, player, board):
    if win == ' X ' or win == ' O ':
        print(f'\nCongratulations {player}.....Victory!!!')
        return False
    elif '   ' not in board:
        print('\nGame is a Draw!!!')
        return False
    else:
        return True


# setup game variables and display number instructions board
players = [('Player 1', ' X '), ('Player 2', ' O ')]
board = [' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']
game_flag = True

displayboard(board)

# setup game board and display instrutions
board = ['   ']*10
board[0] = ' . '

print('\n INSTRUCTIONS\n')
print(f'{players[0][1]}- {players[0][0]} will go first')
print(f'{players[1][1]}- {players[1][0]} will go second')

# main game loop
while game_flag is True:

    # alternate player turns
    for player, symbol in players:

        # take player turn & check valid selection
        choice = False
        while choice is False:
            choice = turn(player)
            if choice is False:
                print('Invalid choice, try again')

        # ammend game board & check if any win conditions met
        board[choice] = symbol
        # clear_output
        print('\n'*100)
        displayboard(board)
        print('\n')
        win = wincheck()

        # check for draw and end game/display message if draw or winner
        game_flag = game_over_check(win, player, board)
        if game_flag is False:
            break
