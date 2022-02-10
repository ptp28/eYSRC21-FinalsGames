import pygame
import time
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init() # initiate pygame and give permission
pygame.mixer.init() # to use pygame's functionality.

# set the pygame window name
pygame.display.set_caption('thank you')
# define the RGB value
# for white colour
white = (255, 255, 255)

# assigning values to X and Y variable
width = 931
height = 502
display_surface = pygame.display.set_mode((width,height))
image1 = pygame.image.load('./Assets/my_.gif')
display_surface.fill(white)
display_surface.blit(image1, (0, 0))
pygame.display.update()

# image.
time.sleep(4)
# create the display surface object
# of specific dimension..enemys(X, Y).
display_surface = pygame.display.set_mode((width,height))



# create a surface object, image is drawn on it.
image = pygame.image.load('./Assets/Thank_You.gif')

pygame.mixer.music.load("./Assets/Thank_you.mp3")

# Setting the volume
pygame.mixer.music.set_volume(0.7)

# Start playing the song
pygame.mixer.music.play()

display_surface.fill(white)

display_surface.blit(image, (0, 0))

pygame.display.update()
time.sleep(4)
quit()
pygame.quit()