# har har mahadev

import turtle
import time
import random
import sys
import winsound

#Setting up turtle screen
screen = turtle.Screen()
screen.setup(800,700)
screen.setworldcoordinates(-400,-400,400,400)

winsound.PlaySound("intro_music.wav", winsound.SND_ASYNC)

# intro animation 1
turtle.addshape("yc.gif")
turtle.addshape("yc(1).gif")
turtle.addshape("yc(2).gif")
turtle.addshape("yc(3).gif")
turtle.addshape("yc(4).gif")
turtle.addshape("yc(5).gif")
turtle.addshape("yc(6).gif")
turtle.addshape("yc(7).gif")
turtle.shape("yc.gif")
time.sleep(0.1)
turtle.shape("yc(1).gif")
time.sleep(0.1)
turtle.shape("yc(2).gif")
time.sleep(0.1)
turtle.shape("yc(3).gif")
time.sleep(0.1)
turtle.shape("yc(4).gif")
time.sleep(0.1)
turtle.shape("yc(5).gif")
time.sleep(0.1)
turtle.shape("yc(6).gif")
time.sleep(0.1)
turtle.shape("yc(7).gif")
time.sleep(2)

# intro animation 2
turtle.addshape("RoboRescue_main.gif")
turtle.addshape("RoboRescue_main (5).gif")
turtle.addshape("RoboRescue_main (4).gif")
turtle.addshape("RoboRescue_main (3).gif")
turtle.addshape("RoboRescue_main (2).gif")
turtle.addshape("RoboRescue_main (1).gif")
turtle.shape("RoboRescue_main (5).gif")
time.sleep(0.1)
turtle.shape("RoboRescue_main (4).gif")
time.sleep(0.1)
turtle.shape("RoboRescue_main (3).gif")
time.sleep(0.1)
turtle.shape("RoboRescue_main (2).gif")
time.sleep(0.1)
turtle.shape("RoboRescue_main (1).gif")
time.sleep(0.1)
turtle.shape("RoboRescue_main.gif")
time.sleep(0.1)
screen.update()
time.sleep(2)
screen.clear()
screen.bgpic("paper.gif")

# initializing turtles for game2()
hammer = turtle.Turtle()
spanner = turtle.Turtle()
tape = turtle.Turtle()
note = turtle.Turtle()
notemaker = turtle.Turtle()

#initializing turtles for skip
turtle.addshape("quit.gif")
turtle.addshape("Skip.gif")
skipT = turtle.Turtle()
skipT.shape("Skip.gif")
skipT.ht()
skipT.pu()
skipT.goto(-350, -382)
skipT.st()

#initializing turtles for exit
exitT = turtle.Turtle()
exitT.shape("quit.gif")
exitT.ht()
exitT.pu()
exitT.goto(350, -382)
exitT.st()

skipflag = False  # skipflag turns true when skip is pressed
player_name = ""  # to store the name of the player
flag = 0  # this flag is used to check if the player has found the right object in game2
flag2 = 0  # flag2 is used in game4 to find and display the result
win_check = 0  # this flag is for checking win in the game2
flag10 = 0 #for checking if hammer is pressed in game2
flag11 = 0# for checking if spanner is pressed in game2
flag12 = 0# for checking if tape is clicked in game2
ans = 0# cheking if there are three wins in game2

wires = turtle.Turtle()
tools = turtle.Turtle()
motor = turtle.Turtle()
health_bar = turtle.Turtle()
instructor = turtle.Turtle()
"""
isSkipPressed function changes the value of skipflag to true and it returns skipflag
"""
def isSkipPressed(x,y):
    global skipflag
    skipflag = True
    return(skipflag)

"""
isExitPressed function exits the game screen 
"""
def isExitPressed(x,y):
    screen.clear()
    outro()
    turtle.bye()

"""
buttonClicked function checks whether skip or exit button is pressed if yes it calls the respective functions
"""
def buttonClicked():
    skipT.onclick(isSkipPressed)
    exitT.onclick(isExitPressed)


