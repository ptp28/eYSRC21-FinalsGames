# Importing libraries
import turtle
import random
import os


# ## FUNCTIONS ## #

# Drawing the road
def draw_road():
    road.hideturtle()
    road.color('white')
    road.width(5)

    # Line 1
    road.up()
    road.goto(75, -410)
    road.down()
    road.goto(75, 410)

    # Line 2
    road.up()
    road.goto(-75, -410)
    road.down()
    road.goto(-75, 410)

    # Line 2
    road.up()
    road.fillcolor('lime green')
    road.begin_fill()
    road.goto(225, -410)
    road.down()
    road.goto(225, 410)
    road.goto(320, 410)
    road.goto(320, -410)
    road.goto(225, -410)
    road.end_fill()

    # Line 4
    road.up()
    road.fillcolor('lime green')
    road.begin_fill()
    road.goto(-225, -410)
    road.down()
    road.goto(-225, 410)
    road.goto(-320, 410)
    road.goto(-320, -410)
    road.goto(-225, -410)
    road.end_fill()


def do_nothing():
    pass


# Initializing the score board
def init_score_display():
    pen.hideturtle()
    pen.up()
    # draw_dox
    score_board.hideturtle()
    score_board.up()
    score_board.width(5)

    score_board.fillcolor('brown')
    score_board.goto(-300, 300)
    score_board.begin_fill()
    score_board.down()
    score_board.goto(5, 300)
    score_board.goto(5, 240)
    score_board.goto(-300, 240)
    score_board.goto(-300, 300)
    score_board.end_fill()
    pen.color('yellow')
    screen.update()


# for printing the score
def display_score():
    pen.clear()
    pen.goto(-280, 245)
    pen.color('yellow')
    pen.write(f'Coins:{points}', False, 'left', ('Press Start 2P', 22, 'normal'))


# Moving the player right
def right():
    global game_state

    if not player.xcor() + 150 > 150:
        for go_right in range(30):
            if game_state == 'running':
                player.setx(player.xcor() + 5)
                for cars in other_cars:
                    if player.distance(cars) <= 60:
                        game_state = 'game over'
                screen.update()
    else:
        player.setx(150)


# Moving the player left
def left():
    global game_state

    if not player.xcor() - 150 < -150:
        for go_left in range(30):
            if game_state == 'running':
                player.setx(player.xcor() - 5)
                for cars in other_cars:
                    if player.distance(cars) <= 60:
                        game_state = 'game over'
                screen.update()
    else:
        player.setx(-150)


# Starting the game, detecting for game_over, pausing etc.
def start():
    global game_state, speed, points, go, initial_speed
    if game_state != 'game over' and game_state != 'pause':
        game_state = 'running'

    while game_state == 'running':
        if game_type == 'story':
            if points >= 100:
                game_state = 'win'
        for cars in other_cars:
            cars.showturtle()
            if player.distance(cars) <= 90:
                game_state = 'game over'
            elif cars.ycor() > -350:
                go = True
                for o_car in other_cars:
                    if o_car != cars:
                        if cars.distance(o_car) <= 250:
                            go = False
                        else:
                            if go is not False:
                                go = True
                    else:
                        go = True
                if go is True:
                    cars.sety(cars.ycor() - speed)
                else:
                    cars.sety(cars.ycor() + speed)
            else:
                cars.goto(random.choice(x_cors), 570)
                cars.shape(random.choice(others))
            screen.update()

        for collect in coins:
            collect.showturtle()
            if player.distance(collect) <= 70:
                points += 1
                collect.goto(random.choice(x_cors), 400)
                display_score()
                screen.update()
            if collect.ycor() > -350:
                go = True
                for cars in other_cars:
                    if collect.distance(cars) <= 80:
                        go = False
                    else:
                        if go is not False:
                            go = True
                if go is True:
                    collect.sety(collect.ycor() - speed)
                else:
                    go = True
            else:
                collect.goto(random.choice(x_cors), 320)
            screen.update()

        # # Increase speed as points increase
        # if points % 15 == 0 and points >= 15:
        #     speed = initial_speed + points / 15

        screen.update()

    if game_state == 'pause':
        pass

    if game_state == 'game over':
        screen.onkeypress(do_nothing, 'Left')
        screen.onkeypress(do_nothing, 'Right')
        game_over_screen.stamp()
        pen.goto(0, 190)
        pen.color('black')
        pen.write(f' Coins collected: {points}', False, 'center', ('Press Start 2P', 15, 'normal'))
        screen.update()

    if game_state == 'win':
        win_screen.stamp()
        screen.update()
        pen.goto(-230, -70)
        pen.color('black')
        pen.write('Thanks for helping me\n'
                  'collect the coins.\n'
                  'Hurrah!! Now I can\n'
                  'upgrade my parts.', False, 'left', ('Press Start 2P', 15, 'normal'))


