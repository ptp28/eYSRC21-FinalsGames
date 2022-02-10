import pygame
import time
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
pygame.mixer.init()


# define the RGB value
# for white colour
white = (255, 255, 255)

# assigning values to X and Y variable
width = 1280
height = 720

# create the display surface object
# of specific dimension..enemys(X, Y).
display_surface = pygame.display.set_mode((width,height))

# set the pygame window name
pygame.display.set_caption('Space invader 2')

# create a surface object, image is drawn on it.
image = pygame.image.load('./Assets/rules3.jpg')

# Loading the song
pygame.mixer.music.load("./Assets/Recording (6).mp3")

# Setting the volume
pygame.mixer.music.set_volume(0.7)

# Start playing the song
pygame.mixer.music.play()


display_surface.fill(white)
display_surface.blit(image, (0, 0))


pygame.display.update()
time.sleep(50)
quit()
pygame.quit()