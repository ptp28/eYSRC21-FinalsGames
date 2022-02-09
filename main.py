"""
Final Sprint Eyantra- eYSRC

Game Name: Pop it!

Playing the game:
- It's a two player game.
- Each player has a cannon.
- You can adjust the aim pointer with the mouse and press the space bar to release the bullet.
- If your bullet hits an opponent's balloon you will either get +10 points or -5 points
- If the explosion ends with a +1 sign, you get +10 points, if it explodes, you get -5 points.
- There are 16 balloons for each player (32 in total) and ten bullets for each player
- The player with higher score after 20 shots wins!

"""

# Name: R Krishna Kanth
# Class: 8
# School: BGS National Public School
# Team-ID: 82


import turtle
import random
import math
import time

# Initializing Variables #
WIDTH = 1200
HEIGHT = 750

TURN = 1

PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

PLAYER1_BULLETS = 10
PLAYER2_BULLETS = 10

PLAYER1_BALLOONS = []
PLAYER2_BALLOONS = []

PLAYER1_PLAYING = False
PLAYER2_PLAYING = False

PLAYER1_SHOOT_POS = (0, 0)
PLAYER2_SHOOT_POS = (0, 0)

GAME_STARTED = False
##############################

####### Registering Shapes ########
turtle.register_shape("logo.gif")
turtle.register_shape("cannon.gif")
turtle.register_shape("cannon_left.gif")
turtle.register_shape("balloon.gif")
turtle.register_shape("balloon1.gif")
turtle.register_shape("bullet.gif")
turtle.register_shape("kaboom.gif")
turtle.register_shape("bullet_count (2).gif")
turtle.register_shape("plus_1.gif")
turtle.register_shape('winner.gif')
##################################

def startGame():
    global GAME_STARTED
    GAME_STARTED = True

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)

turtle.bgpic('bg.gif')
turtle.listen()

logo = turtle.Turtle()
logo.ht()
logo.shape("balloon.gif")
logo.up()
logo.goto(0, 0)

img = turtle.Turtle()
img.shape('logo.gif')
img.goto(0,190)
logo.showturtle()

bal1 = turtle.Turtle()
bal1.speed(0)
bal1.shape('balloon1.gif')
bal1.ht()
bal1.up()
bal1.goto(500, 0)
bal1.showturtle()

bal2 = bal1.clone()
bal2.goto(-500, 0)

while GAME_STARTED == False:
    turtle.up()
    turtle.ht()
    
    turtle.goto(0, -100)
    turtle.write("➜Place the aim pointer accordingly to shoot the opponent's balloons", align="center", font=("Courier New", 20, 'bold'))
    turtle.goto(0, -150)
    turtle.write("➜The balloon that is hit can be a positive one which will award 10 points", align="center", font=("Courier New", 20, 'bold'))
    turtle.goto(0, -170)
    turtle.write("Or a negative one which will decrease 5 points", align="center", font=("Courier New", 20, "bold"))
    turtle.goto(0, -210)
    turtle.write("➜Both players have ten bullets each. Player with higher score wins", align="center", font=("Courier New", 20, "bold"))
    turtle.goto(0, 320)
    turtle.write("Click on n to start the game", align="center", font=("Courier New", 30, "bold"))
    
    screen.onkey(startGame, 'n')

turtle.clear()

logo.ht()
img.ht()
bal1.ht()
bal2.ht()
loading = turtle.Turtle()
loading.up()
loading.goto(0, -300)
loading.write("Preparing Game", align="center", font=("Comic Sans", 30, 'normal'))
###########################



