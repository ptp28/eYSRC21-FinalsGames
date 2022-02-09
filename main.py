import time
import turtle
import random

# Variables
turn = 1
blue_pos = 0
red_pos = 0
red_dir = 1
blue_dir = 1
blue_start = True
red_start = True
player_1 = ""
player_2 = ""
mode = ""
player_6_counter = 0
red_6_counter = 0
blue_6_counter = 0
quit = False


# Functions
def PvPBlueTurn():
    global turn, blue_start, blue_pos, blue_dir, blue_6_counter, mode, quit
    if turn == 1:
        if blue_start:
            blue.goto(-192, -165)
            blue_start = False
        random_play = random.randint(1, 6)
        blue_dice.showturtle()
        if random_play == 1:
            blue_dice.shape("Assets/blue_one.gif")
        elif random_play == 2:
            blue_dice.shape("Assets/blue_two.gif")
        elif random_play == 3:
            blue_dice.shape("Assets/blue_three.gif")
        elif random_play == 4:
            blue_dice.shape("Assets/blue_four.gif")
        elif random_play == 5:
            blue_dice.shape("Assets/blue_five.gif")
        elif random_play == 6:
            blue_dice.shape("Assets/blue_six.gif")
        for i in range(random_play):
            if blue_pos == 100:
                break
            if blue_pos != 0 and blue_pos % 10 == 0:  # Go up
                blue.setheading(90)
                blue.forward(35)
                blue_dir = -blue_dir
                window.update()
                time.sleep(0.5)
            else:  # Go left right
                if blue_dir == 1:
                    blue.setheading(0)
                elif blue_dir == -1:
                    blue.setheading(180)
                blue.forward(35)
                window.update()
                time.sleep(0.5)
            blue_pos += 1

        str_blue_pos = str(blue_pos)
        if board_data[str_blue_pos][0] == "snake" or board_data[str_blue_pos][0] == "ladder":
            blue.goto(-192, -165)
            blue_pos = 0
            blue_dir = 1
            for i in range(board_data[str_blue_pos][1]):
                if blue_pos != 0 and blue_pos % 10 == 0:
                    blue.setheading(90)
                    blue.forward(35)
                    blue_dir = -blue_dir
                else:
                    if blue_dir == 1:
                        blue.setheading(0)
                    elif blue_dir == -1:
                        blue.setheading(180)
                    blue.forward(35)
                blue_pos += 1
        if blue_pos == 100:
            reply = window.textinput(player_1 + "won", "End of Game \n Type (y/n) if you want to play again")
            if reply == "" or reply is None or reply == "y":
                blue_dice.hideturtle()
                red_dice.hideturtle()
                blue.hideturtle()
                red.hideturtle()
                window.resetscreen()
                window.bgpic("nopic")
                mode = ""
            elif reply == "n":
                turtle.bye()
                quit = True
                return
            home(1, 1)
            return
        turn = -1
        if random_play == 6:
            blue_6_counter += 1
            if blue_6_counter < 3:
                turn = 1
            else:
                blue_6_counter = 0
                turn = -1
        else:
            blue_6_counter = 0
    elif turn == -1:
        window.textinput("Wait for your turn", player_1 + " you must wait for your turn now it Red's chance")
