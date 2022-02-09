

'''
Initialising all the necessary modules
'''
import turtle # Modules used for drawing the game
import math # This modules is used for mathematics
import random # Modules used for getting random values
import playsound # Modules used for playing sound
# | = }
if __name__ == '__main__': # Run the code when the py file is called
    def int_screen(): # Initialisting the screen
        turtle.tracer(0)
        global screen # Making the screen object as global variable
        screen = turtle.Screen() # Making a screen object for control the screen
        screen.title("Space Invaders 1") # Setting the screen title
        screen.bgpic("space4.gif") # Setting the background colour
        screen.setup(800,650) # Setting the screen size

        turtle.register_shape("ufo_real.gif")  # Register the shape
        turtle.register_shape("bullet.gif")
        turtle.register_shape("rocket ship.gif")
    def draw_border(): # Drawing border

        border_pen = turtle.Turtle() # making a pen to draw a border
        border_pen.speed(0) # speed to maximum
        border_pen.color("white")
        border_pen.penup()
        border_pen.setposition(-300, -300)
        border_pen.pendown()
        border_pen.pensize(3)
        for side in range(4):
            border_pen.fd(600) # moving forward to 600 pixel
            border_pen.lt(90) # moving left
        border_pen.hideturtle() # hiding the turtle


    def int_draw_pen(): # Initialising the score pen

        global score_pen # Initialising the score variable
        score_pen = turtle.Turtle() # Making a draw pen object for draw the score
        score_pen.speed(0) # speed to maximum
        score_pen.color("red")
        score_pen.penup()
        score_pen.setposition(-20, 260)

        score_pen.write("Score:0  High score:0", False, align="left", font=("Arial", 14, "normal")) # drawing the highe score as 0
        score_pen.hideturtle() # hiding the turtle
    def int_player(): # Initialising the player
        global player,playerspeed # Making the player and playerspeed as global variable

        player = turtle.Turtle() # Making a player object for playing

        player.shape("rocket ship.gif") # setting the player shape as rocket
        player.penup()
        player.speed(0)
        player.setposition(0, -250) # setting the player position
        player.setheading(90)
        playerspeed = 15 # setting the player speed
    def int_enemies(): # Initialising the enemies
        global enemy,enemyspeed,enemies # Making the enemy,enemyspeed,enemies as global variable

        number_of_enemies = 5 # setting the number of enemies
        enemies = [] # creating the list for storing the enemies object

        for i in range(number_of_enemies):
            # create the enemy
            enemies.append(turtle.Turtle())#Apending all enemy object to the list

        for enemy in enemies: # iterating all the enemy object in enemies list
            enemy.shape("ufo_real.gif") # setting the shape
            enemy.penup()
            enemy.speed(0) # speed to maximum
            x = random.randint(-200, 200) # getting random values for x
            y = random.randint(100, 250) # getting random values for y
            enemy.setposition(x, y) # going to x,y position

        enemyspeed = 1 # setting the enemy speed
    def int_missel(n): # function for intialising missile
        global missiles # making a missile as global variable

        missiles = [] # creating a list for storing the missiles

        for i in range(n):
            missile = turtle.Turtle() # creating the missile object
            missile.color("blue")
            missile.shape("bullet.gif")
            missile.speed = 1
            missile.state = "ready" # setting the missile state to ready
            missile.hideturtle() # hide the missile turtle
            missile.penup()
            missile.goto(1000,1000)
            missile.shapesize(1, 2, 1)
            missiles.append(missile) # appending the missiles object to list
    int_screen() # calling the int screen function
    score = 0 # intialising the score
    high_score = 0 # intialising the high score
    draw_border() # calling the border function
    int_draw_pen() # calling the int draw pen function
    int_enemies() # calling the int enemies function
    int_player() # calling the int player function
    int_missel(5) # calling the int missel function
    playsound.playsound('Game_start.mp3') #playing the sound

    def move_left(): # Move the player to left
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = -280
        player.setx(x)


    def move_right(): # Move the player to right
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)


    def f_missile(): # firing the missile
        for missile in missiles: # iterating all the missile object in missiles list
            if missile.state == "ready":
                missile.goto(player.xcor(), player.ycor()+10)
                missile.showturtle()
                missile.setheading(player.heading())
                missile.state = "fire"
                break

    screen.listen() # listening to the keyboard command
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.onkey(f_missile, "space")
    Game_Over = False
    while True:
        turtle.update() # updating the screen
        for missile in missiles: # iterating all the missile object in missiles list
            if missile.state == "fire": # check if missile state is Fire
                missile.fd(missile.speed) # move forward the missile speed
            if missile.xcor() > 400 or missile.xcor() < -400 or missile.ycor() > 300 or missile.ycor() < -300:# Check if missile as hit the boader
                missile.hideturtle() # |
                missile.goto(1000,1000)# |
                missile.state = "ready"#| reseting the missile
        for enemy in enemies: # iterating all the enemy object in enemies list
            x = enemy.xcor() # Get the xcor
            x += enemyspeed # Adding the xcor by the speed
            enemy.setx(x) # going to x coordinate

            if enemy.xcor() > 270:#Check if enemy as hit the boader
                for enemys in enemies:
                    y = enemys.ycor()# Get the ycor
                    y -= 40 # Subtracting the xcor by the speed
                    enemys.sety(y) # going to y coordinate
                    if enemys.ycor() < -285 and Game_Over == False:
                        enemys.hideturtle() # hide the enemy turtle

                        x = random.randint(-200, 200) # getting random values for x
                        y = random.randint(100, 250)# getting random values for y
                        enemys.setposition(x, y) # going to x,y position
                        enemys.showturtle() # Showing the turtle

                    enemyspeed *= -1 # Changing the enemy direction

            if enemy.xcor() < -270:#Check if enemy as hit the boader

                for enemys in enemies:
                    y = enemys.ycor()# Get the ycor
                    y -= 40  # Subtracting the xcor by the speed
                    enemys.sety(y) # going to y coordinate
                    if enemys.ycor() < -285  and Game_Over == False:
                        enemys.hideturtle()# hide the enemy turtle

                        x = random.randint(-200, 200) # getting random values for x
                        y = random.randint(100, 250)# getting random values for y
                        enemys.setposition(x, y) # going to x,y position
                        enemys.showturtle() # Showing the turtle

                    enemyspeed *= -1 # Changing the enemy direction


            for missile in missiles:
                if missile.distance(enemy)<60: # check for a collision between the bullet and the enemy
                    playsound.playsound('hit_2_sound.mp3',False) # playing the song
                    #Reseting the missile
                    # missile.goto(600, 600)
                    missile.hideturtle()
                    missile.goto(1000, 1000)
                    missile.state = "ready"
                    # Reseting the enemy
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    enemy.setposition(x, y)

                    # update the score
                    score += 10
                    if score > high_score:  # Checking if score is the highest sore
                        high_score = score  #

                    score_pen.clear()
                    score_pen.write(f'Score:{score}  High score:{high_score}', False, align="left", font=("Arial", 14, "normal"))
            if score == 80:
                score_pen.color("white")
            if score == 0:
                score_pen.color("red")

            if player.distance(enemy)<100: #  check for a collision between the player and enemy
                Game_Over = True
            if Game_Over == True:
                repeat = screen.textinput("Game over!", "Type yes or no to play again") # Replay dialogbox

                while not repeat: # if nothing as been typed but as pressed enter then ask the dialog box again.
                    if not repeat:
                        repeat = screen.textinput("Game over!", "type yes or no to play again")
                if repeat == 'yes': # If answer yes
                    Game_Over = False
                    screen.listen() # listening to keyboard command
                    score = 0 # reset the score

                    score_pen.clear()
                    score_pen.write(f'Score:{score}  High score:{high_score}', False, align="left", font=("Arial", 14, "normal")) # writing the reset score
                    # Reseting the missile
                    for missile in missiles:
                        missile.goto(600, 600)
                        missile.hideturtle()
                        missile.state = "ready"
                    # Reseting the enemy
                    for enemy in enemies:
                        x = random.randint(-200, 200)
                        y = random.randint(100, 250)
                        enemy.setposition(x, y)
                if repeat == 'no': # If answer no
                    screen.bye() #closing the screen
                    break# break out of the while loop
                    exit() # exit the code

