
#############-----IMPORTING THE MODULES REQUIRED-----##############
import turtle
import time
import random
import pickle


#############-----DEFINING THE GLOBAL VARIABLES-----##############
# The starting coordinates for the sudoku grid
Start_x = 0
Start_y = 90
length_board = 90 # Length of the board

# The Number of rows and columns in the sudoku grid
rows = 9
col = 9
Life = 3 # Number of wrong turns compromised for the user

# the status for the help button
status = 'hide'

# Initialising the lists required in the program
centre_coord = []
grid_solution = []
board = []


Gameover = False # status of the continuation of the game


start_time = None # initialising the start_time variable

# setting the time elapsed as 0
second = 0
minute = 0
hour = 0

# setting the player name as empty
player = None

def input_names_of_player():
	"""
	Purpose:
	---
	This function is being used to add name of the player.

	Global variables -- player, scrn
	player: name of the player
	scrn; the turtle screen object
	:return: None
	"""
	##############	ADD YOUR CODE HERE	##############
	global player, scrn

	player = scrn.textinput("Welcome To Sudoku", 'Please enter your name')


def input_level():
	"""
		Purpose:
		---
		This function takes the user input for Level and returns it for furthur use.

		Global variables -- None

		:returns: Level
		:rtype: int
	"""
	##############	ADD YOUR CODE HERE	##############
	Level = None
	i = 0

	while Level is None:
		if i >= 5:
			turtle.bye()
			break


		else:
			i += 1
			Level = scrn.numinput('Level Selection', 'Please choose your level(1-5)\n (1 - Easy, 5 - Hard)', minval=1,maxval=5)


	return Level


def Init_screen():
	"""
		Purpose:
		---
		This function performs the initialization of the turtle screen and various turtle variables.

		Global variables -- scrn, turtle, pen, Life_pen, pen_time, Level_pen, scrn_cover, Help_pen
		pen, Life_pen, pen_time, Level_pen, scrn_cover, Help_pen = different turtle objects
		:returns: None

	"""

	global scrn, turtle, pen, Life_pen, pen_time, Level_pen, scrn_cover, Help_pen

	scrn = turtle.Screen()  # Uisng the turtle screen as scr variable

	# setting the screen dimensions, Title, color etc
	scrn.setup(700, 810)
	scrn.title('SUDOKU')
	scrn.setworldcoordinates(0.5, 0.5, 90.5, 109.5)
	scrn.bgcolor('cyan')

	scrn.tracer(0)  #
	# registering an image file for further use
	scrn.register_shape('Assets/sudoku-instructions_21.gif')

	turtle.hideturtle()

	# Initialising other turtles

	# pen
	pen = turtle.Turtle()
	pen.hideturtle()

	# Life_pen
	Life_pen = turtle.Turtle()
	Life_pen.hideturtle()

	# pen_time
	pen_time = turtle.Turtle()
	pen_time.hideturtle()

	# Level_pen
	Level_pen = turtle.Turtle()
	Level_pen.hideturtle()

	# scrn_cover
	scrn_cover = turtle.Turtle()
	scrn_cover.hideturtle()

	# Help_pen
	Help_pen = turtle.Turtle()
	Help_pen.penup()
	Help_pen.goto(45, 45)
	Help_pen.hideturtle()

	Help_pen.shape('Assets/sudoku-instructions_21.gif')  # setting the turtle's shape to an image
	Help_pen.shapesize(1, 1, 10)  # setting the size of the turtle shape