def PvPRedTurn():
    global turn, red_start, red_dir, red_pos, red_6_counter, mode, quit
    if turn == -1:  # Check if it's red turn
        if red_start:  # Checks if it is start or first move
            red.goto(-192, -165)
            red_start = False
        random_play = random.randint(1, 6)  # Dice Throw
        red_dice.showturtle()
        if random_play == 1:
            red_dice.shape("Assets/red_one.gif")
        elif random_play == 2:
            red_dice.shape("Assets/red_two.gif")
        elif random_play == 3:
            red_dice.shape("Assets/red_three.gif")
        elif random_play == 4:
            red_dice.shape("Assets/red_four.gif")
        elif random_play == 5:
            red_dice.shape("Assets/red_five.gif")
        elif random_play == 6:
            red_dice.shape("Assets/red_six.gif")
        for i in range(random_play):
            if red_pos == 100:
                break
            if red_pos != 0 and red_pos % 10 == 0:  # If the coin has to go up
                red.setheading(90)
                red.forward(35)
                red_dir = -red_dir
                window.update()
                time.sleep(0.5)
            else:  # If coin instead has to go to left or right
                if red_dir == 1:
                    red.setheading(0)
                elif red_dir == -1:
                    red.setheading(180)
                red.forward(35)
                window.update()
                time.sleep(0.5)
            red_pos += 1
        str_red_pos = str(red_pos)
        if board_data[str_red_pos][0] == "snake" or board_data[str_red_pos][0] == "ladder":
            pre_red_data = board_data[str_red_pos]
            red.goto(-192, -165)
            red_pos = 0
            red_dir = 1
            for i in range(pre_red_data[1]):
                if red_pos != 0 and red_pos % 10 == 0:
                    red.setheading(90)
                    red.forward(35)
                    red_dir = -red_dir
                else:
                    if red_dir == 1:
                        red.setheading(0)
                    elif red_dir == -1:
                        red.setheading(180)
                    red.forward(35)
                red_pos += 1
        if red_pos == 100:
            reply = window.textinput(player_2 + " won", "End of Game \n Type (y/n) if you want to play again")
            if reply == "" or reply is None or reply == "y":
                blue_dice.hideturtle()
                red_dice.hideturtle()
                blue.hideturtle()
                red.hideturtle()
                window.onclick(play)
                window.onkey(guide, "H")
                window.onkey(guide, "h")
                window.listen()
                window.update()
                window.resetscreen()
                window.bgpic("nopic")
                mode = ""
            elif reply == "n":
                quit = True
                turtle.bye()
                return
            home(1, 1)
            return
        turn = 1
        if random_play == 6:
            red_6_counter += 1
            if red_6_counter < 3:
                turn = -1
            else:
                red_6_counter = 0
                turn = 1
        else:
            red_6_counter = 0
    elif turn == 1:
        window.textinput("Wait for your turn", player_2 + " you must wait for your turn now it Blue's chance")

def setup():
    # Variable Creation
    global_vars = globals()
    global blue, red, blue_dice, red_dice
    if "blue" not in global_vars.keys():
        blue = turtle.Turtle()
    if "red" not in global_vars.keys():
        red = turtle.Turtle()
    if "blue_dice" not in global_vars.keys():
        blue_dice = turtle.Turtle()
    if "red_dice" not in global_vars.keys():
        red_dice = turtle.Turtle()

    # Positioning and Graphics
    blue.showturtle()
    red.showturtle()
    blue_dice.showturtle()
    red_dice.showturtle()
    window.bgpic("Assets/board1.gif")
    blue.penup()
    red.penup()
    blue.shape("circle")
    blue.color(53, 4, 128)
    blue.goto(-210, -165)
    red.shape("circle")
    red.color(17, 217, 155)
    red.goto(-240, -165)
    blue_dice.penup()
    blue_dice.goto(0, -217)
    red_dice.penup()
    red_dice.goto(0, 218)
    turtle.addshape("Assets/red_one.gif")
    turtle.addshape("Assets/red_two.gif")
    turtle.addshape("Assets/red_three.gif")
    turtle.addshape("Assets/red_four.gif")
    turtle.addshape("Assets/red_five.gif")
    turtle.addshape("Assets/red_six.gif")
    turtle.addshape("Assets/blue_one.gif")
    turtle.addshape("Assets/blue_two.gif")
    turtle.addshape("Assets/blue_three.gif")
    turtle.addshape("Assets/blue_four.gif")
    turtle.addshape("Assets/blue_five.gif")
    turtle.addshape("Assets/blue_six.gif")
    blue_dice.shape("Assets/blue_six.gif")
    red_dice.shape("Assets/red_six.gif")

    # Final Writings
    dummy.penup()
    dummy.hideturtle()
    dummy.goto(0, -255)
    if mode == "P":
        dummy.write(player_1, False, "center", ("Lucida Calligraphy", 10, "bold"))
        dummy.goto(0, 240)
        dummy.write(player_2, False, "center", ("Lucida Calligraphy", 10, "bold"))
        window.title(player_1 + " Vs " + player_2)
    elif mode == "C":
        dummy.write(player_name, False, "center", ("Lucida Calligraphy", 10, "bold"))
        dummy.goto(0, 240)
        dummy.write("Computer", False, "center", ("Lucida Calligraphy", 10, "bold"))
        window.title(player_name + " Vs Computer")

    window.update()

    if redraw == True:
        global red_pos, red_dir, blue_pos, blue_dir, board_data
        red_spot = red_pos
        blue_spot = blue_pos
        red.goto(-192, -165)
        red_pos = 0
        red_dir = 1
        for i in range(red_spot):
            if red_pos != 0 and red_pos % 10 == 0:
                red.setheading(90)
                red.forward(35)
                red_dir = -red_dir
            else:
                if red_dir == 1:
                    red.setheading(0)
                elif red_dir == -1:
                    red.setheading(180)
                red.forward(35)
            red_pos += 1
        blue.goto(-192, -165)
        blue_pos = 0
        blue_dir = 1
        for i in range(blue_spot):
            if blue_pos != 0 and blue_pos % 10 == 0:
                blue.setheading(90)
                blue.forward(35)
                blue_dir = -blue_dir
            else:
                if blue_dir == 1:
                    blue.setheading(0)
                elif blue_dir == -1:
                    blue.setheading(180)
                blue.forward(35)
            blue_pos += 1