"""
write function helps us to write the text using turtle.write() in an animatic way using sleep . The arguments are plot(story or content we want it to display),
x(x coordinate of the starting of text) , y(y coordinate of the starting of text),o (used for differently spacing the text in the second iteration), colour(colour of the text),
font(font of the text), type(normal,bold,italic), size(size of the font), flag(to check if buttonClicked should be run or not, flag==0(not to be run),flag ==1(to be run))
"""
def write(plot, x, y, o, colour, font, type, size , flag):
    global skipflag

    turtle.pu()

    turtle.pencolor(colour)

    turtle.goto(x,y)
    for i in range(0,len(plot)):
        turtle.ht()

        # this part checks if flag is 1 it then calls the buttonClicked function if skipflag is changed to one after the buttonClicked function is run then it returns from the function
        if flag == 1:
            buttonClicked()
            if skipflag == True:
                return

        turtle.write(plot[i], move=False, align="left", font=(font, size, type))
        time.sleep(2)

        turtle.goto(o,y-30)
        y = y-40#to write the text in the next line


"""
locate moves the mapmarker as and on the game proceeds . it takes the argument pos to identify at which location it is called so that it can map the further route.
"""
def locate(pos):
    map_marker = turtle.Turtle()
    map_marker.ht()
    map_marker.pu()
    map_marker.shape("circle")
    map_marker.pencolor("red")
    map_marker.pensize(5)

    if pos == 1:
        map_marker.goto(250, 200)
        screen.bgpic("Map.gif")
        map_marker.st()
        map_marker.pd()
        map_marker.pensize(5)
        map_marker.right(90)
        map_marker.forward(225)
        map_marker.right(90)
        map_marker.forward(475)
        time.sleep(1)
    if pos == 2:
        map_marker.pu()
        map_marker.goto(-235, -15)
        map_marker.right(180)
        map_marker.pd()
        screen.bgpic("Map.gif")
        map_marker.st()
        map_marker.clear()
        map_marker.right(180)
        map_marker.forward(325)
        map_marker.left(90)
        map_marker.forward(250)
        map_marker.left(90)
        map_marker.forward(80)
        time.sleep(1)
    if pos == 3:
        map_marker.pu()
        map_marker.goto(20, 230)
        map_marker.left(180)
        map_marker.pd()
        screen.bgpic("Map.gif")
        map_marker.st()
        map_marker.clear()
        map_marker.right(180)
        map_marker.forward(80)
        map_marker.right(90)
        map_marker.forward(250)
        map_marker.left(90)
        map_marker.forward(155)
        map_marker.left(90)
        map_marker.forward(225)
"""
intro function displays the storyline in the beggining of the game.
"""
def intro():
    global skipflag,player_name

    screen.bgpic("paper.gif")
    player_name = turtle.textinput("Enter player's name","What's your character's name?")# getting players name

    story =[["Dear Diary,",str(player_name) + " here!! "," After all these years today is the day I will achieve my dream.", " I have always wanted to build my own robot." , "And I will finally do it with e-yan today." , "I have built him from scratch, and today I just have to charge him." , "Will update what happened later.","Bye "],
            ["Dear Diary, ",  "It’s " + str(player_name) + " again", " All was going perfectly until I tried to charge it."," Suddenly there was a loud ‘BANG!’ and the lights went out."," And sadly, even e-yan shut down."," But, even after the lights came back on", "I was still shocked and didn’t know what to do."," In a daze, I went to ask Professor Shreedhar for help. And he said…"],
            ["Hmmm.." + str(player_name), " Did you overload the power supply?"," Because this looks like a short circuit.", "You need to get more supplies "],
            [" You will find some new wires in the ", "computer lab", " some other basic tools in the mechanical lab,","and motors in the robotics lab"," after finding all this, come back to me."]
            ]#Nested list of the contents to be presented on the screen
    coordinates=[-350,250,-350,-350,-50,-350,-170,330,-170,-170,330,-170]# list of the coordinates of the content
    coord = 0#variable to access coordinates from the coordinates list

    for plot in range(0,2):
        if skipflag == True:
            coord+=3
            break
        write(story[plot],coordinates[coord],coordinates[coord+1],coordinates[coord+2],"blue","Lucida Handwriting","italic",13,1)
        coord += 3


    for plot in range(0,2):
        screen.clear()
        screen.bgpic("prof1.gif")
        write(story[plot+2], coordinates[coord], coordinates[coord + 1], coordinates[coord + 2], "black","Book Antiqua","normal",13,0)

        coord += 3

    skipflag = False
    return()