def init_board():
	"""
		Purpose:
		---
		This function performs the initialization of fundamentals of the board like numbers and Life, Level, status etc.

		Global variables -- board, grid_solution, Life

		:returns: None

	"""

	global board, grid_solution, Life

	Level = input_level()  # Getting the user input for level

	if Level is not None:
		level_selected = random.randint(1 + int(30 * (Level - 1)),
										int(30 * Level))  # Using the level to detemine the sudoku grid from 2 files
	else:
		return

	# Operating on the files for getting the grid and board using the pickle module
	with open('Assets/file.txt', 'rb') as fp:
		grid_solution = pickle.load(fp)[level_selected - 1]  # Grid contains the numerical values of all the locations

	with open('Assets/file_2.txt', 'rb') as fp:

		board = pickle.load(fp)[
			level_selected - 1]  # board contains the numerical values of a few locations, to be shown

	# Drawing the Initial Numbers on the sudoku Board

	for i in range(9):
		for j in range(9):
			if board[i][j] != 0:
				draw_number(turtle, i, j, board[i][j], 40)


	# Displaying the Life(s) remaining on the Screen
	Text_Life = 'Life: ' + str(Life)
	write(Life_pen, -0.7, -0.55, Text_Life, 36, 'purple')

	# Displaying the Level selected by the user on the screen
	Text_Level = 'Level: ' + str(int(Level))
	write(Level_pen, -1.7, 5.5, Text_Level, 36, 'blue')

	# Displaying the Help button on the screen
	draw_button(-1.8, 4, '?', Level_pen)

def sudoku_board():
	"""
		Purpose:
		---
		This function is being used to draw the sudoku grid on the screen.

		Global variables -- None

		:returns: None

	"""
	# Moving the turtle to the initial location
	turtle.penup()
	turtle.goto(Start_x, Start_y)

	turtle.pensize(7)  # setting the turtle pen-width

	draw_square(length_board)  # drawing a square using a function

	x, y = turtle.pos()  # getting the turtle's current coordintes as x and y respectively

	# Drawing the smaller sections of the grid
	for i in range(3):
		for j in range(3):
			turtle.penup()
			turtle.goto(x + 30 * j, y)
			turtle.pensize(12)
			turtle.pencolor('red')
			draw_square(length_board / 3)

		y = y - 30

	y = Start_y

	# overlapping the sections for creating an astonishing effect
	for i in range(9):
		for j in range(9):
			turtle.penup()
			turtle.goto(x + 10 * j, y)
			turtle.pensize(7)
			turtle.pencolor('red')
			centre_coord.append((int(x + 10 * j + 5) + 1,
								 int(y - 5)))  # Creating a list of the centre coordinates of the grid section squares
			draw_square(length_board / 9)

		y = y - 10

	y = Start_y
	for i in range(9):
		for j in range(9):
			turtle.penup()
			turtle.goto(x + 10 * j, y)
			turtle.pensize(3)
			turtle.pencolor('orange')

			draw_square(length_board / 9)

		y = y - 10

	# Drawing a ribbon over the sudoku grid separating the grid and the dashboard
	turtle.setheading(0)
	turtle.penup()
	turtle.pencolor('orange')
	turtle.pensize(10)
	turtle.goto(-1, 91.7)
	turtle.fillcolor('orange')
	turtle.begin_fill()
	turtle.pendown()
	turtle.goto(92, 91.7)

	turtle.goto(92, 115)

	turtle.goto(-1, 115)

	turtle.goto(-1, 91.7)
	turtle.end_fill()

	# Updating the screen to see the results
	scrn.update()


def input_number():
	"""
		Purpose:
		---
		This function takes the user input for a number and returns it for further use.

		Global variables -- None

		:returns: num
		:rtype: int
	"""

	num = scrn.numinput('Input!', 'Please input your Num \n i.e(1-9)' ,minval=1 ,maxval=9)


	if num is not None:
		return int(num)
	else:
		return


def write(writer, i, j, text, size, color):
	"""
		Purpose:
		---
		This function is used for writing on the screen using turtle write command.

		Global variables -- None
		:parameter: writer, i,j,text,size, color

		writer: turtle to be used for writing

		i,j: coordinates for the location of writing

		text: the text to be written

		size: size of the text

		color: color of the text

		:returns: None

	"""
	# Converting the i,j values to x,y coordintes as per the cartesian plane
	x = j * 10 + 5
	y = -10 * i + 90 - 5

	# writing the text
	writer.penup()
	writer.goto(x, y)
	writer.color(color)
	writer.write(text, font=('Arial', size, 'bold'))
	# Updating the screen
	scrn.update()


