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
X = 600
Y = 700

# create the display surface object
# of specific dimension..enemys(X, Y).
display_surface = pygame.display.set_mode((X, Y))
image1 = pygame.image.load('Start_screen.gif')
display_surface.fill(white)
display_surface.blit(image1, (0, 0))
pygame.display.update()

# image.
time.sleep(4)
# set the pygame window name
display_surface = pygame.display.set_mode((X+100, Y))

pygame.display.set_caption('instruction')

# create a surface object, image is drawn on it.
image = pygame.image.load('instruction_for_opencv.gif')


display_surface.fill(white)


display_surface.blit(image, (0, 0))

pygame.display.update()
time.sleep(15)
quit()
pygame.quit()