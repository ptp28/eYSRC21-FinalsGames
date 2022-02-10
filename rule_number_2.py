import pygame
import time

pygame.init()
pygame.mixer.init()


# define the RGB value

white = (255, 255, 255)

# assigning values to X and Y variable
width = 1280
height = 720

# create the display surface object
# of specific dimension..enemys(X, Y).
display_surface = pygame.display.set_mode((width,height))
# set the pygame window name
pygame.display.set_caption('Space invader1')

# create a surface object, image is drawn on it.
image = pygame.image.load('Assets/rules2.jpg')

# Loading the song
pygame.mixer.music.load("Assets/Recording (4).mp3")

# Setting the volume
pygame.mixer.music.set_volume(0.7)

# Start playing the song
pygame.mixer.music.play()

# infinite loop



display_surface.fill(white)
display_surface.blit(image, (0, 0))


pygame.display.update()
time.sleep(45)
quit()
pygame.quit()