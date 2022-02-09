# Imports
import turtle as t
import random
from time import sleep


# Global Variables
# Registering the shapes
t.register_shape('Assets/falcon.gif')
t.register_shape('Assets/tie_fighter_1gif.gif')
t.register_shape('Assets/tie_fighter_2gif.gif')
t.register_shape('Assets/pixel_laser_green.gif')

# Lives, score etc.
score = 0
enemy_count = 5
lives = 3
wave = 1
wavelength = 5

# Player
player_ship = t.Turtle()
player_ship.shape('Assets/falcon.gif')

# Pen
font = ('Courier', 20, '')  # Global font
pen = t.Turtle()  # Global Pen


# Functions
# Movement functions
def move_left():  # Player Left Movement
    player_ship.setheading(180)
    player_ship.fd(15)
    if player_ship.xcor() < -370:
        player_ship.goto(-370, player_ship.ycor())


def move_right():  # Player Right Movement
    player_ship.setheading(0)
    player_ship.fd(15)
    if player_ship.xcor() > 370:
        player_ship.goto(370, player_ship.ycor())


def move_up():  # Player Up Movement
    player_ship.setheading(90)
    player_ship.fd(15)
    if player_ship.ycor() > 270:
        player_ship.goto(player_ship.xcor(), 270)


def move_down():  # Player Down Movement
    player_ship.setheading(270)
    player_ship.fd(15)
    if player_ship.ycor() < -270:
        player_ship.goto(player_ship.xcor(), -270)


def shoot():  # Shooting Bullets
    global enemies, score, wavelength, wave

    main_laser = t.Turtle()
    main_laser.ht()
    main_laser.speed(0)
    main_laser.pu()
    main_laser.goto(player_ship.xcor(), player_ship.ycor())  # To ensure that the bullet stays with the ship
    main_laser.shape('Assets/pixel_laser_green.gif')

    shot_laser = main_laser.clone()  # Cloning our main bullet
    shot_laser.speed = 170  # Speed of our bullet
    shot_laser.st()

    while shot_laser.xcor() < 400:  # Check if bullet has hit border
        x = shot_laser.xcor()
        x += shot_laser.speed
        shot_laser.setx(x)

        if shot_laser.xcor() >= 400:  # If it has hit border, hide it
            shot_laser.ht()

        for enemy in enemies:  # Looping through enemies
            if shot_laser.distance(enemy) < 70:  # Checking if bullet has hit enemy
                shot_laser.ht()
                shot_laser.goto(0, 500)  # Sending our bullet off-screen
                enemy.goto(random.randint(450, 550), random.randint(-270, 270))
                score += 5
                pen.clear()
                pen.write('Score: {} Lives: {} Wave: {}'.format(score, lives, wave), align='Center', font=font)
                wavelength -= 1  # Length of the wave reduces as we kill more enemies
                if wavelength <= 0:
                    wave += 1
                    wavelength = wave * enemy_count
                    pen.clear()
                    pen.write('Score: {} Lives: {} Wave: {}'.format(score, lives, wave), align='Center', font=font)
                    for enemy in enemies:  # Wave ended, so respawn all enemies
                        enemy.goto(random.randint(450, 550), random.randint(-270, 270))
                    sleep(5)  # Freezes time for 5 secs


# Main Functions
def screen_setup():
    global win

    win = t.Screen()
    win.setup(800, 600)
    win.setworldcoordinates(-400, -300, 400, 300)
    win.title('Star Wars: Space Shooter')
    win.bgpic('Assets/deathstar.gif')

    # Player pre-initialization
    player_ship.speed(0)
    player_ship.pu()
    player_ship.ht()
    player_ship.goto(-300, 0)
    player_ship.st()

    # Pen pre-initialization
    pen.ht()
    pen.pu()
    pen.pencolor('green')
    pen.goto(0, 270)
    pen.clear()
    pen.write('Score: {} Lives: {} Wave: {}'.format(score, lives, wave), align='Center', font=font)


def triggers():
    t.onkeypress(move_up, 'Up')
    t.onkeypress(move_down, 'Down')
    t.onkeypress(move_left, 'Left')
    t.onkeypress(move_right, 'Right')

    t.onkeypress(shoot, 'space')

    t.listen()


def enemy_ships():
    global enemies, lives, win
    enemies = []  # List of enemies
    enemy_sprites = ['Assets/tie_fighter_1gif.gif', 'Assets/tie_fighter_2gif.gif']  # List of enemy ship shapes

    for enemy in range(enemy_count):  # Making our enemies
        enemy = t.Turtle()
        enemy.speed(0)
        enemy.pu()
        enemy.ht()
        enemy.goto(random.randint(450, 550), random.randint(-270, 270))  # Spawning the enemies
        enemy.speed = random.randint(5, 15)
        enemy.setheading(180)
        enemy.shape(random.choice(enemy_sprites))  # Choose a sprite
        enemy.showturtle()
        enemies.append(enemy)  # Appends the enemies to the list

    while True:  # Main while loop running throughout the game for enemy movement
        for ship in enemies:
            x = ship.xcor()  # Current X coordinate of ship
            x -= ship.speed  # Moving our ship
            ship.setx(x)

            if x < -370:
                ship.goto(random.randint(450, 550), random.randint(-270, 270))
                ship.speed += 2

            if ship.distance(player_ship) <= 60:
                ship.goto(random.randint(450, 550), random.randint(-270, 270))
                lives -= 1
                pen.clear()
                pen.write('Score: {} Lives: {} Wave: {}'.format(score, lives, wave), align='Center', font=font)
                if lives <= 0:
                    pen.clear()
                    pen.goto(0, -80)
                    game_over_font = ('Courier', 15, '')
                    pen.write('Game Over! Your final score was {}, you survived till wave {}'.format(score, wave), align='Center', font=game_over_font)
                    win.update()
                    player_ship.speed(5)
                    player_ship.home()
                    t.exitonclick()



t.delay(20)  # Optimal delay for our game
screen_setup()
triggers()
enemy_ships()
t.mainloop()
