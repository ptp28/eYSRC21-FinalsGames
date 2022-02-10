'''
*****************************************************************************************
*
*        		========================================================
*           		e-Yantra School Robotics Competition (eYSRC 2021)
*        		========================================================
*
*  This script is to be used to implement Mini Assignment titled- 'Pacman with Maze'.
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

# Team ID:          63
# 					[ Team-ID ]
# Author List:      
# 					[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:       	2_CT_pacman.py
# Functions:        move_up, move_down, move_left, move_right, movement, enemy_movement, wall_collision_pacman,
#                   wall_pacman_collision_enemy, score_guy, end_good, end_bad

#                   [ Comma separated list of functions in this file ]
#                   print_menu, play_game, change_background, main
# Global variables: 
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are NOT ALLOWED to make any changes in this section. ##
## You have to implement this assignment with the available ##
## modules for this task.								    ##
##############################################################

import turtle
import os
import random
import math
##############################################################

score = 0

maze = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXXE           XX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX       EXX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXXE                    X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXXE                   X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Initializing the screen
wn = turtle.Screen()
wn.tracer(0)
wn.title("e-Yantra School Robotics Competition")
wn.bgcolor('black')
wn.setup(650, 680)


game_over_flag = False

directions = ['up', 'down', 'left', 'right']

colours = ['spring green', 'violet', 'orange red', 'red']

x = -304
y = 285

wall_list = []
wall_cor_list = []

enemy_list = []

food_list = []

enemy_no = 0

# Building the map

for list_index in maze:
    for string_index in list_index:
        if string_index == 'X':
            wall = turtle.Turtle()
            wall.penup()
            wall.shape('square')
            wall.color('blue')
            wall.goto(x, y)
            wall_list.append(wall)
            wall_cor_list.append((wall.xcor(), wall.ycor()))
        elif string_index == 'P':
            pacman = turtle.Turtle()
            pacman.penup()
            pacman.direction = 'stop'
            pacman.shape('circle')
            pacman.color('yellow')
            pacman.goto(x, y)
        elif string_index == 'E':
            pacdot = turtle.Turtle()
            pacdot.penup()
            pacdot.shape('circle')
            pacdot.shapesize(stretch_wid=0.25, stretch_len=0.25)
            pacdot.color('misty rose')
            pacdot.goto(x, y)
            food_list.append(pacdot)

            enemy = turtle.Turtle()
            enemy.penup()
            enemy.shape('square')
            enemy.color(colours[enemy_no])
            enemy.goto(x, y)
            enemy.direction = random.choice(directions)
            enemy_list.append(enemy)
            enemy_no += 1

        elif string_index == ' ':
            pacdot = turtle.Turtle()
            pacdot.penup()
            pacdot.shape('circle')
            pacdot.shapesize(stretch_wid=0.25, stretch_len=0.25)
            pacdot.color('misty rose')
            pacdot.goto(x, y)
            food_list.append(pacdot)

        x += 25
    y -= 25
    x = -304

last_value_x = pacman.xcor()
last_value_y = pacman.ycor()


# Window binding functions
def move_up():
    pacman.direction = 'up'


def move_down():
    pacman.direction = 'down'


def move_left():
    pacman.direction = 'left'


def move_right():
    pacman.direction = 'right'


# Set window bindings
wn.listen()
wn.onkey(move_up, 'w')
wn.onkey(move_down, 's')
wn.onkey(move_left, 'a')
wn.onkey(move_right, 'd')

wn.onkey(move_up, 'Up')
wn.onkey(move_down, 'Down')
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')


# Moving PACMAN
def movement():
    ################# ADD UTILITY LOGIC HERE #########################################
    ## Write appropriate code to check the direction of pacman and move accordingly ##
    ## You can use any logic you want to play this game                             ##
    ##################################################################################
    global last_value_y, last_value_x

    steps = 5

    if pacman.direction == 'up':
        last_value_y = pacman.ycor()
        last_value_x = pacman.xcor()
        pacman.sety(pacman.ycor() + steps)

    if pacman.direction == 'down':
        last_value_y = pacman.ycor()
        last_value_x = pacman.xcor()
        pacman.sety(pacman.ycor() - steps)

    if pacman.direction == 'left':
        last_value_y = pacman.ycor()
        last_value_x = pacman.xcor()
        pacman.setx(pacman.xcor() - steps)

    if pacman.direction == 'right':
        last_value_y = pacman.ycor()
        last_value_x = pacman.xcor()
        pacman.setx(pacman.xcor() + steps)


# Moving the enemy
def enemy_movement():
    steps = 5
    for enemy in enemy_list:
        if enemy.direction == 'up':
            enemy.sety(enemy.ycor() + steps)

        if enemy.direction == 'down':
            enemy.sety(enemy.ycor() - steps)

        if enemy.direction == 'left':
            enemy.setx(enemy.xcor() - steps)

        if enemy.direction == 'right':
            enemy.setx(enemy.xcor() + steps)


# Pacman collision with the wall
def wall_collision_pacman():
    for wall in wall_list:
        if wall.distance(pacman) <= 24:

            pacman.goto(last_value_x, last_value_y)
            pacman.direction = 'stop'


# Enemy collision with pacman or the wall
def wall_pacman_collision_enemy():
    for enemy in enemy_list:
        if enemy.distance(pacman) <= 20:
            end_bad()
        for wall in wall_list:
            if wall.distance(enemy) <= 24:
                if enemy.direction == 'up':
                    enemy.sety(enemy.ycor() - 5)
                    enemy.direction = random.choice(directions)
                elif enemy.direction == 'down':
                    enemy.sety(enemy.ycor() + 5)
                    enemy.direction = random.choice(directions)
                elif enemy.direction == 'right':
                    enemy.setx(enemy.xcor() - 5)
                    enemy.direction = random.choice(directions)
                elif enemy.direction == 'left':
                    enemy.setx(enemy.xcor() + 5)
                    enemy.direction = random.choice(directions)


pen = turtle.Turtle()
end_screen = turtle.Turtle()


# Initializing the score board
def score_guy():
    pen.up()
    pen.hideturtle()
    pen.goto(304, 300)
    pen.color('red')
    pen.write(f'TEAM #63             Score: {score}', align='right', font=('Courier', 25, 'bold'))


# Function for when the player wins
def end_good():
    global game_over_flag

    pen.clear()
    pen.write(f'                     Score: {score}', align='right', font=('Courier', 25, 'bold'))

    end_screen.up()
    end_screen.hideturtle()
    end_screen.color('white')
    end_screen.write(f'!!! You WIN !!!', align='center', font=('Orbitron', 40, 'bold'))
    game_over_flag = True


# Function for when the player touches a ghost
def end_bad():
    global game_over_flag

    pen.clear()
    pen.write(f'                     Score: {score}', align='right', font=('Courier', 25, 'bold'))

    end_screen.up()
    end_screen.hideturtle()
    end_screen.color('white')
    end_screen.write(f'!!! GAME OVER !!!', align='center', font=('Orbitron', 40, 'bold'))
    game_over_flag = True


score_guy()

# Main game loop
while game_over_flag is False:
    wn.update()

    end_screen.hideturtle()

    wall_collision_pacman()
    wall_pacman_collision_enemy()

    for pacdot in food_list:
        if pacman.distance(pacdot) < 20:
            pacdot.goto(600, 600)
            pen.clear()
            pen.write(f'                     Score: {score}', align='right', font=('Courier', 25, 'bold'))
            score += 1

    if score == 249:
        end_good()

    movement()
    enemy_movement()

turtle.exitonclick()