def guide():
    global mode, dummy, window, last_mode
    window.onkey(None, "H")
    window.onkey(None, "h")
    last_mode = mode
    window.resetscreen()
    window.bgpic("nopic")
    dummy.color(250, 211, 70)
    dummy.penup()
    dummy.hideturtle()
    dummy.goto(-245, -42)
    dummy.write("  Rules: \n  Click on the dice to roll"
                "\n  You can press H whenever you like to come back to this page"
                "\n  Each player has their own dice, \n  their name will be written beside it"
                "\n  After a six you get another turn"
                "\n  If you get three sixes in a row your turn ends"
                "\n  If you reach the step of ladder, \n  your piece climbs it"
                "\n  If you reach the mouth of snake, \n  your piece slides down to tail"
                "\n  Click Anywhere to go back to the last screen"
                "\n  End of Rules", False, "left", ("Lucida Calligrapy", 15, "bold"))
    mode = "G"
    window.update()


def player_Play():
    global blue, blue_start, blue_pos, blue_dir, mode, quit, dummy
    if blue_start:
        blue.goto(-192, -165)
        blue_start = False
    random_play = random.randint(1, 6)
    blue_dice.showturtle()
    if random_play == 1:
        blue_dice.shape("Assets/blue_one.gif")
    elif random_play == 2:
        blue_dice.shape("Assets/blue_two.gif")
    elif random_play == 3:
        blue_dice.shape("Assets/blue_three.gif")
    elif random_play == 4:
        blue_dice.shape("Assets/blue_four.gif")
    elif random_play == 5:
        blue_dice.shape("Assets/blue_five.gif")
    elif random_play == 6:
        blue_dice.shape("Assets/blue_six.gif")
    for i in range(random_play):
        if blue_pos == 100:
            break
        if blue_pos != 0 and blue_pos % 10 == 0:
            blue.setheading(90)
            blue.forward(35)
            blue_dir = -blue_dir
            window.update()
            time.sleep(0.5)
        else:
            if blue_dir == 1:
                blue.setheading(0)
            elif blue_dir == -1:
                blue.setheading(180)
            blue.forward(35)
            window.update()
            time.sleep(0.5)
        blue_pos += 1

    str_blue_pos = str(blue_pos)
    if board_data[str_blue_pos][0] == "snake" or board_data[str_blue_pos][0] == "ladder":
        blue.goto(-192, -165)
        blue_pos = 0
        blue_dir = 1
        for i in range(board_data[str_blue_pos][1]):
            if blue_pos != 0 and blue_pos % 10 == 0:
                blue.setheading(90)
                blue.forward(35)
                blue_dir = -blue_dir
            else:
                if blue_dir == 1:
                    blue.setheading(0)
                elif blue_dir == -1:
                    blue.setheading(180)
                blue.forward(35)
            blue_pos += 1
    if blue_pos == 100:
        reply = window.textinput(player_1 + "won", "End of Game \n Type (y/n) if you want to play again")
        if reply == "" or reply is None or reply == "y":
            window.resetscreen()
            blue_dice.hideturtle()
            red_dice.hideturtle()
            blue.hideturtle()
            red.hideturtle()
            window.bgpic("nopic")
            mode = ""
        elif reply == "n":
            window.resetscreen()
            dummy.write("Click Anywhere and the window will close", False, "center",
                        ("Lucida Calligraphy", 10, "normal"))
            quit = True
            return
        home(1, 1)
        return

    return random_play


