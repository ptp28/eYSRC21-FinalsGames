def game3():
    import turtle
    import math
    import random
    import playsound
    # from sheet_dot_best_manager import sheet_manager
    def int_screen():  # Initializing the screen
        global  screen # Make the screen a global variable
        screen = turtle.Screen() # Create screen object
        screen.setup(width=800, height=600)
        screen.title("Space Invader 2")
        screen.bgcolor("black")
        screen.bgpic("Assets/space4.gif")
        # Stop screen updates
        screen.tracer(0)


        # Register Shapes
        player1_vertices =((0,25),(-15,0),(-18,5),(-18,-5),(0,-10),(18,-5),(18, 5),(15, 0))
        screen.register_shape("space jet1.gif", player1_vertices)
        player_vertices = (
        (-111, 94), (-120, 48), (-124, 35), (-127, 19), (-128, 10), (-171, -15), (-174, -28), (-153, -37), (-129, -22),
        (-127, -30), (-144, -41), (-137, -54), (-122, -49), (-120, -42), (-102, -42), (-103, -51), (-85, -54), (-78, -43),
        (-98, -32), (-98, -21), (-70, -35), (-47, -26), (-48, -21), (-90, 9), (-92, 16), (-100, 48), (-111, 94))
        screen.register_shape("space jet.gif", player_vertices)
        player2_vertices = (
        (111, -94), (120, -48), (124, -35), (127, -19), (128, -10), (171, 15), (174, 28), (153, 37), (129, 22), (127, 30),
        (144, 41), (137, 54), (122, 49), (120, 42), (102, 42), (103, 51), (85, 54), (78, 43), (98, 32), (98, 21), (70, 35),
        (47, 26), (48, 21), (90, -9), (92, -16), (100, -48), (111, -94))
        screen.register_shape("space jet2.gif", player2_vertices)

        screen.register_shape("Assets/ufo2.gif")
        screen.register_shape("Assets/bullet.gif")

    def int_player(): # initialising the player
        global player,player1,player2# Initialising the player
        player = turtle.Turtle()
        player.speed(0)
        player.penup()
        player.color("#6E8B20")
        player.shape("space jet.gif")
        player.score = 0
        player1 = turtle.Turtle()
        player1.speed(0)
        player1.penup()
        player1.color('#ae0a02')
        player1.shape("space jet1.gif")
        player1.score = 0
        player2 = turtle.Turtle()
        player2.speed(0)
        player2.penup()
        player2.color("#727934")
        player2.shape("space jet2.gif")
        player2.score = 0



        # return heading
    def int_missile(): # initialising the missile
        global missiles
        missiles = []
        for i in range(10):
            missile = turtle.Turtle()
            missile.speed(0)
            missile.penup()
            missile.color("blue")
            missile.shape("circle")
            missile.speed = 1
            missile.state = "ready"
            missile.hideturtle()
            missile.shapesize(1,2,1)
            missiles.append(missile)
    def int_score_pen() : # initialising the score_pen
        global pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.penup()
        pen.color("white")
        pen.hideturtle()
        pen.goto(0, 250)
        pen.write("Score: 0", False, align="center", font=("Arial", 24, "normal"))

    def int_asteroid(): # initialising the asteroid
        global asteroids
        asteroids = []
        for n in range(5):
            # print(x,y)
            ufo = turtle.Turtle()
            ufo.color("brown")
            ufo.speed(0)
            ufo.penup()
            ufo.shape("Assets/ufo2.gif")
            ufo.speed = random.randint(2, 3) / 30
            ufo.goto(0,0)
            # if rocket_ship_move == 2:
            heading = random.randint(0,250)
            # manager.send_data({'heading':heading})
            distance = random.randint(300, 350)
            ufo.setheading(heading)
            ufo.forward(distance)
            x1 = player.xcor()
            y1 = player.ycor()
            x2 = ufo.xcor()
            y2 = ufo.ycor()
            heading = math.atan2(y1 - y2, x1 - x2)
            heading = heading * 180.0 / 3.14159
            ufo.setheading(heading)
            asteroids.append(ufo)

    int_screen()
    int_player()
    int_asteroid()
    int_score_pen()
    int_missile()
    playsound.playsound('Assets/Game_start.mp3')

    def turn_left():

        player.lt(20)
        player1.lt(20)
        player2.lt(20)


    def turn_right():


        player.rt(20)
        player1.rt(20)
        player2.rt(20)



    def f_missile(): # fireing the missile
        for missile in missiles:
            if missile.state == "ready":
                playsound.playsound('Assets/Hit_sound.wav', False)

                missile.goto(0,0 )
                missile.showturtle()
                missile.setheading(player.heading())
                missile.state = "fire"
                break


    # Keyboard binding
    screen.listen()
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(f_missile, "space")


    # Start main game loop\
    Game_Over = False
    while True:
        # Do screen update
        screen.update()
        player.goto(0, 0)



        for missile in missiles:
            if missile.state == "fire":
                missile.fd(missile.speed)# Move the missile


            if missile.xcor() > 400 or missile.xcor() < -400 or missile.ycor() > 300 or missile.ycor() < -300:# Border hiting
                missile.hideturtle()
                missile.state = "ready"


        for ufo in asteroids:# Iterate through all asteroids

            ufo.fd(ufo.speed)# Move the asteroid



            for missile in missiles:
                # ufo.fd(distance)
                if ufo.distance(missile) < 60  : # Check for collisions
                    ufo.fd(ufo.speed)

                    #Reset ufo
                    heading = random.randint(0, 260)
                    distance = random.randint(600, 800)
                    ufo.setheading(heading)
                    ufo.fd(distance)
                    x1 = player.xcor()
                    y1 = player.ycor()
                    x2 = ufo.xcor()
                    y2 = ufo.ycor()
                    heading = math.atan2(y1 - y2, x1 - x2)
                    heading = heading * 180.0 / 3.14159
                    ufo.setheading(heading)

                    ufo.speed += 0.06

                    # Reset Missile
                    missile.goto(600, 600)
                    missile.hideturtle()
                    missile.state = "ready"

                    # Increase score
                    player.score += 10
                    pen.clear()
                    pen.write("Score: {}".format(player.score), False, align="center", font=("Arial", 24, "normal"))

            # Asteroid and Player
            if ufo.distance(player) < 40 or ufo.distance(player1) < 160 or  ufo.distance(player2) < 160:
                 # Reset Asteroid
                heading = random.randint(0, 260)
                distance = random.randint(600, 800)
                ufo.setheading(heading)
                ufo.fd(distance)
                x1 = player.xcor()
                y1 = player.ycor()
                x2 = ufo.xcor()
                y2 = ufo.ycor()
                heading = math.atan2(y1 - y2, x1 - x2)
                heading = heading * 180.0 / 3.14159
                ufo.setheading(heading)
                ufo.speed += 0.006
                Game_Over = True
                player.score -= 30
                pen.clear()
                pen.write("Score: {}".format(player.score), False, align="center", font=("Arial", 24, "normal"))
        if Game_Over == True:
            repeat = screen.textinput("Game over!", "Type yes or no to play again")

            while not repeat:
                if not repeat:
                    repeat = screen.textinput("Game over!", "type yes or no to play again")
            if repeat == 'yes':
                Game_Over = False

                for ufo in asteroids:
                    heading = random.randint(0, 200)
                    distance = random.randint(500, 600)
                    ufo.setheading(heading)
                    ufo.fd(distance)
                    x1 = player.xcor()
                    y1 = player.ycor()
                    x2 = ufo.xcor()
                    y2 = ufo.ycor()
                    heading = math.atan2(y1 - y2, x1 - x2)
                    heading = heading * 180.0 / 3.14159
                    ufo.setheading(heading)
                    ufo.speed += 0.06
                    # ufo.hideturtle()
                    # ufo.goto(1000,1000)
                for missile in missiles:
                    # Reset Missile
                    missile.goto(600, 600)
                    missile.hideturtle()
                    missile.state = "ready"

                    # Keyboard binding
                screen.listen()
                player.score = 0
                pen.clear()
                pen.write("Score: {}".format(player.score), False, align="center", font=("Arial", 24, "normal"))
                # break
            if repeat == 'no':
                screen.bye()


game3()