# Responding to a click and do accordingly
def play(x, y):
    global game_type, game_state, points, speed, initial_speed
    # Reset the speed
    speed = initial_speed

    if game_state != 'running':
        if screen.bgpic() == main_menu_shape:

            # Detecting if play is clicked
            if -232 < x < 232 and -242 < y < -80:

                # If play is clicked print the controls page
                screen.bgpic(control_page)
                pen.color('black')
                pen.goto(-85, -160)
                pen.write("Press 'D' or\n'Right Arrow'\nto move right\n\n\n"
                          "Press 'A' or\n'Left Arrow' to\n move left\n\n\n"
                          "Press 'P' to\npause", False, 'left', ('Press Start 2P', 15, 'normal'))
                pen.goto(-160, -230)
                pen.write("Click anywhere to\n    continue", False, 'left', ('Press Start 2P', 15, 'normal'))
        elif screen.bgpic() == control_page:
            pen.clear()
            screen.bgpic(mode_page)
        elif screen.bgpic() == mode_page:

            # If endless button clicked set mode to endless and start the game
            if -275 < x < 275 and -275 < y < -97:
                screen.bgpic('nopic')
                game_type = 'endless'
                draw_road()
                init_score_display()
                display_score()
                player.shape(player_shape)
                player.showturtle()
                start()

            # If story button clicked set mode to story and print the story
            elif -232 < x < 221 and 95 < y < 257:
                game_type = 'story'
                screen.bgpic(story_page)
                pen.goto(-230, -90)
                pen.color('black')
                pen.write('Hi! I am ROADSTER, the\n'
                          'race car.I have a big\n'
                          'race coming up which I\n'
                          'have to win to become the\n'
                          'WORLD CHAMPION.To win the\n'
                          'race, I need to upgrade\n'
                          'my parts. For that, I\n'
                          'need 100 COINS. Please\n'
                          'help me to collect 100\n'
                          '    coins without hitting\n'
                          '      any cars.\n'
                          '       Press START to\n'
                          '       continue.', False, 'left', ('Press Start 2P', 15, 'normal'))
        elif screen.bgpic() == story_page:

            # If start clicked after story is print, start the game
            if -170 < x < 170 and -287 < y < -167:
                screen.bgpic('nopic')
                draw_road()
                init_score_display()
                display_score()
                player.shape(player_shape)
                player.showturtle()
                start()

        elif game_state == 'game over':

            # If retry button is clicked at the game over screen screen, restart.
            if -144 < x < -23 and -152 < y < -39:
                game_over_screen.clear()
                restart_level()

            # If home button is clicked at the game over screen go to menu
            elif 30 < x < 151 and -152 < y < -39:
                game_over_screen.clear()
                go_to_menu()
        elif game_state == 'win':

            # If retry button is clicked at the win screen screen, restart.
            if -146 < x < -30 and -189 < y < -81:
                win_screen.clear()
                restart_level()

            # If home button is clicked at the win screen go to menu
            elif 21 < x < 138 and -189 < y < -81:
                win_screen.clear()
                go_to_menu()


# To restart the level after retry button is clicked
def restart_level():
    global points, game_state, speed, initial_speed
    speed = initial_speed
    points = 0
    display_score()
    player.goto(0, -200)
    screen.onkeypress(left, 'Left')
    screen.onkeypress(right, 'Right')
    repeat = 0
    for car in other_cars:
        car.goto(random.choice(x_cors), 400 + repeat * 200)
        repeat += 1
    repeat = 0
    for coin in coins:
        coin.goto(random.choice(x_cors), 400 + repeat * 200)
        repeat += 1
    game_state = 'running'
    start()