"""
This function is the first sub game of the plot...guess the online shopping site.
"""
def game1(image):

    random.shuffle(image)# shuffles the image list so that the sites are not displayed in the same order
    screen.clear()
    screen.bgpic(image[0][0])# to set the firstpicture of the site as background picture
    name = screen.textinput("Now we have to collect the wires", "Enter the name of the online shopping site whose logo is displayed")
    #If the answer entered by the player is equal to the answer in the same list in the index 1, it exits the function
    if name.lower() == image[0][1]:
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)
        image.remove(image[0])
        turtle.ht()
        turtle.pu()
        turtle.goto(-50,0)
        turtle.pd()
        plot = ["That was the right answer!!!!", "The wires have been ordered!"]
        write(plot, -200, -40, -200, "navy", "Book Antiqua", "bold",20,0)
        time.sleep (3)
        pass
    else:
        #If the answer entered by the player is not same it gives the player three chances. After three chances it exits from the game
        image.remove(image[0])
        if len(image) < 3:
            winsound.PlaySound("mario_dies.wav", winsound.SND_ASYNC)
            plot = ["Unfortunately you could not guess any of the sites ...", "Better luck saving e-yan next time"]
            write(plot, -320, -40, -200, "navy", "Book Antiqua", "bold", 20, 0)
            choice()
        winsound.PlaySound("wrong.wav", winsound.SND_ASYNC)
        plot = ["Unfortunately you could not guess the site... ","lets move on to the next site"]
        write(plot, -320, -40, -200, "navy", "Book Antiqua", "bold",20,0)
        game1(image)
    screen.clear()
    time.sleep (1)