def draw_number(writer, i, j, number, size):
	"""
		Purpose:
		---
		This function is used for writing on the screen using turtle write command.

		Global variables -- None

		:parameter: writer, i,j,text,size, color

		writer: turtle to be used for writing

		i,j: coordinates for the location of writing

		number: Number to be written

		size: size of the text

		:returns: None

	"""
	# converting the i, j coordinates to x and y ones for drawing
	x = j * 10 + 5
	y = -10 * i + 90 - 5

	# using the writer as a turtle object
	writer.penup()
	writer.goto(x, y - 5)
	writer.pencolor("dark blue")
	writer.pendown()
	writer.write(str(number), align='center', font=('Arial', size, 'bold'))
	turtle.pencolor('red')
	# creating the effect
	writer.write(str(number), align='center', font=('Arial', size - 3, 'bold'))
	scrn.update()


def draw_square(length):
	"""
			Purpose:
			---
			This function performs the task of drawing a square of length provided, on the screen.

			Global variables -- None
			:parameter: Length

			:returns: None

		"""


	for i in range(4):
		turtle.pendown()
		turtle.fd(length)
		turtle.right(90)


def draw_and_check(i, j):

	"""
		Purpose:
		---
		This function initiates the drawing of the numbers on the screen and checks for a possible Gameover.

		Global variables -- board, Gameover, Life

		:parameter: i,j

		i,j: coordinates for the location of writing

		:returns: None

	"""


	global board, Gameover, Life, player

	# checking and drawing the number on the screen
	if board[i][j] != 0:
		draw_number(turtle, i, j, board[i][j], 40)

	# saving the return value of gameover function in Gameover variable
	Gameover = gameover(board)

	# condition for player entering name as none
	if player == None:
		player = ''
	# Using the Gameover variable for checking purpose

	if Gameover == True:
		if Life > 0:

			# Taking the user input for playing the game again
			Text = str(player) + ' WON!'
			write(turtle,-0.7, 3,Text,25,'red')
			time.sleep(1)
			Reply = scrn.textinput('Congrats!',' You have Successfully \n completed the Sudoku \n Would you like to play again')

			# checking the input
			if (Reply is not None and Reply.lower() == 'yes'):


				reinitialize_screen()
				return
			else:
				# closing the turtle window

				turtle.bye()


	if Life <= 0:
		Gameover = True
		Text = str(player) + ' LOST!'
		write(turtle, -0.7, 3, Text, 25, 'dark blue')
		time.sleep(1)
		Reply = scrn.textinput('You Lost!', 'Sorry, but you have lost the game\n would you like to play again', )
		if (Reply is not None and Reply.lower() == 'yes'):

			reinitialize_screen()
		else:
			turtle.bye()


def count_down():
	"""
		Purpose:
		---
		This function is being used for Displaying a count_down on the screen before beginning the Game

		Global variables -- None

		:parameter: None


		:returns: None

	"""

	# Displaying the count_down for from 3

	for i in range(3, 0, -1):
		if i == 3:
			write(pen, -0.7, 2.3, 'Welcome To Sudoku!', 30, 'red')
			time.sleep(1)

			pen.clear()
			write(pen, -0.7, 2.3, 'Game Starts in', 30, 'red')
			time.sleep(1)
			pen.clear()

		draw_number(pen, 4, 4, i, 100)
		time.sleep(1)
		if i == 1:
			pen.clear()
			write(pen, 4, 2.4, 'GO!', 90, 'orange')
			time.sleep(1)
		pen.clear()