def computer_Play(depth=0):
    global red, turn, red_start, red_pos, red_dir, mode, quit
    if red_start:  # Checks if it is start or first move
        red.goto(-192, -165)
        red_start = False
    random_play = random.randint(1, 6)  # Dice Throw
    red_dice.showturtle()
    if random_play == 1:
        red_dice.shape("Assets/red_one.gif")
    elif random_play == 2:
        red_dice.shape("Assets/red_two.gif")
    elif random_play == 3:
        red_dice.shape("Assets/red_three.gif")
    elif random_play == 4:
        red_dice.shape("Assets/red_four.gif")
    elif random_play == 5:
        red_dice.shape("Assets/red_five.gif")
    elif random_play == 6:
        red_dice.shape("Assets/red_six.gif")
    for i in range(random_play):
        if red_pos == 100:
            break
        if red_pos != 0 and red_pos % 10 == 0:  # If the coin has to go up
            red.setheading(90)
            red.forward(35)
            red_dir = -red_dir
            window.update()
            time.sleep(0.5)
        else:  # If coin instead has to go to left or right
            if red_dir == 1:
                red.setheading(0)
            elif red_dir == -1:
                red.setheading(180)
            red.forward(35)
            window.update()
            time.sleep(0.5)
        red_pos += 1
    str_red_pos = str(red_pos)
    if board_data[str_red_pos][0] == "snake" or board_data[str_red_pos][0] == "ladder":
        pre_red_data = board_data[str_red_pos]
        red.goto(-192, -165)
        red_pos = 0
        red_dir = 1
        for i in range(pre_red_data[1]):
            if red_pos != 0 and red_pos % 10 == 0:
                red.setheading(90)
                red.forward(35)
                red_dir = -red_dir
            else:
                if red_dir == 1:
                    red.setheading(0)
                elif red_dir == -1:
                    red.setheading(180)
                red.forward(35)
            red_pos += 1
    if red_pos == 100:
        reply = window.textinput(player_2 + " won", "End of Game \n Type (y/n) if you want to play again")
        if reply == "" or reply is None or reply == "y":
            blue_dice.hideturtle()
            red_dice.hideturtle()
            blue.hideturtle()
            red.hideturtle()
            window.onclick(play)
            window.onkey(guide, "H")
            window.onkey(guide, "h")
            window.listen()
            window.update()
            window.resetscreen()
            window.bgpic("nopic")
            mode = ""
        elif reply == "n":
            dummy.write("Click Anywhere and the window will close", False, "center",
                        ("Lucida Calligraphy", 10, "normal"))
            quit = True
            return
        home(1, 1)
        return
    if random_play == 6:
        if depth < 2:
            computer_Play(depth + 1)


