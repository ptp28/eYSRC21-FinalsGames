'''
*****************************************************************************************
*
*        		=================================================
*           	e-Yantra School Robotics Competition (eYSRC 2021)
*        		=================================================
*
*  This script is to be used to implement Mini Assignment titled- 'Tic Tac Toe: Player vs Player'.
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*  
*  e-Yantra - A MOE project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          
# 					[ Team-ID ]
# Author List:      
# 					[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:         tic_tac_toe.py
# Functions:        t_tracker, check_for_win, do_none, initialize_screen, draw_board, draw_circle, draw_x, draw,
#                   gameover, play, reinitialize_screen, input_names_of_player, bestMove, minimax
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this assignment with the available ##
## modules for this task.								    ##
##############################################################
import turtle
import os, sys, traceback

##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################

screen = turtle.Screen()
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = 'x'
player = []
pen = turtle.Turtle()
test = False
playing = True


# To display whose turn it is
def t_tracker():
    pen.hideturtle()
    pen.goto(0, 4)
    pen.color('white')
    pen.clear()
    if turn == 'x' and player[0] is not None and player[0] != '':
        pen.write(f"{player[0]}'s Turn (X)", align='center', font=('Orbitron', 30, 'bold'))
    elif turn == 'o' and player[1] is not None and player[1] != '':
        pen.write(f"{player[1]}'s Turn (O)", align='center', font=('Orbitron', 30, 'bold'))
    elif turn == 'o':
        pen.write(f"Player O's Turn", align='center', font=('Orbitron', 30, 'bold'))
    elif turn == 'x':
        pen.write(f"Player X's Turn", align='center', font=('Orbitron', 30, 'bold'))


# To check for win using the gameover function
def check_for_win():
    global playing, screen
    replay = False

    game_state = gameover(board)
    if game_state == 1 and player[0] is not None:
        x_won = screen.textinput('TIC TAC TOE', f'{player[0].upper()}(X) Won \n\n Type yes/y to play again')
        replay = x_won
        playing = False
    elif game_state == 2 and player[1] is not None:
        o_won = screen.textinput('TIC TAC TOE', f'{player[1].upper()}(O) Won \n\n Type yes/y to play again')
        replay = o_won
        playing = False
    elif game_state == 1:
        x_won = screen.textinput('TIC TAC TOE', f'Player X Won \n\n Type yes/y to play again')
        replay = x_won
        playing = False
    elif game_state == 2:
        o_won = screen.textinput('TIC TAC TOE', f'Player O Won \n\n Type yes/y to play again')
        replay = o_won
        playing = False
    elif game_state == 3:
        tie = screen.textinput('TIC TAC TOE', 'It is a tie \n\n Type yes/y to play again')
        replay = tie
        playing = False

    if replay is not None:
        if type(replay) == str:
            if replay.lower() == 'yes' or replay.lower() == 'y':
                playing = True
                reinitialize_screen()
            else:
                screen.bye()
    else:
        screen.bye()


def do_none(x, y):
    pass

##############################################################


def initialize_screen():
    """
    Purpose:
    ---
    Use this function to initialize the screen that is to be used by turtle.
    Also initialize `board` variable as
        board = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]  # Nested list representing the value inside each box of the game.

    NOTE:
    1. Width and Height of the screen should both be 800 pixels.
    2. World coordinates should range from -5 to 5 for both the axes.
    ---
    """
    global screen

    ##############	ADD YOUR CODE HERE	##############

    screen.setup(800, 800)
    screen.title("Tic Tac Toe - e-Yantra")
    screen.setworldcoordinates(-5, -5, 5, 5)
    screen.bgcolor('black')
    screen.tracer(n=2, delay=10)
    turtle.speed(0)
    turtle.showturtle()
    turtle.resetscreen()

    ##################################################


def draw_board():
    """
    Purpose:
    ---
    Use this function to draw the board of Tic Tac Toe.
    ---
    """
    ##############	ADD YOUR CODE HERE	##############

    turtle.pencolor('green')
    turtle.pensize(10)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(-3, -1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3, 1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1, -3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1, -3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

    screen.update()

    ##################################################


def draw_circle(x, y):
    """
    Purpose:
    ---
    Use this function to draw circle (representing O's turn).
    ---
    Input Arguments:
    ---
    `x`	:	x coordinate of the center of the circle
    `y`	:	y coordinate of the center of the circle
    ---
    """
    ##############	ADD YOUR CODE HERE	##############

    turtle.up()
    turtle.goto(x, y - 0.75)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.75, steps=15)

    screen.update()

    ##################################################


def draw_x(x, y):
    """
    Purpose:
    ---
    Use this function to draw X (representing X's turn).
    ---
    Input Arguments:
    ---
    `x`	:	x coordinate of X mark
    `y`	:	y coordinate of X mark
    ---
    """
    ##############	ADD YOUR CODE HERE	##############

    turtle.color('yellow')

    turtle.up()
    turtle.goto(x - 0.75, y - 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y + 0.75)
    turtle.up()
    turtle.goto(x - 0.75, y + 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y - 0.75)

    screen.update()

    ##################################################


def draw(i, j, p):
    """
    Purpose:
    ---
    Use this function to decide when to call draw_x(x,y) and draw_circle(x,y).
    ---
    Input Arguments:
    ---
    `i`	:	Definition will depend on your logic
    `j`	:	Definition will depend on your logic
    `p`	:	Definition will depend on your logic
    ---

    """
    ##############	ADD YOUR CODE HERE	##############

    global turn

    x, y = 2 * (j - 1), -2 * (i - 1)

    if p == 0:
        return
    elif p == 1:
        draw_x(x, y)
        turn = 'o'
    else:
        draw_circle(x, y)
        turn = 'x'

    t_tracker()

    ##################################################


def gameover(board):
    """
    Purpose:
    ---
    Use this function to decide if the game has reached a terminal condition or not.
    ---
    Input Arguments:
    ---
    `board`	: Nested list representing the value inside each box of the game.
    ---
    Return: 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
    ---

    """
    ##############	ADD YOUR CODE HERE	##############

    global test

    screen.onclick(do_none)

    for i in range(3):
        if board[i][0] > 0 and board[i][0] == board[i][1] == board[i][2]:
            if test is False:
                start_x, start_y = 2 * (0 - 1), -2 * (i - 1)
                end_x, end_y = 2 * (2 - 1), -2 * (i - 1)

                screen.tracer(1)

                turtle.penup()
                turtle.goto(start_x - 1, start_y)
                turtle.pendown()
                turtle.goto(end_x + 1, end_y)

                screen.tracer(n=2, delay=10)

            return board[i][0]

        if board[0][i] > 0 and board[0][i] == board[1][i] == board[2][i]:
            if test is False:
                start_x, start_y = 2 * (i - 1), -2 * (0 - 1)
                end_x, end_y = 2 * (i - 1), -2 * (2 - 1)

                screen.tracer(1)

                turtle.penup()
                turtle.goto(start_x, start_y + 1)
                turtle.pendown()
                turtle.goto(end_x, end_y - 1)

                screen.tracer(n=2, delay=10)

            return board[0][i]

    if board[0][0] > 0 and board[0][0] == board[1][1] == board[2][2]:
        if test is False:
            start_x, start_y = 2 * (0 - 1), -2 * (0 - 1)
            end_x, end_y = 2 * (2 - 1), -2 * (2 - 1)

            screen.tracer(1)

            turtle.penup()
            turtle.goto(start_x - 1, start_y + 1)
            turtle.pendown()
            turtle.goto(end_x + 1, end_y - 1)

            screen.tracer(n=2, delay=10)

        return board[0][0]

    if board[0][2] > 0 and board[0][2] == board[1][1] == board[2][0]:
        if test is False:
            start_x, start_y = 2 * (2 - 1), -2 * (0 - 1)
            end_x, end_y = 2 * (0 - 1), -2 * (2 - 1)

            screen.tracer(1)

            turtle.penup()
            turtle.goto(start_x + 1, start_y + 1)
            turtle.pendown()
            turtle.goto(end_x - 1, end_y - 1)

            screen.tracer(n=2, delay=10)

        return board[0][2]

    none = 0

    for i in range(3):
        if 0 not in board[i]:
            none += 1

    if none == 3:
        return 3

    screen.onclick(play)
    return 0

    ##################################################


def play(x, y):
    """
    Purpose:
    ---
    Use this function when a click is detected on the screen.
    ---
    Input Arguments:
    ---
    `x`	:	x coordinate where the click is detected
    `y`	:	y coordinate where the click is detected
    ---
    """
    # Cordinate system before conversion (Top left is (-5,5) and bottom right is (5,-5)):
    '''
    y
    ↑
    |
    |
    .-----→x
    (-5,5)						   (5,5)
    .----------------------------------.
    |				 |				   |
    |				 |				   |
    |				 |				   |	
    |				 |(0,0)			   |
    |----------------.-----------------|
    |				 |				   |
    |				 |				   |
    |				 |				   |
    |				 |				   |
    .----------------------------------.
    (-5,-5)						  (5,-5)

    '''
    # Cordinate system after conversion (Top left is (0,0) and bottom right is (2,2)):
    '''
    .----→j		|	  |
    |		0,0 |	  | 2,0
    |	   _____|_____|_____
    ↓			|	  |
    i			| 1,1 |
           _____|_____|_____
                |	  | 
            0,2	|	  | 2,2
                |	  |
    '''
    # Conversion from one coordinate system to another:
    '''
    Conversion of x to j:
     x	|	j
    ---------
    -3	|	0
    -1	|	1
     1	|	2

    Assume x=aj+b,
    Solve simultaneously for the above limits
    and obtain the value of a and b

    Conversion of y to i:
     y	|	i
    ---------
     3	|	0
     1	|	1
    -1	|	2

    Assume y=ai+b,
    Solve simultaneously for the above limits
    and obtain the value of a and b.

    '''
    ##############	ADD YOUR CODE HERE	##############
    global board, test, playing

    t_tracker()

    i = -(int(y - 3)) // 2
    j = (int(x + 3)) // 2

    if i > 2 or j > 2 or i < 0 or j < 0 or board[i][j] != 0:
        return
    if turn == 'x' and playing:
        board[i][j] = 1
        draw(i, j, board[i][j])
        t_tracker()
        check_for_win()
    if turn == 'o' and playing:
        cor_1, cor_2, board = bestMove(board)
        test = False
        draw(cor_1, cor_2, board[cor_1][cor_2])
        t_tracker()
        check_for_win()

    ##################################################


def reinitialize_screen():
    """
    Purpose:
    ---
    Use this function to reinitialize the screen.
    """
    ##############	ADD YOUR CODE HERE	##############

    global board, turn

    screen.resetscreen()
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    draw_board()

    turn = 'x'
    t_tracker()

    screen.onclick(play)

    screen.update()

    ##################################################


def input_names_of_player():
    """
    Purpose:
    ---
    Use this function to add name of the player.

    Refer screen.textinput() from official documentation of turtle.
    """
    ##############	ADD YOUR CODE HERE	##############

    global player, screen
    player_x = screen.textinput("TIC TAC TOE", 'Enter name of Player')

    player.append(player_x)
    player.append('Computer')

    t_tracker()

    ##################################################


def bestMove(board):
    """
    Purpose:
    ---
    Use this function to decide the bestMove by the computer.
    ---
    Input Arguments:
    ---
    `board`	: Nested list representing the value inside cell of the game.
    ---
    Return:
    ---
    `board`   :  Updated nested list with computer's move.
    `coord_1` :  1st Coordinate of computer's move.
    `coord_2` :  2nd Coordinate of computer's move.

    ---
    NOTE: Remember to use the following convention-
    0: Cell is empty
    1: 'X' i.e. player's move
    2: 'O' i.e. computer's move

    """
    ##############	ADD YOUR CODE HERE	##############
    # Computer to make its turn

    # NOTE: `__` denotes blanks which are supposed to be filled by students.

    global test

    test = True

    bestScore = float('-inf')  # Initialize `bestScore` to the lowest value since we want score to be the highest.
    coord_1 = 0  # Initialize 1st Coordinate of computer's move.
    coord_2 = 0  # Initialize 2nd Coordinate of computer's move.
    bestDepth = float('inf')  # Initialize `bestDepth` to highest value since we want depth to be the lowest.

    # Iterating through the entire board.
    for i in range(0, 3):
        for j in range(0, 3):
            # Is the spot available?
            if board[i][j] == 0:
                # If yes, assign the spot for 'O' i.e. computer and call the minimax algorithm.
                board[i][j] = 2
                depth, score = minimax(board, 0, False)  # Player is trying the next move. Hence the next move is not the maximizing move.
                board[i][j] = 0  # Revert the board back to original position.
                if (score >= bestScore == 10 and depth < bestDepth) or (score >= bestScore != 10):  # Write condition to update the value of bestScore and bestDepth.
                    bestScore = score
                    bestDepth = depth
                    coord_1, coord_2 = i, j

    board[coord_1][coord_2] = 2  # Update the board with computer's position.
    ##################################################
    return coord_1, coord_2, board


def minimax(board, depth, isMaximizing):
    """
    Purpose:
    ---
    Use this function to find the depth and score using MiniMax Algorithm.
    ---
    Input Arguments:
    ---
    `board`	: Nested list representing the value inside cell of the game.
    `depth` : Depth/Number of moves by player and computer.
    `isMaximizing` : True/False
    ---
    Return:
    ---
    `depth` :  Depth when a terminal condition i.e. player wins/computer wins/tie is achieved.
    `bestScore` : Maximum score achieved at a terminal condition.
    ---
    """
    ##############	ADD YOUR CODE HERE	##############

    scores = [0, -10, 10, 0]  # Index of this list corresponds to return value of gameover() function.
    result = gameover(board)  # return 1 if player 1 wins, 2 if computer wins, 3 if tie, 0 if game is not over
    if result != 0:  # Return the score if it is a terminal state i.e. one of the three possibilities: 1. Player 1 Wins, 2. Computer Wins, 3. Tie
        return depth, scores[result]

    if isMaximizing:  # Maximizing player's turn i.e. computer.
        bestScore = float('-inf')
        for i in range(0, 3):
            for j in range(0, 3):
                # // Is the spot available?
                if board[i][j] == 0:
                    # If yes, assign the spot for 'O' i.e. computer and call the minimax algorithm.
                    board[i][j] = 2
                    depth, score = minimax(board, depth + 1, False)  # Player will try for the next move. Hence the next move is NOT the maximizing move.
                    board[i][j] = 0  # Revert the board back to original position.
                    bestScore = max(bestScore, score)  # Since our goal is to maximize the score of computer, find the maximum of the 2 numbers i.e. best score and score obtained.
        return depth, bestScore
    else:  # Minimizing player's turn i.e. human
        bestScore = float('inf')
        for i in range(0, 3):
            for j in range(0, 3):
                # // Is the spot available?
                if board[i][j] == 0:
                    # If yes, assign the spot for 'X' i.e. player and call the minimax algorithm.
                    board[i][j] = 1
                    depth, score = minimax(board, depth + 1, True)  # Computer will try for the next move. Hence the next move is the maximizing move.
                    board[i][j] = 0  # Revert the board back to original position.
                    bestScore = min(bestScore, score)  # Since our goal is to minimize the score of human i.e. player 1, we find the minimum of the 2 numbers i.e. best score and score obtained.
        return depth, bestScore
##################################################

# NOTE: 1. 'main' is executed only once in the entire run.
#       2.  Do not edit main function.


initialize_screen()
draw_board()  # Draw the board for the first time.
input_names_of_player()
screen.onclick(play)  # Bind function to mouse-click event on canvas. Coordinates of the click are passed as an argument to the function.
turtle.mainloop()