def play(x, y):
	"""
		Purpose:
		---
		This function is called by the onclick function of the turtle
		module when the user clicks somewhere on the screen.

		Global variables -- board, grid, Life, Gameover, status

		status: the status of help button
		:parameter: x,y

		x,y: coordinates for the location of click

		:returns: None

	"""




	global board, grid_solution, Life, Gameover, status

	# Converting the x,y coordintes to i,j for the ease of computing
	i = -(int(y - 90)) // 10
	j = (int(x)) // 10


	# Checking if the click happened inside the Help Box
	if i == -2 and j == 4:

		if status == 'show':
			# calling the Help function to hide the help message
			Help('Hide')
			status = 'hide'
		else:
			# calling the Help function to show the help message
			status = 'show'
			Help(status)

	# Checking if the click happened outside the Sudoku grid and hence returning the function
	if i >= 9 or j >= 9 or i < 0 or j < 0:

		return

	# checking for Life being greater than 0 so as to continue the game
	if status == 'hide':

		if Life > 0:

			# If the user clicks a box that's already filled and returning
			if board[i][j] != 0:
				# displaying the message of already filled
				write(pen, -0.8, 4, 'That box is Already filled!', 18, 'dark blue')
				time.sleep(0.7)
				pen.clear()
				return
			# else, the user has clicked on an empty box, and user has more than 0 lives,

			# So, Asking the user for a numerical input for the box
			for life in range(Life):
				number = input_number() # Taking input from the user


				if number is not None: # processing the input
					if grid_solution[i][j] == number: # checking if the number entered by the user is correct
						# since grid has the correct values of all boxes
						# Hence changing the board list of that location to the number for displaying it
						board[i][j] = number
						break # breaking the for loop since work is complete

					else: # condition if the user entered an incorrect number

						Life -= 1 # deducting a life
						Life_pen.clear()
						# displaying the New numerical of Life
						Text = 'Life: ' + str(Life)
						write(Life_pen, -0.7, -0.55, Text, 32, 'purple')

						write(pen, -0.7, 4, 'WRONG CHOICE!', 22, 'dark blue')
						time.sleep(0.7)
						pen.clear()
						break


				else: # condition if number variable is None, i.e, the user didn't enter a number
					break
		# calling the draw and check function for Displaying the changes in grid number and Gameover
		draw_and_check(i, j)


def Game_Run(i, j):
	"""
		Purpose:
		---
		This function is used for tracking the on-game time elapsed and displaying it every second.

		Global variables -- start_time, second, minute, hour
		start_time: The time of starting of the current game


		:parameter: i,j

		i,j: coordinates for the location of writing the time

		:returns: None

	"""




	global start_time, second, minute, hour

	# calculating the seconds elapsed
	second = int(time.time() - start_time) - (60 * minute + (3600 * hour))


	# converting the seconds into minutes and hours
	if (second >= 60):
		second = 0
		minute += 1

	if (minute >= 60):
		minute = 0
		hour += 1

	# Displaying the time elapsed on the screen
	pen_time.clear()
	write(pen_time, i, j, 'Time: %d:%d:%d ' % (hour, minute, second), 30, 'blue')
	# Updating the screen

	turtle.update()


def Help(status):
	"""
		Purpose:
		---
		The purpose of this function is to display or hide the help messsage on the scren

		Global variables -- None


		:parameter: status

		status: whether the help is to be shown or is it already there and is to be removed
		:returns: None

	"""



	# Showing the HELP message

	if status == 'show':
		L = 90
		scrn_cover.hideturtle()
		scrn_cover.color('green')
		scrn_cover.setheading(90)
		scrn_cover.penup()
		scrn_cover.goto(0, 0)
		scrn_cover.fillcolor('cyan')
		scrn_cover.begin_fill()
		for i in range(4):
			scrn_cover.fd(L)
			scrn_cover.right(90)
		scrn_cover.end_fill()
		scrn_cover.penup()
		scrn_cover.goto(20, 80)
		scrn_cover.write('Click the Help button again \n to close the help window', font=('Arial', 20, 'bold'))
		Help_pen.penup()
		Help_pen.goto(45, 45)
		Help_pen.stamp()
	else:
		# Removing the help message
		scrn_cover.clear()
		Help_pen.reset()

		Help_pen.hideturtle()
		scrn_cover.hideturtle()