"""
This function is the second sub game in our plot .... find the objects. It contains three tools to be found tape,hammer,spanner
"""
def game2():
    global win_check,flag,flag10,flag11,flag12,ans
    shuffle = turtle.Turtle()
    shuffle.ht()
    shuffle.pu()
    turtle.addshape("shuffle.gif")
    shuffle.shape("shuffle.gif")
    shuffle.goto(-350, -290)
    shuffle.st()

    exitT = turtle.Turtle()
    exitT.shape("quit.gif")
    exitT.ht()
    exitT.pu()
    exitT.goto(100, -300)
    exitT.st()

    hammer.ht()
    tape.ht()
    spanner.ht()

    screen.bgpic("BG.gif")
    screen.tracer()
    turtle.addshape("note (1).gif")
    note.shape("note (1).gif")
    note.st()
    note.pu()
    note.goto(280,-270)
    notemaker.pu()

    tape_places = [(-365, -200), (55, 250)]#two coordinates for tape turtle is given
    tape_cors = random.choice(tape_places)#choice is made between the two available by the random function which is stored in tape_cors function

    hammer_places = [(180, 140), (-365, 345)]#two coordinates for hammer turtle is given
    hammer_cors = random.choice(hammer_places)#choice is made between the two available by the random function which is stored in hammer_cors function

    spanner_places = [(350, 290), (-180, 230)]#two coordinates for spaner turtle is given
    spanner_cors = random.choice(spanner_places)#choice is made between the two available by the random function which is stored in spanner_cors function

    if flag10 != 1:# if hammer is not clicked
        #initializing hammer turtle
        turtle.addshape("hammer (1).gif")
        hammer.shape("hammer (1).gif")
        hammer.shapesize(5)
        hammer.pu()
        hammer.ht()
        hammer.goto(hammer_cors)
        hammer.st()

    if flag12 != 1:# if tape is not clicked
        #initializing tape turtle
        turtle.addshape("tape.gif")
        tape.shape("tape.gif")
        tape.shapesize(1)
        tape.pu()
        tape.ht()
        tape.goto(tape_cors)
        tape.st()

    if flag11 != 1:# if spanner is not clicked
        #initializing spanner turtle
        turtle.addshape("spanner.gif")
        spanner.shape("spanner.gif")
        spanner.shapesize(1)
        spanner.pu()
        spanner.ht()
        spanner.goto(spanner_cors)
        spanner.st()

    turtle.addshape("tick.gif")

    correct = turtle.Turtle()
    correct.shape("tick.gif")
    correct.ht()

    correct1 = turtle.Turtle()
    correct1.shape("tick.gif")
    correct1.ht()

    correct2 = turtle.Turtle()
    correct2.shape("tick.gif")
    correct2.ht()

    screen.update()

    """
    If the player finds all the three tools then the win audio is played. If win_check is greater than two that means the player has found all the tools.
    """
    def checkforWin():
        global win_check,ans
        if win_check > 2:
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            ans = 1


    """
    The function plays the "correct" audio and strikes hammer fom the to find list and increments win_check variable by one
    """
    def isHammerFound(x,y):
        global flag, win_check,flag10
        winsound.PlaySound("correct.wav", winsound.SND_ASYNC)
        flag = 1
        flag10 = 1
        win_check = win_check + 1
        correct.st()
        correct.pu()
        correct.goto(160,-325)
        hammer.ht()
        checkforWin()

    """
    The function plays the "correct" audio and strikes spanner fom the to find list and increments win_check variable by one
    """
    def isSpannerFound(x,y):
        global flag, win_check,flag11
        winsound.PlaySound("correct.wav", winsound.SND_ASYNC)
        flag = 2
        flag11 = 1
        win_check = win_check + 1
        correct1.st()
        correct1.pu()
        correct1.goto(160,-245)
        spanner.ht()
        checkforWin()

    """
    The function plays the "correct" audio and strikes hammer fom the to find list and increments win_check variable by one
    """
    def isTapeFound(x,y):
        global flag, win_check,flag12
        winsound.PlaySound("correct.wav", winsound.SND_ASYNC)
        flag = 3
        flag12 = 1
        win_check = win_check + 1
        checkforWin()
        correct2.st()
        correct2.pu()
        correct2.goto(160,-285)
        tape.ht()
        checkforWin()

    """
    This function checks if flag is less than 1 is yes it plays the "click" audio indicating the tool chosed is wrong. It resets flag to 0.
    """
    def isScreenTouching(x,y):
        global flag
        if flag < 1:
            winsound.PlaySound("click.wav", winsound.SND_ASYNC)

    def isShufflePressed(x,y):
        game2()


    #This part calls the necessary function when the tools are clicked upon
    while win_check < 3:
        hammer.onclick(isHammerFound)
        if ans == 1:
            break
        screen.update()
        spanner.onclick(isSpannerFound)
        if ans == 1:
            break
        screen.update()
        tape.onclick(isTapeFound)
        if ans == 1:
            break
        screen.update()
        screen.onclick(isScreenTouching)
        shuffle.onclick(isShufflePressed)
        exitT.onclick(isExitPressed)
    note.ht()
    correct.ht()
    correct1.ht()
    correct2.ht()
    shuffle.ht()
    exitT.ht()

    pass


