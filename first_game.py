
def game():
    import turtle
    import time
    import random
    import playsound

    delay = 0.1
    level = 1

    # Score
    score =  0  # Creating a variable for score
    high_score = 0  # Creating a variable for high score
    def int_screen():# intialising

        global screen,screen_width,screen_height
        screen = turtle.Screen()  # creating an object for screen
        screen.title("Planet Explorer")  # setting the title as eysrc
        screen.bgcolor("black")  # change the background to black
        screen.setup(width=1000, height=600)  # setting the screen width and height
        screen.tracer(0)  # Turns off the screen updates
        screen.register_shape('./Assets/rocket _up.gif')  # registering the shape
        # screen.register_shape('rocket tail.gif')  # registering the shape
        # screen.register_shape('tran.gif')  # registering the shape
        screen.register_shape('./Assets/ufotrail.gif')  # registering the shape
        screen.register_shape('./Assets/ufo.gif')  # registering the shape
        screen.register_shape('./Assets/rocket left.gif')  # registering the shape
        screen.register_shape('./Assets/rocket right.gif')  # registering the shape
        screen.register_shape('./Assets/rocket down.gif')  # registering the shape
        screen.register_shape('./Assets/asteroid1.gif')  # registering the shape
        screen.register_shape('./Assets/winner (2).gif')  # registering the shape
        screen.register_shape('./Assets/start_image.gif')  # registering the shape

        # screen.register_shape('rocket-space-launch-project-start-up-flying-cartoon-vector-illustration-isolated-white-background-127571950.gif')  # registering the shape

        screen.register_shape('./Assets/mars.gif')  # registering the shape
        screen.register_shape('./Assets/jupiter.gif')  # registering the shape

        # screen.register_shape('restart button.gif')  # registering the shape

        screen.register_shape('./Assets/neptune.gif')

        screen.register_shape('./Assets/venus.gif')  # registering the shape
        screen_width = 860  # setting a variable for screen width
        screen_height = 460  # setting a variable for screen heigh
        # Sleeping for 8 sec
        screen.bgpic('./Assets/space4.gif')  # changing the background image

    def int_player(): # intilising the player
        global player
        player = turtle.Turtle()  # creating an object for player
        player.speed(0)  # setting the speed to maximum
        player.shape("./Assets/rocket _up.gif")  # changing the shape
        player.color("grey")  # setting the colour as grey
        player.penup()  # stop writing on the screen

        player.goto(0, 0)
        player.direction = "stop"  # setting the direction as stop


    def goal():

        global planet,planet1,planet2,planet3
        planet = turtle.Turtle()  # creating a object for planet
        planet.speed(0)  # setting the speed as maximum
        planet.shape('./Assets/mars.gif')  # setting the shape
        planet.color("red")  # setting the colour as red
        planet.penup()
        planet.goto(0, 100)

        planet1 = turtle.Turtle()  # creating a object for planet1
        planet1.speed(0)  # setting the speed as maximum
        planet1.shape("./Assets/jupiter.gif")  # setting the shape
        planet1.color("red")  # setting the colour as red
        planet1.penup()
        x = random.randint(-int(screen_width / 2), int(screen_width / 2))  # getting random values under the screen width
        y = random.randint(-int(screen_height / 2), int(screen_height / 2))  # getting random values under the screen height
        planet1.goto(x, y)  # going to the random position

        planet2 = turtle.Turtle()  # creating a object for planet2
        planet2.speed(0)  # setting the speed as maximum
        planet2.shape('./Assets/venus.gif')  # setting the shape
        planet2.color("red")  # setting the colour as red
        planet2.penup()
        x = random.randint(-int(screen_width / 2), int(screen_width / 2))  # getting random values under the screen width
        y = random.randint(-int(screen_height / 2), int(screen_height / 2))  # getting random values under the screen height
        planet2.goto(x, y)  # going to the random position

        planet3 = turtle.Turtle()  # creating a object for planet3
        planet3.speed(0)  # setting the speed as maximum
        planet3.shape('./Assets/neptune.gif')  # setting the shape
        planet3.color("red")  # setting the colour as red
        planet3.penup()
        x = random.randint(-int(screen_width / 2), int(screen_width / 2))  # getting random values under the screen width
        y = random.randint(-int(screen_height / 2), int(screen_height / 2))  # getting random values under the screen height
        planet3.goto(x, y)  # going to the random position
    def int_winer_screen(): # intilising the winner
        global winner
        winner = turtle.Turtle()  # creating a object for planet
        winner.speed(0)  # setting the speed as maximum
        winner.shape('./Assets/winner (2).gif')  # setting the shape
        winner.color("red")  # setting the colour as red
        winner.penup()

        winner.hideturtle()
    def int_obstacle(): # intilising the obstacle
        global obstacle,obstacle2
        obstacle = turtle.Turtle()  # creating a object for obstacle
        obstacle.speed(0)  # setting the speed as maximum
        obstacle.shape("./Assets/ufotrail.gif")  # setting the shape as square
        obstacle.shapesize(1, random.randint(5, 8), 1)  # increasing the width of square
        obstacle.color("red")  # setting the colour as red
        obstacle.penup()
        obstacle.speed = random.randint(10, 25)
        x = random.randint(90,220)
        # y = random.randint(-int(screen_height / 2), int(screen_height / 2))
        obstacle.goto(x, 240)  # going to the random position

        obstacle2 = turtle.Turtle()  # creating a object for obstacle2
        obstacle2.speed(0)  # setting the speed as maximum
        obstacle2.shape("./Assets/ufotrail.gif")  # setting the shape
        obstacle2.shapesize(1, 10, 1)  # increasing the width
        obstacle2.color("green")  # setting the colour as green
        obstacle2.penup()
        obstacle2.speed = random.randint(10, 25)
        x = random.randint(-220,90)

        obstacle2.goto(x, -240)  # going to the random position

    def int_pen():
        # Pen
        global pen
        pen = turtle.Turtle()  # creating a object for writing
        pen.speed(0)  # setting the speed as maximum
        pen.shape("square")  # setting the shape as square
        pen.color("white")  # setting the colour as red
        pen.penup()
        pen.hideturtle()  # hiding the turtle
        pen.goto(0, 260)
        pen.write("Score: 0  High Score: 0  Level: 1", align="center", font=("Courier", 16, "normal"))  # writing the score and level
    def int_ufo():
        global ufo,ufo1
        ufo = turtle.Turtle()  # creating a object for obstacle
        ufo.speed(3)
        ufo.penup()
        ufo.shape('./Assets/ufo.gif')
        ufo.goto(-300, -240)
        # ufo.stamp()
        ufo1 = turtle.Turtle()  # creating a object for obstacle
        ufo1.speed(3)
        ufo1.penup()
        ufo1.shape('./Assets/ufo.gif')
        ufo1.goto(300, 240)

    def int_asteroid():
        global asteroid, asteroid1
        asteroid = turtle.Turtle()  # creating a object for asteroid
        asteroid.speed(3)
        asteroid.penup()
        asteroid.shape('./Assets/asteroid1.gif')
        asteroid.hideturtle()
        asteroid.goto(1100,900)

        asteroid1 = turtle.Turtle()  # creating a object for asteroid
        asteroid1.speed(3)
        asteroid1.penup()
        asteroid1.shape('./Assets/asteroid1.gif')
        asteroid1.hideturtle()
        asteroid1.goto(1100,900)
    def int_start():
        start = turtle.Turtle()  # creating a object for start
        # start.speed(3)
        start.penup()
        start.shape('./Assets/start_image.gif')
        start.penup()
        start.showturtle()
        # start.stamp()
        turtle.update()
        playsound.playsound('./Assets/Game_start.mp3',False)
        time.sleep(2)
        start.hideturtle()
        start.clear()
    # calling all the function
    int_screen()
    int_player()
    int_obstacle()
    int_asteroid()
    int_pen()
    int_winer_screen()
    goal()
    int_ufo()
    int_start()

    def go_up():  # creating a function to move up
        if player.direction != "down":
            player.direction = "up"  # changing the direction to up

    def go_up_left():  # creating a function to move up
        if player.direction != "down":
            player.direction = "up_left"  #

    def go_up_right():  # creating a function to move up
        if player.direction != "down":
            player.direction = "up_right"  #
    def go_down():  # creating a function to move down
        if player.direction != "up":
            player.direction = "down"  # changing the direction to down

    def go_down_right():  # creating a function to move up
        if player.direction != "up":
            player.direction = "down_right"
    def go_down_left():  # creating a function to move up
        if player.direction != "up":
            player.direction = "down_left"
    def go_left():  # creating a function to move left
        if player.direction != "right":
            player.direction = "left"  # changing the direction to left


    def go_right():  # creating a function to move right
        if player.direction != "left":
            player.direction = "right"  # changing the direction to right


    def move():  # creating a function for moving
        if player.direction == "up":  # check if player direction equals up
            # player.shape('snake_head_down.gif')
            player.shape('./Assets/rocket _up.gif')
            # for segment in segments:  # hiding the turtles
            #     segment.shape('rocket tail.gif')
            player.setheading(0)
            y = player.ycor()# getting the turtle y cordinate
            player.sety(y + 20)  # moving up
        if player.direction == 'up_left': # check if player direction equals up
            player.setheading(40)

            y = player.ycor() # getting the turtle y cordinate
            x = player.xcor()
            player.sety(y + 20)# moving up
            player.setx(x - 20)
        if player.direction == 'up_right':  # check if player direction equals up

            player.setheading(340)

            y = player.ycor()  # getting the turtle y cordinate
            x = player.xcor()
            player.sety(y + 20)  # moving up
            player.setx(x + 20)
        if player.direction == 'down_right':  # check if player direction equals up
            player.setheading(150)

            y = player.ycor()  # getting the turtle y cordinate
            x = player.xcor()
            player.sety(y - 20)  # moving up
            player.setx(x - 20)
        if player.direction == 'down_left':  # check if player direction equals up
            player.setheading(-150)

            y = player.ycor()  # getting the turtle y cordinate
            x = player.xcor()
            player.sety(y - 20)  # moving up
            player.setx(x + 20)
        if player.direction == "down":  # check if player direction equals down
            # player.shape("snake_head_up.gif")
            player.shape('./Assets/rocket down.gif')  # registering the shape
            player.settiltangle(180)


            y = player.ycor()  # getting the turtle y cordinate
            player.sety(y - 20)  # moving down
        if player.direction == "left":  # check if player direction equals left
              # registering the shape
            player.shape('./Assets/rocket right.gif')
            player.settiltangle(-90)

            x = player.xcor()  # getting the turtle x cordinate
            player.setx(x - 20)  # moving left
        if player.direction == "right":
            player.shape('./Assets/rocket left.gif')# check if player direction equals right
            # player.shape('snake_head_left.gif')

            player.setheading(90)

            x = player.xcor()  # getting the turtle x cordinate
            player.setx(x + 20)  # moving right


    time_used = 0  # creating a variable for halting



    if time_used == 0:  # check if it has not been halted
        screen.listen()  # getting the what key is pressed
        screen.onkeypress(go_up_left, "q")  # check if up arrow is pressed
        screen.onkeypress(go_up_right, "w")  # check if up arrow is pressed
        screen.onkeypress(go_down_right, "a")  # check if up arrow is pressed
        screen.onkeypress(go_down_left, "s")  # check if up arrow is pressed
        screen.onkeypress(go_up, "Up")  # check if up arrow is pressed
        screen.onkeypress(go_down, "Down")  # check if down arrow is pressed
        screen.onkeypress(go_left, "Left")  # check if left arrow is pressed
        screen.onkeypress(go_right, "Right")  # check if right arrow is pressed








    ufo_foward_or_backward = 1
    ufo1_foward_or_backward = 1
    end_loop = 0
    # Main game loop
    while True:
        screen.update()  # updating the screen

        rand = random.randint(40,100)
        if score == rand:

            asteroid.showturtle()
            x = random.randint(int(player.xcor()) + random.randint(30, 50),
                               int(player.xcor()) + random.randint(150, 200))  # getting random values under the screen width
            y = random.randint(int(player.ycor()),
                               (int(player.ycor()) + random.randint(150, 200)))
            asteroid.goto(x, y)
        if score == rand+5:
            asteroid.hideturtle()
            asteroid.goto(1100,900)
        rand2=random.randint(150, 250)
        if score == rand2:
            asteroid.showturtle()
            x = random.randint(int(player.xcor()) + random.randint(30, 50),
                               int(player.xcor()) + random.randint(150, 200)) # getting random values under the screen width
            y = random.randint(int(player.ycor()),
                               int(player.ycor()) + random.randint(150, 200))
            asteroid.goto(x, y)
        if score == rand2+5:
            asteroid.hideturtle()
            asteroid.goto(1100,900)
        rand = random.randint(40, 100)
        #second asteroid
        if score == rand:

            asteroid1.showturtle()
            x = random.randint(int(player.xcor()),
                               int(player.xcor()) + random.randint(150, 200))  # getting random values under the screen width
            y = random.randint(int(player.ycor()),
                               (int(player.ycor()) + random.randint(150, 200)))
            asteroid1.goto(x, y)
        if score == rand+5:
            asteroid1.hideturtle()
            asteroid1.goto(1100,900)
        rand2 = random.randint(150, 250)
        if score == rand2:
            asteroid1.showturtle()
            x = random.randint(int(player.xcor()),
                               int(player.xcor()) + random.randint(150, 200))  # getting random values under the screen width
            y = random.randint(int(player.ycor()),
                               int(player.ycor()) + random.randint(150, 200))
            asteroid1.goto(x, y)
        if score == rand2+5:
            asteroid1.hideturtle()
            asteroid1.goto(1100,900)

        if time_used == 0:
            screen.listen()
        if ufo_foward_or_backward == 1:
            ufo_x = ufo.xcor()  # getting the y coordinate
            ufo_x += ufo.speed()
            ufo.setx(ufo_x)
            # print(ufo.xcor())

        if ufo_foward_or_backward == 2:
            ufo_x = ufo.xcor()  # getting the y coordinate
            ufo_x -= ufo.speed()
            ufo.setx(ufo_x)



        if ufo.xcor() ==-470 or ufo.xcor() ==-471 :  # moving the ufo back to the screen

            ufo_foward_or_backward = 1


        if ufo.xcor() == -270 :  # moving the ufo back to the screen

            ufo_foward_or_backward = 2

        if ufo1_foward_or_backward == 1:
            ufo1_x = ufo1.xcor()  # getting the y coordinate
            ufo1_x += ufo1.speed()
            ufo1.setx(ufo1_x)


        if ufo1_foward_or_backward == 2:
            ufo1_x = ufo1.xcor()  # getting the y coordinate
            ufo1_x -= ufo1.speed()
            ufo1.setx(ufo1_x)



        if ufo1.xcor() ==470 or ufo1.xcor() ==471 :  # moving the ufo back to the screen

            ufo1_foward_or_backward = 2


        if ufo1.xcor() == 270 :  # moving the ufo back to the screen

            ufo1_foward_or_backward = 1


        t_x = obstacle.xcor()  # getting the y coordinate
        t_x -= obstacle.speed
        obstacle.setx(t_x)  # moving the obstacle
        if obstacle.xcor() <= -800 :  # moving the obstacle back to the screen
            obstacle.setx(ufo1.xcor())
            obstacle.speed = random.randint(10, 25)
        t1_x = obstacle2.xcor()  # getting the y coordinate
        t1_x += obstacle2.speed
        obstacle2.setx(t1_x)  # moving the obstacle2
        if obstacle2.xcor() >= random.randint(700, 1000):  # moving the obstacle2 back to the screen
            obstacle2.setx(ufo.xcor())
            obstacle2.speed = random.randint(10,25)


        if player.xcor() > 550 or player.xcor() < -550 or player.ycor() > 290 or player.ycor() < -290:
            time.sleep(1)  # sleeping for 1 second
            player.goto(0, 0)  # resetting the position
            player.shape("./Assets/rocket _up.gif")
            player.direction = "stop"  # making the turtle to stop


            score = 0


            # Reset the delay
            delay = 0.1

            x = random.randint(-int(screen_width / 2),
                                int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                                int(screen_height / 2))  # getting random values under the screen height
            planet2.goto(x, y)

            x = random.randint(-int(screen_width / 2),
                                   int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                                   int(screen_height / 2))  # getting random values under the screen height
            planet1.goto(x, y)

            x = random.randint(-int(screen_width / 2),
                                   int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                                   int(screen_height / 2))  # getting random values under the screen height
            planet3.goto(x, y)
            # Reset level1_use
            level1_use = 1
            # Reset level
            level = 1
            pen.up()
            pen.goto(-10, 0)
            pen.down()
            pen.clear()



            pen.write("Game Over !!", align="center",
                          font=("Courier", 35, "normal"))  # printing game over
            time.sleep(1)
            playsound.playsound('./Assets/laser_hit.wav',False)

            repeat = screen.textinput("Game over!", "type yes or no to play again")
            while not repeat:
                if not repeat:
                    repeat = screen.textinput("Game over!,type yes or no to play again")
            if repeat == 'yes':

                asteroid.hideturtle()
                asteroid.goto(1100, 900)
                asteroid1.hideturtle()
                asteroid1.goto(1100, 900)

                # grid.clear()
                pen.color('white')
                pen.up()
                pen.goto(0, 260)
                pen.down()
                pen.clear()
                pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                              font=("Courier", 16, "normal"))  # resetting the score

            else:
                end_loop = 1
                screen.bye()

        if player.distance(asteroid) < 63 or player.distance(asteroid1) < 63 or player.distance(ufo1)<74 or player.distance(ufo)<74:
            time.sleep(1)  # sleeping for 1 second
            player.goto(0, 0)  # resetting the position
            player.shape("./Assets/rocket _up.gif")
            player.direction = "stop"  # making the turtle to stop



            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            x = random.randint(-int(screen_width / 2),
                               int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                               int(screen_height / 2))  # getting random values under the screen height
            planet2.goto(x, y)

            x = random.randint(-int(screen_width / 2),
                               int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                               int(screen_height / 2))  # getting random values under the screen height
            planet1.goto(x, y)

            x = random.randint(-int(screen_width / 2),
                               int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                               int(screen_height / 2))  # getting random values under the screen height
            planet3.goto(x, y)
            # Reset level1_use
            level1_use = 1
            # Reset level
            level = 1
            pen.up()
            pen.goto(-10, 0)
            pen.down()
            pen.clear()



            pen.write("Game Over !!", align="center",
                      font=("Courier", 35, "normal"))  # printing game over
            playsound.playsound('./Assets/laser_hit.wav')

            # time.sleep(1)
            repeat = screen.textinput("Game over!", "type yes or no to play again")
            while not repeat:
                if not repeat:
                    repeat = screen.textinput("Game over!,type yes or no to play again")
            if repeat == 'yes':

                asteroid.hideturtle()
                asteroid.goto(1100, 900)
                asteroid1.hideturtle()
                asteroid1.goto(1100, 900)

                # grid.clear()
                pen.color('white')
                pen.up()
                pen.goto(0, 260)
                pen.down()
                pen.clear()
                pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                          font=("Courier", 16, "normal"))  # resetting the score
            else:
                end_loop = 1
                screen.bye()

        # Check for a collision with the planet

        if player.distance(planet2) < 34:  # check if collision with the planet2
            fo = planet2
        elif player.distance(planet3) < 34:  # check if collision with the planet3
            fo = planet3
        if player.distance(planet1) < 34:  # check if collision with the planet1
            fo = planet1
        if player.distance(planet) < 34:  # check if collision with the planet
            fo = planet
        if player.distance(planet3) < 34 or player.distance(planet2) < 34 or player.distance(planet1) < 34 or player.distance(planet) < 34:
            # Move the planet to a random spot
            x = random.randint(-int(screen_width / 2),
                               int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                               int(screen_height / 2))  # getting random values under the screen height
            fo.goto(x, y)

            # Shorten the delay
            delay -= 0.001

            score += 10  # increasing the score
            playsound.playsound('./Assets/Hit_for_first_game.mp3', block=False)
            if score > high_score:  # Checking if score is the highest sore
                high_score = score  # Then update  the list to the high score
            pen.clear()
            pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                      font=("Courier", 16, "normal"))  # Writing the current score

        if player.distance(obstacle2) < 70 or player.distance(obstacle) < 70:  # Check for a collision with the obstacle
            score-= 10  # decreasing the score
            playsound.playsound('./Assets/punch_sound.wav',block=False)

            x = random.randint(-200, 200)
            y = random.randint(-190, 190)
            player.goto(x, y)  # Moving the player to random position



            pen.clear()
            pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                      font=("Courier", 16, "normal")) # Writing the current score


        move() # calling the move function

        # Levels
        if level == 1 and score == 100:#  Check if it is level 1
            level += 1     # update the level
            planet2.goto(1000, 1000)
            # time_used = time_used + 1
            pen.goto(0, 240)
            start = time.time()
            pen.color('orange')

            while time.time() - start < 6:
                pen.clear()

                pen.goto(0, 210)
                pen.write('You will enter level 2  in 5 sec , Time :' + str(int(time.time() - start)), align="center",
                          font=("Courier", 16,"normal")) #Writing the current time



            pen.goto(0, 260)
            pen.clear()     # Clearing the screen
            pen.color('white')
            time_used = 0


            pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                      font=("Courier", 16, "normal")) #Writing the current score


        if level == 2 and score == 150:#  Check if it is level 1
            level += 1   # update the level
            planet1.goto(1000, 1000)

            start = time.time()
            pen.color('orange')


            while time.time() - start < 6:
                pen.clear()
                pen.goto(0, 210)

                pen.write('You will enter level 3  in 5 sec , Time :' + str(int(time.time() - start)), align="center",
                          font=("Courier", 16))    #Writing the current time



            time_used = 0
            pen.goto(0, 260)
            pen.clear()  # Clearing the screen
            pen.color('white')

            pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                      font=("Courier", 16, "normal"))   #Writing the current score

            # planet1.hideturtle()
        if level == 3 and score == 200:#  Check if it is level 1
            level += 1  # update the level
            planet3.goto(1000, 1000)

            pen.goto(0, 240)
            start = time.time()
            pen.color('orange')

            # pen.write('You are entering level 2 ')
            while time.time() - start < 6:
                pen.clear()
                # pen.goto(0, 240)
                pen.goto(0, 220)
                pen.write('You will enter level 4 in 5 sec , Time :' + str(int(time.time() - start)), align="center",
                          font=("Courier", 16))  #Writing the current time



            pen.goto(0, 260)
            pen.clear()  # Clearing the screen
            pen.color('white')

            time_used = 0

            pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                      font=("Courier", 16, "normal")) #Writing the current score


        time.sleep(delay)
        pen.clear() #  Clearing the screen
        pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                  font=("Courier", 16, "normal"))  #Writing the current score
        if end_loop == 1:
            return

        if score == 300:
            # time.sleep(1)  # sleeping for 1 second
            player.goto(0, 0)  # resetting the position
            player.shape("./Assets/rocket _up.gif")
            player.direction = "stop"  # making the turtle to stop


            # Reset the score
            score = 0


            # Reset the delay
            delay = 0.1

            x = random.randint(-int(screen_width / 2),
                               int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                               int(screen_height / 2))  # getting random values under the screen height
            planet2.goto(x, y)

            x = random.randint(-int(screen_width / 2),
                               int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                               int(screen_height / 2))  # getting random values under the screen height
            planet1.goto(x, y)

            x = random.randint(-int(screen_width / 2),
                               int(screen_width / 2))  # getting random values under the screen width
            y = random.randint(-int(screen_height / 2),
                               int(screen_height / 2))  # getting random values under the screen height
            planet3.goto(x, y)
            # Reset level1_use

            level = 1
            pen.up()
            pen.goto(-10, 0)
            pen.down()
            pen.clear()
            winner.showturtle()

            time.sleep(3)

            repeat = screen.textinput("Won the game ", "type yes or no to play again")
            while not repeat:
                if not repeat:
                    repeat = screen.textinput("Won the game,type yes or no to play again")
            if repeat == 'yes':

                asteroid.hideturtle()
                asteroid.goto(1100, 900)
                asteroid1.hideturtle()
                asteroid1.goto(1100, 900)
                winner.hideturtle()
                pen.color('white')
                pen.up()
                pen.goto(0, 260)
                pen.down()
                pen.clear()
                pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center",
                          font=("Courier", 16, "normal"))  # resetting the score
                playsound.playsound('./Assets/Won_the_game.mp3', False)


            else:
                end_loop = 1
                screen.bye()



game()
    # exit()