def draw_button(i, j, Name, writer):
	"""
		Purpose:
		---
		The purpose of this function is to display a button of the name provided at a certain location

		Global variables -- None


		:parameter: i, j, Name, writer
		Name: Name of the button to be displayed
		writer: turtle to be used for writing

		i,j: coordinates for the location of writing
		:returns: None

	"""
	# converting the i,j coordinates to x,y ones
	x = j * 10 + 5
	y = -10 * i + 90 - 5


	# displaying the button
	writer.penup()
	writer.goto(x -2.3, y)
	writer.pendown()
	writer.color('green')
	writer.write(Name, font=('Arial', 28, 'bold'))

	writer.penup()
	writer.goto(x - 3.5, y)
	writer.pensize(6)
	writer.pendown()
	for i in range(2):
		writer.fd(6)
		writer.left(90)
		writer.fd(6)
		writer.left(90)

	# Updating the screen
	scrn.update()


def gameover(board):
	"""
		Purpose:
		---
		This function performs the logic for checking if the game is over or not

		Global variables -- Life


		:parameter: board

		board: A list of lists containing the values of numbers on the sudoku grid
		:returns: True or False
		True: if the game has to end
		False: if the game has to continue
	"""

	global Life

	# checking for a posible gameover
	# by iterating if a block in the grid still remains 0 or not
	p = 0
	for i in range(rows):
		for j in range(col):
			if board[i][j] == 0:
				p += 1 # incrementing p by 1 each time we encounter an empty cell
	if p > 0:
		return False
	elif Life == 0:
		# if we have an empty cell but life is 0 then, this signifies that the player has lost the game
		return True
	elif p ==0:
		return True
	else:
		return 	False



def reinitialize_screen():
	"""
	Purpose:
	---
	This function performs the task of reinitializing the screen if the user wishes to play again
	it resets everthing to the initial stage and makes all te required variable values None

	:globals: board, start_time, Gameover, second, minute, hour, Life
	second, minute, hour = Time elapsed

	"""
	##############	ADD YOUR CODE HERE	##############
	global board, start_time, Gameover, second, minute, hour, Life

	# resetting the screen

	turtle.resetscreen()
	pen_time.reset()

	# Hiding all the turtles post reset
	turtle.hideturtle()
	Life_pen.hideturtle()
	Level_pen.hideturtle()
	Help_pen.hideturtle()
	pen_time.hideturtle()
	scrn_cover.hideturtle()
	pen.hideturtle()

	# Immediately updating the screen
	scrn.update()

	# Setting the gloabl Life variable to 3 again
	Life = 3

	# setting the Gameover variable to False
	Gameover = False


	# Reinitialising the sudoku board
	sudoku_board()

	# Asking the user for name again
	input_names_of_player()

	# Reinitializing the Dashboard and board, grid values based on level selected by the user
	init_board()

	# Displaying the Count_down again
	count_down()

	# Reinitialising the starting time of the game for
	# calculating the time elapsed
	start_time = time.time()
	# Setting the time elapsed to 0
	second = minute = hour = 0


########################----- MAIN FUNCTION -----############################
"""
	Purpose:
	---
	This is the main condition of the entire program and is executed only once in each run of the program
	
	it comprises of the initialization of the screen and sudoku board for the first time.
	
	
	
"""


# Initialising the screen (This is donw only once )
Init_screen()


# initialising the sudoku board
sudoku_board()

# Asking the user for name
input_names_of_player()

# initializing the Dashboard and board, grid values based on level selected by the user
init_board()


# Displaying the Count_down
count_down()

# initialising the starting time of the game for
# calculating the time elapsed
start_time = time.time()

# condition for running the time and click function
while gameover(board) is not True:
	scrn.onclick(play)
	Game_Run(-1.7, -0.55)

# Using the turtle.mainloop for letting the screen to stay
turtle.mainloop()


#################################################################
#####   Team-Id = 12    #####
#####                   #####
#####    Kushagra       #####
#####    Chaudhary      #####
#############################
#############################
#####      Mohd.        #####
#####      Ziya         #####
#####      Ahmad        #####
#####      Khan         #####
################################################################