"""
This function is the third sub game of the plot...Unscramble the words
"""
def game3(flag1,word,order):

    screen.clear()
    screen.bgpic("roboBackground.png")
    turtle.pu()
    turtle.ht()
    word1 = [["s", "e", "n", "s", "o", "r"], "sensor"]#nested list of the letters and answer of 1st word
    word2 = [["e", "n", "g", "i", "n", "e"], "engine"]#nested list of the letters and answer of 2nd word
    word3 = [["g", "a", "d", "g", "e", "t"], "gadget"]#nested list of the letters and answer of 3rd word
    order = [word1, word2, word3]#list of all three words
    turtle.pu()
    turtle.ht()
    if flag1 == 0:
        word = (random.choice(order))#the random choice of one of the words in order list is stored in word variable

    random.shuffle(word[0])#shuffles the letters of the word chosen

    #to present the jumbled letters with suitable gaps
    for i in range(0, 6):
        turtle.goto(-300 + (i * 50), 30)
        turtle.write(word[0][i], move=False, align="center", font=("Arial", 100, "normal"))
        time.sleep(1)
        turtle.clear()

    ans = turtle.textinput("Unscramble the word :", word[0])
    # If the answer entered by the player is equal to the answer in the same list at index position 1, it returns from the function
    if ans.lower() == str(word[1]):
        #turtle.clear()
        winsound.PlaySound("correct .wav", winsound.SND_ASYNC)
        turtle.goto(0, 0)
        plot = ["Great job!! You got the right answer.", "You got the motors"]
        write(plot, -330, 100, -230, "navy", "Book Antiqua", "bold", 20, 0)
        pass

    # if the answer entered by the player is not equal to the answer in the same list it rewrites the same word in different order. This goes on for three chances and then breaks from the game loop
    if ans.lower() != str(word[1]):
        #turtle.clear()
        winsound.PlaySound("wrong.wav", winsound.SND_ASYNC)
        turtle.goto(0, 0)
        flag1 += 1
        if flag1 == 3:
            winsound.PlaySound("mario_dies.wav", winsound.SND_ASYNC)
            plot = ["Unfortunately you could not guess the word ...", "Better luck saving e-yan next time"]
            write(plot, -350, 100, -230, "navy", "Book Antiqua", "bold", 20, 0)
            choice()
        plot = ["Oh no ... That is not the right answer.", "Try again"]
        write(plot, -350, 100, -230, "navy", "Book Antiqua", "bold", 20, 0)
        turtle.clear()
        game3(flag1,word,order)