def home(x, y):
    global dummy, window
    window.resetscreen()
    dummy.hideturtle()
    dummy.penup()
    dummy.goto(-100, 100)
    dummy.pendown()
    dummy.fillcolor(250, 51, 62)
    dummy.begin_fill()
    dummy.forward(200)
    dummy.circle(23, 90)
    dummy.forward(50)
    dummy.circle(23, 90)
    dummy.forward(200)
    dummy.circle(23, 90)
    dummy.forward(50)
    dummy.circle(23, 90)
    dummy.end_fill()
    dummy.penup()
    dummy.goto(0, 138)
    dummy.write("vs Player", False, "center", ("Lucida Calligraphy", 18, "normal"))

    dummy.penup()
    dummy.goto(-100, -100)
    dummy.pendown()
    dummy.fillcolor(33, 212, 236)
    dummy.begin_fill()
    dummy.forward(200)
    dummy.circle(23, 90)
    dummy.forward(50)
    dummy.circle(23, 90)
    dummy.forward(200)
    dummy.circle(23, 90)
    dummy.forward(50)
    dummy.circle(23, 90)
    dummy.end_fill()
    dummy.penup()
    dummy.goto(0, -62)
    dummy.write("vs Computer", False, "center", ("Lucida Calligraphy", 18, "normal"))

    dummy.penup()
    dummy.goto(-100, -220)
    dummy.pendown()
    dummy.fillcolor(8, 242, 110)
    dummy.begin_fill()
    dummy.forward(200)
    dummy.circle(23, 90)
    dummy.forward(25)
    dummy.circle(23, 90)
    dummy.forward(200)
    dummy.circle(23, 90)
    dummy.forward(25)
    dummy.circle(23, 90)
    dummy.end_fill()
    dummy.penup()
    dummy.goto(0, -200)
    dummy.write("How to play", False, "center", ("Lucida Calligraphy", 18, "normal"))
    window.update()


def play(x, y):
    global blue_pos, red_pos, turn, blue_start, red_start, red_dir, blue_dir, board_data, player_1, player_2, mode, player_name, player_6_counter, red_6_counter, blue_6_counter, quit, last_mode, redraw

    window.onclick(None)
    window.onkey(None, "H")
    window.onkey(None, "h")

    redraw = False
    computer_circle_center_list = [(-100, -77), (123, -77), (123, -27), (-123, -27)]
    inside_computer_button = False
    for i in computer_circle_center_list:
        if (((x - i[0]) ** 2) + ((y - i[1]) ** 2)) < (23 ** 2):  # (x - center_x^2) + (y - center_y^2) < radius^2
            inside_computer_button = True
    inside_circle = False
    center_corner_circles = [(100, 123), (100, 173), (-100, 172), (-100, 123)]
    for i in center_corner_circles:
        if (((x - i[0]) ** 2) + ((y - i[1]) ** 2)) < (23 ** 2):
            inside_circle = True
    how_play_corner_circles = [(-100, -152), (100, -152), (100, -177), (-100, -177)]
    inside_how_play = False
    for i in how_play_corner_circles:
        if (((x - i[0]) ** 2) + ((y - i[1]) ** 2)) < (23 ** 2):
            inside_how_play = True


    if (((100 > x > -100) and (196 > y > 100)) or inside_circle or (
            (123 > x > -122) and (173 > y > 123))) and mode == "":  # Player Vs Player Mode
        player_1 = window.textinput("Player 1 Name", "Player 1 please enter your name: ")
        player_2 = window.textinput("Player 2 Name", "Player 2 please enter your name: ")
        if player_1 is None or player_1 == "":
            player_1 = "Player 1"
        if player_2 is None or player_2 == "":
            player_2 = "Player 2"
        window.resetscreen()
        mode = "P"
        setup()
        global blue, red, blue_dice, red_dice
        window.update()

    elif (-23 < x < 23) and (-240 < y < -195) and mode == "P":  # Blue dice roll
        PvPBlueTurn()
    elif (-23 < x < 23) and (195 < y < 240) and mode == "P":  # Red dice roll
        PvPRedTurn()

    if (((-100 < x < 100) and (-100 < y < -4)) or (
            (-123 < x < 123) and (-77 < y < -27)) or inside_computer_button) and mode == "":
        player_name = window.textinput("Player Name", "What is your name player?")
        if player_name == "" or player_name is None:
            player_name = "Player"
        window.resetscreen()
        mode = "C"
        setup()
        window.update()

    elif (-23 < x < 23) and (-240 < y < -195) and mode == "C":  # Blue dice roll
        dice_roll = player_Play()
        if quit:
            turtle.bye()
        if dice_roll == 6:
            player_6_counter += 1
            if quit:
                turtle.bye()
            if player_6_counter == 3:
                computer_Play()
                player_6_counter = 0
                if quit:
                    turtle.bye()
        else:
            computer_Play()
            if quit:
                turtle.bye()
    elif (((-100 < x < 100) and (-220 < y < -129)) or (
            (-123 < x < 123) and (-177 < y < -154)) or inside_how_play) and mode == "":
        guide()

    elif (mode == "G"):
        window.resetscreen()
        redraw = True
        mode = last_mode
        if last_mode == "":
            home(1, 1)
        else:
            setup()
        redraw = False

    if not quit:
        window.update()
        window.onclick(play)
        window.onkey(guide, "H")
        window.onkey(guide, "h")
        window.listen()
    if quit:
        return