# Drawing the division line
turtle.down()
turtle.goto(0,0)
turtle.setheading(90)
turtle.forward(HEIGHT//2)
turtle.right(180)
turtle.forward(HEIGHT)
##########################

turtle.speed(0)
turtle.up()

# Placing the right cannon
player1 = turtle.Turtle()
player1.up()
player1.speed(0)
player1.shape('cannon.gif')
player1.goto(-450, -200)
##########################

# Placing the left cannon
player2 = turtle.Turtle()
player2.up()
player2.speed(0)
player2.shape('cannon_left.gif')
player2.goto(450, -200)
########################


def setup_balloons():
    """
    This will create all the balloons place them in a 4*4 grid for the
    players and add them to PLAYER1_BALLOONS and PLAYER2_BALLOONS
    and randomly assign balloons a reward of -1 or 1
    """
    global PLAYER1_BALLOONS, PLAYER2_BALLOONS

    for x in range(4):  # Placing Balloons in a 4*4 grid
        for j in range(-1, 3):
            balloon = turtle.Turtle()
            balloon.up()
            balloon.speed(10)
            balloon.shape('balloon1.gif')
            balloon.goto(-x * 100 - 200, j * 100 + 70)
            PLAYER1_BALLOONS.append(balloon)

    # Assigning rewards randomly
    random.shuffle(PLAYER1_BALLOONS)
    for balloon in PLAYER1_BALLOONS[:8]:
        balloon.reward = -5
    for balloon in PLAYER1_BALLOONS[8:]:
        balloon.reward = 10

    for x in range(4):  # Placing Balloons in a 4*4 grid
        for j in range(-1, 3):
            balloon = turtle.Turtle()
            balloon.up()
            balloon.speed(10)
            balloon.shape('balloon1.gif')
            balloon.goto(x * 100 + 200, j * 100 + 70)
            PLAYER2_BALLOONS.append(balloon)

    # Assigning rewards randomly
    random.shuffle(PLAYER2_BALLOONS)
    for balloon in PLAYER2_BALLOONS[:8]:
        balloon.reward = -5
    for balloon in PLAYER2_BALLOONS[8:]:
        balloon.reward = 10


setup_balloons()
ray = turtle.Turtle()
ray.speed(0)

# Displaying bullet count status for both players
bullets1 = []
bullets2 = []
for i in range(10):
    b = turtle.Turtle()
    b.up()
    b.speed(10)
    b.shape('bullet_count (2).gif')
    b.goto(-300 + i * 20, -325)
    bullets1.append(b)

for i in range(10):
    b = turtle.Turtle()
    b.up()
    b.speed(10)
    b.shape('bullet_count (2).gif')
    b.goto(100 + i * 20, -325)
    bullets2.append(b)
#################################

score = turtle.Turtle()


def display_stats() -> None:
    """
    Prints the scores for both players at the top of the screen
    Updates the bullet count state
    """
    for o in range(10 - PLAYER1_BULLETS):
        bullets1[o].ht()

    for o in range(10 - PLAYER2_BULLETS):
        bullets2[o].ht()

    score.up()
    score.clear()
    score.speed(0)
    # Printing Player1 and Player2 at the top of the screen
    score.goto(-WIDTH // 4, 320)
    score.write(f'PLAYER 1; Score: {PLAYER_1_SCORE}', align="center", font=("Courier New", 30, "normal"))
    score.goto(WIDTH // 4, 320)
    score.write(f'PLAYER 2; Score: {PLAYER_2_SCORE}', align="center", font=("Courier New", 30, "normal"))


def slope_to_angle(y2: float, y1: float, x2: float, x1: float) -> float:
    # This function calculates the slope and returns the angle of inclination
    """

         a
        /|
       / |
      /  |
     /θ  |
    b----c

    c = 90
    so given the slope, we can find the angle by using math.atan (tan^-1)

    tan(θ) = opposite/adjacent = ca/cb
    m = slope of ba
    θ = tan^-1(m)

    :return float -> The angle of inclination of slope
    """

    slope = (y2 - y1) / (x2 - x1)   # Slope formula
    theta = math.atan(slope)        # tan^-1(slope) = angle
    return theta * (180 / math.pi)  # Convert from radians to degree


def display_ray(_: float, y: float) -> None:
    """
    Displays a ray from the cannon through the user's mouse pos
    to enable precise aiming.

    By default, the y and x are 0, the user can influence the y axis with the mouse click

    The ray is only displayed till the user's half of the screen to make the game challenging

    :param _: float -> The x axis value of the click
    :param y: float -> The y axis value of the click
    """
    global PLAYER1_SHOOT_POS, PLAYER2_SHOOT_POS

    ray.up()
    ray.clear()
    ray.ht()
    ray.pencolor('blue')

    if TURN == 1:
        ray.goto(player1.pos())
        PLAYER1_SHOOT_POS = (0, y)
    else:
        ray.goto(player2.pos())
        PLAYER2_SHOOT_POS = (0, y)

    ray.down()
    ray.goto(0, y)

def do_nothing(x=None, y=None) -> None:
    """
    Empty Function to remove all keypress and screenclick listeners
    """
    pass

def game_over() -> None:
    """
    Game Over function
    Displays final scores
    """
    turtle.up()
    turtle.goto(0, 100)
    turtle.write("Final Score", align="center", font=("Courier New", 30, 'bold'))
    turtle.goto(0, 0)
    turtle.write(
        f"PLAYER1 SCORE: {PLAYER_1_SCORE}; PLAYER2 SCORE: {PLAYER_2_SCORE}", 
        align="center", 
        font=("Courier New", 20, "normal")
    )
    winner = turtle.Turtle()
    winner.shape('winner.gif')
    winner.up()
    if PLAYER_1_SCORE > PLAYER_2_SCORE:
        winner.goto(player1.pos())
    elif PLAYER_1_SCORE < PLAYER_2_SCORE:
        winner.goto(player2.pos())
    else:
        turtle.goto(0, -100)
        turtle.write(
        f"It's a tie", 
        align="center", 
        font=("Courier New", 20, "normal")
    )
    # Removing KeyBinds
    turtle.onkey(do_nothing, 'space')
    turtle.onkey(do_nothing, 'n')
    screen.onclick(do_nothing)


def shoot() -> None:
    """
    Function triggered when the user clicks on the space bar

    Shoots the bullets, and the check for collisions and award scores.
    """
    global TURN, PLAYER1_PLAYING, PLAYER2_PLAYING, PLAYER1_BULLETS, PLAYER2_BULLETS, \
        PLAYER_1_SCORE, PLAYER_2_SCORE, GAME_STARTED


    # Checking if the player is pressing the space bar more than one time per turn
    # To make the game robust and preventing spamming of space bar
    if (TURN == 1 and PLAYER1_PLAYING) or (TURN == 2 and PLAYER2_PLAYING):
        return

    PLAYER1_PLAYING = TURN == 1
    PLAYER2_PLAYING = TURN == 2

    # Explosion animation
    explosion = turtle.Turtle()
    explosion.up()
    explosion.ht()
    explosion.shape('kaboom.gif')
    #######################

    # Plus1 animation #
    plus1 = turtle.Turtle()
    plus1.up()
    plus1.ht()
    plus1.shape('plus_1.gif')
    ####################

    ray.ht()

    bullet = turtle.Turtle()
    bullet.ht()
    bullet.shape('circle')
    bullet.turtlesize(5)
    bullet.up()
    bullet.setheading(0)

    if TURN == 1:
        bullet.goto(player1.pos())
        angle = slope_to_angle(PLAYER1_SHOOT_POS[1], player1.ycor(), PLAYER1_SHOOT_POS[0], player1.xcor())
        bullet.left(angle)
        PLAYER1_BULLETS -= 1
    else:
        # Rotating the cannon bullet according to the ray aim adjusted by the user
        bullet.setheading(180)
        bullet.goto(player2.pos())
        angle = slope_to_angle(PLAYER2_SHOOT_POS[1], player1.ycor(), PLAYER2_SHOOT_POS[0], player1.xcor())
        bullet.right(angle)
        PLAYER2_BULLETS -= 1

    bullet.showturtle()

    run = True
    while run:
        burst = False
        bullet.forward(10)

        if TURN == 1:
            PLAYER1_PLAYING = True
            to_delete = []
            for balloon in PLAYER2_BALLOONS:
                # Checking for collision between bullet and balloon
                if abs(bullet.xcor() - balloon.xcor()) < 80 and abs(bullet.ycor() - balloon.ycor()) < 80:
                    PLAYER_1_SCORE += balloon.reward
                    if balloon.reward > 0:
                        plus1.goto(balloon.pos())
                        plus1.showturtle()
                    else:
                        explosion.goto(balloon.pos())
                        explosion.showturtle()
                    bullet.ht()

                    time.sleep(0.2)
                    balloon.ht()
                    to_delete.append(balloon)
                    burst = True

            # Deleting collided balloons
            for item in to_delete:
                PLAYER2_BALLOONS.remove(item)

        elif TURN == 2:
            PLAYER2_PLAYING = True
            to_delete = []
            for balloon in PLAYER1_BALLOONS:
                # Checking for collision between bullet and balloon
                if abs(balloon.xcor() - bullet.xcor()) < 80 and abs(balloon.ycor() - bullet.ycor()) < 80:
                    PLAYER_2_SCORE += balloon.reward
                    bullet.ht()
                    # Checking if balloon is a positive or negative one
                    if balloon.reward > 0:
                        plus1.goto(balloon.pos())
                        plus1.showturtle()
                    else:
                        explosion.goto(balloon.pos())
                        explosion.showturtle()

                    time.sleep(0.2)
                    balloon.ht()
                    to_delete.append(balloon)
                    burst = True

            for item in to_delete:  # Deleting all balloons that have been hit
                PLAYER1_BALLOONS.remove(item)

        # Checking if the bullet has hit a balloon or gone out of the screen
        if bullet.xcor() > 1000 or burst or bullet.xcor() < -1000:
            run = False
            bullet.ht()

    # Alternating turns between the player
    if TURN == 1:
        TURN = 2
        PLAYER1_PLAYING = False

    elif TURN == 2:
        TURN = 1
        PLAYER2_PLAYING = False
    ######################################

    # Hiding the explosion and updating score
    explosion.ht()
    plus1.ht()
    display_ray(0, 0)
    display_stats()
    #########################################

    # Checking if all bullets for both players are used
    if PLAYER1_BULLETS == 0 and PLAYER2_BULLETS == 0:
        game_over()


loading.clear()

display_ray(0, 0)
display_stats()

screen.onclick(display_ray)  # Draws the shooting ray for precise aim on click event
screen.listen()  # Listen for key presses
screen.onkey(shoot, 'space')  # Shoots the bullet on pressing space bar

turtle.mainloop()
