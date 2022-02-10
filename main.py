'''
*****************************************************************************************
*
*        		===============================================
*           		e-Yantra School Robotics Competition (eYSRC 2021)
*        		===============================================
*
*  This script is to be used to implement Competition Task titled- 'Connect 4'.
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
# Filename:         connect_4.py
# Functions:
#                   [ Comma separated list of functions in this file ]
# Global variables:
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this assignment with the available ##
## modules for this task.								    ##
##############################################################
import turtle

##############################################################
"""
Purpose:
---
Add the code to initialise your global variables here.
ROWS => Number of rows on the board
COLS => Number of columns on the board
STARTX & STARTY => starting point of the turtle.
WIDTH => Width of the Connect 4 board
HEIGHT => Height of the Connect 4 board
RADIUS => Radius of individual coin spot
---
"""
#####################	ADD YOUR CODE HERE	###################

SCREEN = turtle.Screen()
ROWS = 7
COLS = 6
STARTX = -450
STARTY = -450 * (ROWS / COLS)
WIDTH = -2 * STARTX
HEIGHT = -2 * STARTY

BOARD = []
TURN = 1

##############################################################
"""
Purpose:
---
Add your code to the function `draw_rectangle` so that it draws a rectangle on the screen.
x => The x-coordinate to start drawing the rectangle.
y => The y-coordinate to start drawing the rectangle.
w => The width of the rectangle to be drawn.
h => The height of the rectangle to be drawn.
color => The color that is to be filled inside the rectangle.
---
"""
#####################	ADD YOUR CODE HERE	###################
def draw_rectangle(x, y, w, h, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.end_fill()
    SCREEN.update()

##############################################################
"""
Purpose:
---
Add your code to the function `draw_circle` so that it draws a circle on the screen.
x => The x-coordinate to start drawing the circle.
y => The y-coordinate to start drawing the circle.
r => The radius of the circle to be drawn.
color => The color that is to be filled inside the circle.
---
"""
#####################	ADD YOUR CODE HERE	###################
def draw_circle(x, y, r, color):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    SCREEN.update()


##############################################################
#   TODO : Simplify documentation later
"""
Purpose:
---
Add your code to the function `draw_pieces` so that it draws the coin spots on the screen.
board => The board array of the game.
X => X.
Y => Y.
radius => RADIUS.
i => i.
j => j.
---
"""
#####################	ADD YOUR CODE HERE	###################
def draw_pieces(board, X, Y, radius, i, j):
    if board[i][j] == 0:
        draw_circle(X, Y, radius, 'white')
    elif board[i][j] == 1:
        draw_circle(X, Y, radius, 'yellow')
    else:
        draw_circle(X, Y, radius, 'red')

##############################################################
#   TODO : Simplify documentation later
"""
Purpose:
---
Add your code to the function `draw_board` so that it draws the board.
board => The board array of the game.
---
"""
#####################	ADD YOUR CODE HERE	###################
def draw_board(board):
    draw_rectangle(STARTX, STARTY, WIDTH, HEIGHT, 'blue')

    row_gap = HEIGHT / ROWS
    col_gap = WIDTH / COLS
    Y = STARTY + row_gap / 2
    for i in range(ROWS):
        X = STARTX + col_gap / 2
        for j in range(COLS):
            draw_pieces(board, X, Y, (row_gap / 3), i, j)
            X += col_gap
        Y += row_gap

##############################################################
#   TODO : Simplify documentation later
"""
Purpose:
---
Add your code to the function `init_board` so that it initializes the game.
---
"""
#####################	ADD YOUR CODE HERE	###################
def init_board():
    global BOARD, SCREEN

    SCREEN.setup(500, 500)
    SCREEN.setworldcoordinates(-500, -500, 500, 500)
    SCREEN.title("Connect 4")
    SCREEN.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    SCREEN.tracer(0, 0)

    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(0)
        BOARD.append(row)

    draw_board(BOARD)


def place_piece_and_draw(board, col, turn):
    # To place the piece and mark the spot for the player

    for i in range(ROWS):
        if board[i][col] == 0:
            board[i][col] = turn
            row = i
            break

    # Draw the piece that was placed
    row_gap = HEIGHT / ROWS
    col_gap = WIDTH / COLS
    Y = STARTY + row_gap * row + row_gap / 2;
    X = STARTX + col_gap * col + col_gap / 2
    i = row
    j = col
    draw_pieces(board, X, Y, row_gap / 3, i, j)
    return row


##############################################################
"""
Purpose:
---
Add your code to the function `play` which is executed when the onclick event is triggered.
x => The x-coordinate where the mouse was clicked.
y => The y-coordinate where the mouse was clicked.
---
"""
#####################	ADD YOUR CODE HERE	###################
def play(x, y):
    global BOARD, TURN

    cols = [WIDTH / COLS * i + STARTX + (WIDTH / COLS) / 2 for i in range(COLS)]
    for i in range(len(cols)):
        if abs(x - cols[i]) < ((WIDTH / COLS) / 2) * (2 / 3) and BOARD[ROWS - 1][i] == 0:
            row_placed = place_piece_and_draw(BOARD, i, TURN)

            # print("-------")
            # print(BOARD)
            # print(TURN)
            # print(row_placed)
            # print(i)

            result = check_game_over(BOARD, TURN, row_placed, i)
            if result == 0:
                SCREEN.textinput('GAME OVER', 'IT IS A TIE')
            elif result == 1:
                SCREEN.textinput('GAME OVER', 'PLAYER \'YELLOW\' WON')
            elif result == -1:
                SCREEN.textinput('GAME OVER', 'PLAYER \'RED\' WON')
            if result != -2:
                SCREEN.bye()
            TURN = -TURN


##############################################################
#   TODO : Simplify documentation later
"""
Purpose:
---
Add your code to the function `check_game_over` so that it initializes the game.
---
"""
#####################	ADD YOUR CODE HERE	###################
def check_game_over(board, turn, last_row, last_col):
    # Check Horizontals
    cnt = 1
    i = last_col + 1
    while i < COLS and board[last_row][i] == turn:
        cnt = cnt + 1
        i = i + 1

    i = last_col - 1
    while i >= 0 and board[last_row][i] == turn:
        cnt = cnt + 1
        i = i - 1
    if cnt >= 4:
        return turn

    # Check Vertical
    if last_row >= 3 \
            and board[last_row - 1][last_col] == turn \
            and board[last_row - 2][last_col] == turn \
            and board[last_row - 3][last_col] == turn:
        return turn

    # Check Diagonal left to right diagonal
    cnt = 1
    i = 1
    while last_row + i < ROWS \
            and last_col + i < COLS \
            and board[last_row + i][last_col + i] == turn:
        cnt = cnt + 1
        i = i + 1
    i = -1
    while last_row + i >= 0 \
            and last_col + i >= 0 \
            and board[last_row + i][last_col + i] == turn:
        cnt = cnt + 1
        i = i - 1
    if cnt >= 4:
        return turn

    # Check Diagonal right to left diagonal
    cnt = 1
    i = 1
    while last_row + i < ROWS \
            and last_col - i >= 0 \
            and board[last_row + i][last_col - i] == turn:
        cnt = cnt + 1
        i = i + 1
    i = -1
    while last_row + i >= 0 \
            and last_col - i < COLS \
            and board[last_row + i][last_col - i] == turn:
        cnt = cnt + 1
        i = i + 1
    if cnt >= 4:
        return turn

    for i in range(COLS):
        if board[ROWS - 1][i] == 0:
            return -2
    return 0


if __name__ == "__main__":
    init_board()
    SCREEN.onclick(play)
    SCREEN.mainloop()
