#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Setting up the tictactoe board

def display_board(board):
    print(board[0],'|',board[1],'|', board[2])
    print('-','-','-','-','-')
    print(board[3],'|',board[4],'|', board[5])
    print('-','-','-','-','-')
    print(board[6],'|',board[7],'|', board[8])
    

#Choosing and Assigning Markers to players - X or O
#PLayers should only be able to choose between either of these two

def player_input():
    player_marker = 'None'
    while player_marker != 'X' and player_marker !='O':
        player_marker = input("Please pick a marker 'X' or 'O'")
    print('You have chosen the marker: {}'.format(player_marker))
    return player_marker

#Marker position

def place_marker(board, marker, position):
    board[position-1] = marker
    
#Choosing which players goes first randomly

import random

def choose_first():
    num = random.randint(1,2)
    if num == 1:
        return 'player1'
    else:
        return 'player2'
    
#Space check, to see if a position is available

def space_check(board, position):
    check = False
    if board[position-1] == " ":
        check = True
    return check

#Full Board check

def full_board_check(board):
    check_full = True
    for i in range(0,9):
        if board[i] == " ":
            check_full = False
            break
    return check_full

#Position check and input

def player_choice(board):
    next_position = 'None'

    while next_position not in ['1','2','3','4','5','6','7','8','9']:
        next_position = input('Please choose your position (only between 1-9): ')
        
    while not space_check(board, int(next_position)):
        print('Sorry the position is not available')
        next_position = int(input('Please choose another position (only between 1-9): '))
    
    if space_check(board, int(next_position)):
        return int(next_position)

#Win check for a particular mark

def win_check(board, mark):
    check = False
    if board[0] == board[4] == board[8] == mark or board[2] == board[4] == board[6] == mark:
        check = True
    else:
        for i in range(2):
            if board[i] == board[i+1] == board[i+2] == mark or board[i] == board[i+3] == board [i+6] == mark:
                check = True
    return check

#If the player wants to replay again once the round is done

def replay():
    replay_choice = 'None'
    while replay_choice != 'Y' and replay_choice != 'N':
        replay_choice = input('Do you want to play again [Y/N]?')
    if replay_choice == 'Y':
        #print('\n'*100)
        return True
    
#Running the game!

print('Welcome to Tic Tac Toe!')

while True:
    print('Picking the first player randomly')
    
    player_list = ['player1', 'player2']
    first_player = choose_first()
    player_list.remove(first_player)
    [second_player] = player_list
    
    #choosing the first player and assigning them a marker of their choice
    if first_player == 'player1':
        print('player1 goes first')
        player_marker = player_input()
        if player_marker == 'X':
            player2_marker = 'O'
        else:
            player2_marker = 'X'
    else:
        print('player2 goes first')
        player_marker = player_input()
        if player_marker == 'X':
            player2_marker = 'O'
        else:
            player2_marker = 'X'
    
    game_on = True
    
    #setting the inital board as empty
    game_board = [' ']*9

    while game_on:
        #Player 1 Turn
        position1 = player_choice(game_board)
        place_marker(board=game_board, marker=player_marker, position=position1)
        display_board(game_board)
        if win_check(game_board, player_marker):
            print('{} won!'.format(first_player))
            game_on = False
            break
        elif full_board_check(game_board):
            print("It's a TIE!")
            game_on = False
            break
        
        # Player2's turn.
        position2 = player_choice(game_board)
        place_marker(board=game_board, marker=player2_marker, position=position2)
        display_board(game_board)
        if win_check(game_board, player2_marker):
            print('{} won!'.format(second_player))
            game_on = False
        elif full_board_check(game_board):
            print("It's a TIE!")
            game_on = False
            break

    if not replay():
        print('Thanks for playing')
        break   