"""
This function is the 4th sub game of the plot ... drag and drop.
"""
def game4(show,wires ,tools,motor):
    global player_name,flag2
    screen.tracer()
    screen.bgpic("game4.png")
    turtle.penup()
    turtle.goto(0,190)
    if show == 0:

        # adding various gifs
        turtle.addshape("empty_bar.gif")
        turtle.addshape("half_bar.gif")
        turtle.addshape("little_bar.gif")
        turtle.addshape("full_bar.gif")
        turtle.addshape("e-yan.gif")
        turtle.addshape("e-yan1.gif")
        turtle.addshape("e-yan2.gif")
        turtle.addshape("e-yan3.gif")
        turtle.addshape("Wires.gif")
        turtle.addshape("Toolbox.gif")
        turtle.addshape("Motors.gif")
        turtle.shape("e-yan.gif")

        #initializing wires turtle
        wires.shape("Wires.gif")
        wires.pu()
        wires.goto(260, 150)
        wires.st()

        #initializing tools turtle
        tools.shape("Toolbox.gif")
        tools.pu()
        tools.goto(240, -90)
        tools.st()

        # initializing motor turtle
        motor.shape("Motors.gif")
        motor.pu()
        motor.goto(-260, -90)
        motor.st()

        turtle.shapesize(1)


        # initializing health_bar turtle
        health_bar.pu()
        health_bar.shape("empty_bar.gif")
        health_bar.goto(0, -315)

        # initializing instructor turtle
        instructor.ht()
        instructor.pu()
        instructor.goto(0, 350)
        instructor.write("Instructions:" + "Drag and drop the tools for eYan to be fixed", font=("calibri", 15, "normal"),
                         align="center")
        screen.update()
    #If flag is equal to 0 then, empty_bar.gif is set as the pic for health_bar turtle
    if flag2 == 0:
        health_bar.shape("empty_bar.gif")
        screen.update()
        instructor.clear()
        instructor.write("Instructions:" + "Drag and drop the tools for eYan to be fixed",
                            font=("calibri", 15, "normal"), align="center")
        screen.update()

    # If flag is equal to 1 then, little_bar.gif is set as the pic for health_bar turtle
    if flag2 == 1:
        turtle.shape("e-yan1.gif")
        health_bar.shape("little_bar.gif")
        screen.update()
        instructor.clear()
        instructor.write("Nice", font=("calibri", 30, "normal"), align="center")
        screen.update()

    # If flag is equal to 2 then, half_bar.gif is set as the pic for health_bar turtle
    if flag2 == 2:
        turtle.shape("e-yan2.gif")
        health_bar.shape("half_bar.gif")
        screen.update()
        instructor.clear()
        instructor.write("very Nice", font=("caibri", 30, "normal"), align="center")
        screen.update()

    # If flag is equal to 3 then, full_bar.gif is set as the pic for health_bar turtle and flag is incremented by 1
    if flag2 == 3:
        turtle.shape("e-yan3.gif")
        health_bar.shape("full_bar.gif")
        screen.update()
        instructor.clear()
        instructor.write("You're all done!!!",
                             font=("caibri", 15, "normal"), align="center")
        flag2 += 1
        screen.update()

    # this recursive function helps us to update the position of the wires as we drag it
    def drag_and_drop_wires(x, y):
        global flag2
        wires.ondrag(None)
        wires.goto(x, y)
        wires.ondrag(drag_and_drop_wires)

    # this recursive function helps us to update the position of the tools as we drag it
    def drag_and_drop_tools(x, y):
        global flag2
        tools.ondrag(None)
        tools.goto(x, y)
        tools.ondrag(drag_and_drop_tools)

    # this recursive function helps us to update the position of the motor as we drag it
    def drag_and_drop_motor(x, y):
        global flag2
        motor.ondrag(None)
        motor.goto(x, y)
        motor.ondrag(drag_and_drop_motor)

    # This function checks the distance between the turtle and motor once motor is released, if it is less than 60 it increments flag2 by one
    def onReleaseofMotor(x, y):
        global flag2
        if motor.distance(turtle.pos()) < 60:
            motor.ht()
            motor.goto(1000, 1000)
            flag2 += 1
            game4(1,wires,tools,motor)
            screen.update()

    # This function checks the distance between the turtle and tols once tools is released, if it is less than 60 it increments flag2 by one
    def onReleaseofTools(x, y):
        global flag2
        if tools.distance(turtle.pos()) < 60:
            tools.ht()
            tools.goto(1000, 1000)
            flag2 += 1
            game4(1,wires,tools,motor)
            screen.update()

    # This function checks the distance between the turtle and wires once wires is released, if it is less than 60 it increments flag2 by one
    def onReleaseofWires(x, y):
        global flag2
        if wires.distance(turtle.pos()) < 60:
            wires.ht()
            wires.goto(1000, 1000)
            flag2 += 1
            game4(1,wires,tools,motor)
            screen.update()

    # while flag2 is less than 4 ,if we drag the particular tool corresponding function  and when particular tool is released then the corresponding function is called
    while flag2 < 4:
        wires.ondrag(drag_and_drop_wires)
        screen.update()
        tools.ondrag(drag_and_drop_tools)
        screen.update()
        motor.ondrag(drag_and_drop_motor)
        screen.update()
        motor.onrelease(onReleaseofMotor)
        screen.update()
        wires.onrelease(onReleaseofWires)
        screen.update()
        tools.onrelease(onReleaseofTools)
    turtle.pd()
    return

"""
end function displays the ending plot of the game
"""
def end():
    screen.bgpic("paper.gif")
    plot = ["And this is how I was able to achieve my dream."," My robot, E-yan is now a fully functional robot and is helping many students"," with school-based tutoring in subjects such as math and science."," This journey of mine has been very memorable to me and I wanted to keep a"," record  of it, hence I have written this diary."," I will write again when another journey comes up. Until then,","Goodbye Dear Diary"]
    write(plot,-375,100,-375, "blue", "Lucida Handwriting","italic", 13, 0)
    screen.clear()
    return

"""
outro function displays the ending animation of the game
"""
def outro():
    winsound.PlaySound("outro_music.wav", winsound.SND_ASYNC)
    turtle.addshape("cy.gif")
    turtle.addshape("cy(1).gif")
    turtle.addshape("cy(2).gif")
    turtle.addshape("cy(3).gif")
    turtle.addshape("cy(4).gif")
    turtle.addshape("cy(5).gif")
    turtle.addshape("cy(6).gif")
    turtle.addshape("cy(7).gif")
    turtle.shape("cy.gif")
    time.sleep(2)
    turtle.shape("cy(1).gif")
    time.sleep(0.1)
    turtle.shape("cy(2).gif")
    time.sleep(0.1)
    turtle.shape("cy(3).gif")
    time.sleep(0.1)
    turtle.shape("cy(4).gif")
    time.sleep(0.1)
    turtle.shape("cy(5).gif")
    time.sleep(0.1)
    turtle.shape("cy(6).gif")
    time.sleep(0.1)
    turtle.shape("cy(7).gif")
    time.sleep(1)