# Game Data

board_data = {
    "1": ["ladder", 38],
    "2": ["empty"],
    "3": ["empty"],
    "4": ["ladder", 14],
    "5": ["empty"],
    "6": ["empty"],
    "7": ["empty"],
    "8": ["ladder", 30],
    "9": ["empty"],
    "10": ["empty"],
    "11": ["empty"],
    "12": ["empty"],
    "13": ["empty"],
    "14": ["empty"],
    "15": ["empty"],
    "16": ["empty"],
    "17": ["empty"],
    "18": ["empty"],
    "19": ["empty"],
    "20": ["empty"],
    "21": ["ladder", 42],
    "22": ["empty"],
    "23": ["empty"],
    "24": ["empty"],
    "25": ["empty"],
    "26": ["empty"],
    "27": ["empty"],
    "28": ["ladder", 76],
    "29": ["empty"],
    "30": ["empty"],
    "31": ["empty"],
    "32": ["snake", 10],
    "33": ["empty"],
    "34": ["empty"],
    "35": ["empty"],
    "36": ["snake", 6],
    "37": ["empty"],
    "38": ["empty"],
    "39": ["empty"],
    "40": ["empty"],
    "41": ["empty"],
    "42": ["empty"],
    "43": ["empty"],
    "44": ["empty"],
    "45": ["empty"],
    "46": ["empty"],
    "47": ["empty"],
    "48": ["snake", 26],
    "49": ["empty"],
    "50": ["ladder", 67],
    "51": ["empty"],
    "52": ["empty"],
    "53": ["empty"],
    "54": ["empty"],
    "55": ["empty"],
    "56": ["empty"],
    "57": ["empty"],
    "58": ["empty"],
    "59": ["empty"],
    "60": ["empty"],
    "61": ["empty"],
    "62": ["snake", 18],
    "63": ["empty"],
    "64": ["empty"],
    "65": ["empty"],
    "66": ["empty"],
    "67": ["empty"],
    "68": ["empty"],
    "69": ["empty"],
    "70": ["empty"],
    "71": ["ladder", 92],
    "72": ["empty"],
    "73": ["empty"],
    "74": ["empty"],
    "75": ["empty"],
    "76": ["empty"],
    "77": ["empty"],
    "78": ["empty"],
    "79": ["empty"],
    "80": ["ladder", 99],
    "81": ["empty"],
    "82": ["empty"],
    "83": ["empty"],
    "84": ["empty"],
    "85": ["empty"],
    "86": ["empty"],
    "87": ["empty"],
    "88": ["snake", 24],
    "89": ["empty"],
    "90": ["empty"],
    "91": ["empty"],
    "92": ["empty"],
    "93": ["empty"],
    "94": ["empty"],
    "95": ["snake", 56],
    "96": ["empty"],
    "97": ["snake", 78],
    "98": ["empty"],
    "99": ["empty"],
    "100": ["Winner"]
}

# Setting screen
window = turtle.Screen()
window.colormode(255)
window.title("Home_Page")
window.setup(500, 500)
window.setworldcoordinates(-250, -250, 250, 250)
window.bgcolor(50, 168, 82)
window.tracer(0)

dummy = turtle.Turtle()
home(1, 1)

window.onclick(play)
window.onkey(guide, "H")
window.onkey(guide, "h")
window.listen()
turtle.mainloop()