# To go to the menu when home clicked
def go_to_menu():
    global game_state, points
    game_state = 'menu'
    points = 0
    road.clear()
    pen.clear()
    score_board.clear()
    player.goto(0, -200)
    screen.onkeypress(left, 'Left')
    screen.onkeypress(right, 'Right')
    repeat = 0
    for car in other_cars:
        car.goto(random.choice(x_cors), 400 + repeat * 200)
        repeat += 1
    repeat = 0
    for coin in coins:
        coin.goto(random.choice(x_cors), 400 + repeat * 200)
        repeat += 1
    for car in other_cars:
        car.hideturtle()
    for coin in coins:
        coin.hideturtle()
    player.hideturtle()
    screen.bgpic(main_menu_shape)
    screen.update()


# Pause and unpause the game when p pressed
def pausing():
    global game_state
    if game_state == 'running':
        pause.stamp()
        game_state = 'pause'
    elif game_state == 'pause':
        pause.clear()
        game_state = 'running'
        start()


# ##___________## #

# Loading the assets
main_menu_shape = os.path.join('Assets', 'main_menu.gif')
control_page = os.path.join('Assets', 'controls.gif')
player_shape = os.path.join('Assets', 'player.gif')
green_car_shape = os.path.join('Assets', 'green_car.gif')
blue_car_shape = os.path.join('Assets', 'blue_car.gif')
coin_shape = os.path.join('Assets', 'coin.gif')
game_over_screen_shape = os.path.join('Assets', 'game_over_screen.gif')
win_screen_shape = os.path.join('Assets', 'win_screen.gif')
pause_shape = os.path.join('Assets', 'pause.gif')
mode_page = os.path.join('Assets', 'mode_selection.gif')
story_page = os.path.join('Assets', 'story_bg.gif')


# Initializing the screen
screen = turtle.Screen()
screen.setup(650, 650)
screen.title("e-Yantra School Robotics Competition  (TEAM ROTHON - #63)")
screen.setworldcoordinates(-300, -300, 300, 300)
screen.bgcolor("dim gray")
screen.tracer(0)
screen.bgpic(main_menu_shape)

# Setting up the points variable
points = 0

# Registering shapes
turtle.register_shape(player_shape)
turtle.register_shape(green_car_shape)
turtle.register_shape(blue_car_shape)
turtle.register_shape(coin_shape)
turtle.register_shape(game_over_screen_shape)
turtle.register_shape(win_screen_shape)
turtle.register_shape(pause_shape)

others = [blue_car_shape, green_car_shape]

# All turtle registrations

# For printing the road
road = turtle.Turtle()

# For printing the score the story etc.
pen = turtle.Turtle()

# For printing the score board
score_board = turtle.Turtle()

# The player turtle
player = turtle.Turtle()

# The game over screen turtle
game_over_screen = turtle.Turtle()

# The win screen turtle
win_screen = turtle.Turtle()

# The pause screen turtle
pause = turtle.Turtle()

# Hiding all the turtle at the start
score_board.hideturtle()
pen.hideturtle()
road.hideturtle()
game_over_screen.hideturtle()
win_screen.hideturtle()
pause.hideturtle()

# Shape allotment
game_over_screen.shape(game_over_screen_shape)
win_screen.shape(win_screen_shape)
pause.shape(pause_shape)


player.penup()
player.hideturtle()

# Setting the game_state and game_type for the first time
game_state = 'menu'
game_type = 'not_selected'

go = True

x_cors = [-150, 0, 150]
other_cars = []
coins = []

# Creating the cars
for i in range(4):
    car = turtle.Turtle()
    car.hideturtle()
    car.up()
    car.shape(random.choice(others))
    car.shapesize(3, 2)
    car.goto(random.choice(x_cors), 400 + i * 200)
    other_cars.append(car)

# Creating the turtles
for i in range(4):
    coin = turtle.Turtle()
    coin.hideturtle()
    coin.up()
    coin.shape(coin_shape)
    coin.color('yellow')
    coin.goto(random.choice(x_cors), 1400 + i * 200)
    coins.append(coin)

player.goto(0, -200)
initial_speed = 10
speed = initial_speed

# Updating the screen
screen.update()

# The key and click bindings
screen.onkeypress(left, 'Left')
screen.onkeypress(right, 'Right')
screen.onclick(play)
screen.onkeypress(left, 'a')
screen.onkeypress(right, 'd')
screen.onkeypress(pausing, 'p')

screen.listen()

screen.mainloop()