"""
This function asks whether the player wants to play again or quit . If the answer is yes it will run the game from game1.
If the answer is no it exits from the game while playing outro music.
"""
def choice ():
    global skipflag,flag,flag2,win_check,flag10,flag11,flag12,ans
    input = turtle.textinput("Do you want to play again ?","Yes / No")
    skipflag = False  # skipflag turns true when skip is pressed
    flag = 0  # this flag is used to check if the player has found the right object in game2
    flag2 = 0  # flag2 is used in game4 to find and display the result
    win_check = 0  # this flag is for checking win in the game2
    flag10 = 0  # for checking if hammer is pressed in game2
    flag11 = 0  # for checking if spanner is pressed in game2
    flag12 = 0  # for checking if tape is clicked in game2
    ans = 0  # cheking if there are three wins in game2

    if input.lower() == "yes":
        main()
    elif input.lower() == "no":
        screen.clear()
        outro()
        sys.exit()

"""
main funcion is the function in which all the functions are called in the correct order of execution
"""
def main():
    order = ""
    flag1 = 0  # flag is used in game3 to find the number of turns the player has played
    word = ""  # to store the random selection in game 3
    image = [["amazon.gif", "amazon"], ["snapdeal.gif", "snapdeal"], ["flipkart.gif", "flipkart"],
             ["jioMart.gif", "jio mart"], ["cliq.gif", "tata cliq"]]  # list of sites and images for game1()


    locate(1)
    screen.clear()
    screen.bgpic("board.png")
    plot = ["Level 1 : Guess the logo ", "Destination : Computer Lab ", "How to play?: To order the wires ,",
            "guess the name of the online shopping site through their logo  ","(If the answer has multiple words write ,"," them seperately using spaces)"]
    write(plot, -250, 100, -250, "white", "Segoe Script", "bold", 13, 0)
    time.sleep(2)
    screen.clear()
    game1(image)
    screen.tracer(10)
    screen.clear()
    locate(2)
    screen.clear()
    screen.bgpic("board.png")
    plot = ["Level 2 : Find the objects ", "Destination : Mechanical Lab ",
            "How to play? : Amongst the tool mess in the mechanical lab,",
            "find the tools given in the list which are required to help e-yan"]
    write(plot, -300, 100, -300, "white", "Segoe Script", "bold", 13, 0)
    time.sleep(2)
    screen.clear()
    game2()
    locate(3)
    screen.clear()
    screen.bgpic("board.png")
    plot =["Level 3 : Unscramble The Word ","Destination : Robotics Lab ","How to play?: To obtain the motors","unscramble the word to form an equipment"]
    write(plot, -250, 100, -250, "white", "Segoe Script", "bold", 13, 0)
    game3(flag1,word,order)
    screen.clear()

    screen.bgpic("prof1.gif")
    plot = ["Well done," + str(player_name) + ".", " You have brought everything we need.",
            " Now replace the parts correctly and", " charge e-yan again."]
    write(plot, -170, 340, -170, "black", "Book Antiqua", "bold", 13, 0)
    screen.clear()
    screen.bgpic("prof1.gif")
    plot = [" Reduce the voltage supply this time.", " All the best," + str(player_name),
            " I just know it'll work this time."]
    write(plot, -170, 340, -170, "black", "Book Antiqua", "bold", 13, 0)
    screen.clear()
    screen.bgpic("board.png")
    plot = ["Level 4 : Drag And Drop", "Destination : Robotics Lab ",
            "How to play?: Drag and drop the tools inside e-yan",
            "to finally repair him"]
    write(plot, -250, 100, -250, "white", "Segoe Script", "bold", 13, 0)
    screen.clear()
    game4(0,wires,tools,motor)
    screen.clear()
    end()
    screen.bgpic("ask.png")
    choice()
intro()
screen.clear()
main()
game2()

turtle.mainloop()