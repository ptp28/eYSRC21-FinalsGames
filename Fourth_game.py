# import time
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import  random
import playsound
import time
app = Ursina()
grass_texture = load_texture('Assets/grass_block.png')

brick_texture = load_texture('Assets/brick_block.png')

sky_texture   = load_texture('Assets/skybox.png')
arm_texture   = load_texture('Assets/arm_texture.png')

winning_sound = Audio('Assets/winning.mp3',loop = True, autoplay = False)
time1 = 3000
time2 = 50
punch_sound  = Audio('Assets/punch.wav',loop = False, autoplay = False)
catch  = Audio('Assets/Catch_win.wav',loop = False, autoplay = False)

block_pick = 1
game_over_play = False
window.fps_counter.enabled = True
window.exit_button.visible = True
def update():
	global block_pick,score,text,text2,time1,aim,game_over_play,winner,text1,time2
	if held_keys['q']:
		quit()
	# text.



	if winner== True:
		time2-=1
		if time2 == 0:
			time.sleep(2)
			exit()
	if held_keys['left mouse'] or held_keys['right mouse'] :
		hand.active()
	else:
		hand.passive()
	input_handler.rebind('up arrow','w')
	input_handler.rebind('down arrow', 's')
	input_handler.rebind('left arrow', 'a')
	input_handler.rebind('right arrow', 'd')


	x = player.get_x()
	y = player.get_y()
	z = player.get_z()

	for sphere in sphere_list:
		sphere.rotation=Vec3(0,10,0)

		if sphere.get_distance(player)<2:



			sphere.color='#6E0D25'
			sphere.y = 20
			score += 1
			text.y = 6


			text = Text(text=f"Score: {score}", position=(-0.65, 0.4), origin=(0, 0), scale=2, color=color.yellow,
						background=True)

			catch.play()
			sphere_list.remove(sphere)
		if len(sphere_list) == 0:
			text.y = 1
			# text.

			text = Text(text='You Win the game', position=(-0.55, 0.4), origin=(0, 0), scale=2, color=color.yellow,
						background=True)
			gif = 'winner.gif'

			Throphy = Animation(gif, parent=camera.ui, origin=(0, 0), position=(0.5, 00), scale=0.60)
			Throphy.x = 0
			winner = True
			playsound.playsound('Assets/Won_the_game.mp3',False)

	if y < -250:
		quit()


	second = time1
	second = int(second)
	minute = second / 1000
	minute = int(minute)

	text1.y = 1

	text1 = Text(text=f"Countdown: {second}", position=(-0, 0.4), origin=(0, 0), scale=2, color=color.yellow,
				background=True)
	time1-=1
	# print(second)
	if minute == 0:
		quit()



# if held_keys['j']: block_pick = 7
class Voxel(Button):
	def __init__(self, position = (0,0,0),texture=texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

	def input(self,key):
		global winner
		if self.hovered:

			if key == 'left mouse down':
				punch_sound.play()
				destroy(self)
			elif key == 'right mouse down':
				punch_sound.play()
				destroy(self)


class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)



for z in range(27):
	for x in range(25):
		voxel = Voxel(position = (x,0,z),texture=grass_texture)
for z in range(25):
	for x in range(19):
		for y in range(6):
			voxel = Voxel(position = (x,y,z),texture=brick_texture)


score = 0
winner = False
player = FirstPersonController()
text = Text(text=f"Score: {score}", position=(-0.65, 0.4), origin=(0, 0), scale=2, color=color.yellow, background=True)
player.x = 22
player.z = 22
sphere_list = []
colors = ['#1428f5','#ec5613','#f200f4','#edff8d']
player.y=0
numbers_of_sphere = random.randint(4,8)
aim = Text(text=f"Aim: {numbers_of_sphere}", position=(0.75, 0.4), origin=(0, 0), scale=2, color=color.yellow, background=True)
text1 = Text(text="Countdown:0", position=(-0, 0.4), origin=(0, 0), scale=2, color=color.yellow,
				background=True)
q = Text(text='q for exit', position=(-0, 2.4), origin=(0, 0), scale=2, color=color.yellow,
				background=True)
for i in range(numbers_of_sphere):
	sphere = Entity(model='sphere',scale = 1,texture= 'gold.jpg')
	sphere.x = random.randint(0,14)
	sphere.z = random.randint(0,14)
	sphere.y = random.randint(3,5)
	sphere_list.append(sphere)

playsound.playsound('Assets/Game_start.mp3')

sky = Sky()
hand = Hand()
app.run()