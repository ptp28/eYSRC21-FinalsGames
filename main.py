# Team id:74
# Name : V.L.Dwaarakesh,Lalit
import pygame
import pygame_menu
import os
import webbrowser

os.system('python opencv_instruction.py')
os.system('python Start_opencv.py')
pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Eysrc-Yantra School Robotics Competition (eYSRC 2021) ')

def game_first():
    def play():
        os.system('python first_game.py')
    def back():
        menu.mainloop(surface)
        return
    def back1():
        menu1.mainloop(surface)
        return
    def written_Instruction():
        os.system('python rule_number_1.py')
    def demo():
        url = "https://youtu.be/swTOrxOT8aI"
        webbrowser.open(url, new=1)

    def Instruction():
        menu2 = pygame_menu.Menu('Game Inventor', 800, 600,
                                 theme=pygame_menu.themes.THEME_ORANGE)
        menu2.add.button('Written Instruction', written_Instruction)
        menu2.add.button('Video Instruction', demo)
        menu2.add.button('back', back1)

        image_widget = menu1.add.image(image_path='Assets/Logo_of_first_game.gif')
        # image_widget.set_border(1, 'black')
        image_widget.set_float(origin_position=True)
        image_widget.scale(1.3, 1.3)
        image_widget.translate(-5, 15)
        image_widget = menu2.add.image(image_path='Assets/eyan_logo.gif')
        # image_widget.set_border(1, 'black')
        image_widget.set_float(origin_position=True)
        image_widget.scale(0.80, 0.80)
        image_widget.translate(490, 0)
        image_widget = menu2.add.image(image_path='Assets/robo.gif')
        # image_widget.set_border(1, 'black')
        image_widget.set_float(origin_position=True)
        image_widget.scale(1, 1)
        image_widget.translate(10, 300)
        menu2.mainloop(surface)


    menu1 = pygame_menu.Menu('Game Inventor', 800, 600,
                            theme=pygame_menu.themes.THEME_ORANGE)
    menu1.add.button('Play',play)
    menu1.add.button('Instruction', Instruction)
    menu1.add.button('back',back)

    image_widget = menu1.add.image(image_path='Assets/Logo_of_first_game.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(1.3,1.3)
    image_widget.translate(-5, 15)
    image_widget = menu1.add.image(image_path='Assets/eyan_logo.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(0.80, 0.80)
    image_widget.translate(480, 0)
    image_widget = menu1.add.image(image_path='Assets/robo.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(1, 1)
    image_widget.translate(10, 300)
    menu1.mainloop(surface)
def game_second():
    def play():
        os.system('python second_game.py')
    def back():
        menu.mainloop(surface)
        return
    def back1():
        menu1.mainloop(surface)
        return
    def written_Instruction():
        os.system('python rule_number_2.py')
    def demo():
        url = "https://youtu.be/iC9mBx07wg0"
        webbrowser.open(url, new=1)
    def Instruction():
        menu2 = pygame_menu.Menu('Game Inventor', 800, 600,
                                 theme=pygame_menu.themes.THEME_ORANGE)
        menu2.add.button('Written Instruction', written_Instruction)
        menu2.add.button('Video Instruction', demo)
        menu2.add.button('back', back1)
        image_widget = menu2.add.image(image_path='Assets/space_invader.gif')

        image_widget.set_float(origin_position=True)
        image_widget.scale(0.80, 0.80)
        image_widget.translate(-30, 255)
        image_widget = menu2.add.image(image_path='Assets/eyan_logo.gif')

        image_widget.set_float(origin_position=True)
        image_widget.scale(0.80, 0.80)
        image_widget.translate(490, 0)
        image_widget = menu2.add.image(image_path='Assets/robo.gif')

        image_widget.set_float(origin_position=True)
        image_widget.scale(1, 1)
        image_widget.translate(10, 0)
        menu2.mainloop(surface)

    menu1 = pygame_menu.Menu('Game Inventor', 800, 600,
                            theme=pygame_menu.themes.THEME_ORANGE)
    menu1.add.button('Play',play)
    menu1.add.button('Instruction', Instruction)
    menu1.add.button('back',back)
    image_widget = menu1.add.image(image_path='Assets/space_invader.gif')
    # image_widget.set_border(1, 'black')
    image_widget.set_float(origin_position=True)
    image_widget.scale(0.80, 0.80)
    image_widget.translate(-30, 255)
    image_widget = menu1.add.image(image_path='Assets/eyan_logo.gif')
    # image_widget.set_border(1, 'black')
    image_widget.set_float(origin_position=True)
    image_widget.scale(0.80, 0.80)
    image_widget.translate(480, 0)
    image_widget = menu1.add.image(image_path='Assets/robo.gif')
    # image_widget.set_border(1, 'black')
    image_widget.set_float(origin_position=True)
    image_widget.scale(1, 1)
    image_widget.translate(10, 0)
    menu1.mainloop(surface)
def game_third():
    def play():
        os.system('python third_game.py')
    def back():
        menu.mainloop(surface)
        return
    def back1():
        menu1.mainloop(surface)
        return
    def written_Instruction():
        os.system('python rule_number_3.py')
    def demo():
        url = "https://youtu.be/zZ4NN3pxZU0"
        webbrowser.open(url, new=1)

    def Instruction():
        menu2 = pygame_menu.Menu('Game Inventor', 800, 600,
                                 theme=pygame_menu.themes.THEME_ORANGE)
        menu2.add.button('Written Instruction', written_Instruction)
        menu2.add.button('Video Instruction', demo)
        menu2.add.button('back', back1)
        image_widget = menu2.add.image(image_path='Assets/space_invader 2.gif')

        image_widget.set_float(origin_position=True)
        image_widget.scale(0.80, 0.80)
        image_widget.translate(-30, 255)

        image_widget = menu2.add.image(image_path='Assets/eyan_logo.gif')

        image_widget.set_float(origin_position=True)
        image_widget.scale(0.80, 0.80)
        image_widget.translate(490, 0)
        image_widget = menu2.add.image(image_path='Assets/robo.gif')

        image_widget.set_float(origin_position=True)
        image_widget.scale(1, 1)
        image_widget.translate(10, 0)
        menu2.mainloop(surface)

    menu1 = pygame_menu.Menu('Game Inventor', 800, 600,
                            theme=pygame_menu.themes.THEME_ORANGE)
    menu1.add.button('Play',play)
    menu1.add.button('Instruction', Instruction)
    menu1.add.button('back',back)
    image_widget = menu1.add.image(image_path='Assets/space_invader 2.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(0.80, 0.80)
    image_widget.translate(-30, 255)
    image_widget = menu1.add.image(image_path='Assets/eyan_logo.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(0.80, 0.80)
    image_widget.translate(480, 0)
    image_widget = menu1.add.image(image_path='Assets/robo.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(1, 1)
    image_widget.translate(10, 0)

    menu1.mainloop(surface)
def game_fourth():
    def play():
        os.system('python fourth_game.py')
    def back():
        menu.mainloop(surface)
        return
    def back1():
        menu1.mainloop(surface)
        return
    def written_Instruction():
        os.system('python rule_number_4.py')

    def demo():
        url = "https://youtu.be/lWYIQrTnA4M"
        webbrowser.open(url, new=1)
    def Instruction():
        menu2 = pygame_menu.Menu('Game Inventor', 800, 600,
                                 theme=pygame_menu.themes.THEME_ORANGE)
        menu2.add.button('Written Instruction', written_Instruction)
        menu2.add.button('Video Instruction', demo)
        menu2.add.button('back', back1)
        image_widget = menu2.add.image(image_path='Assets/ball_finder.gif')
        # image_widget.set_border(1, 'black')
        image_widget.set_float(origin_position=True)
        image_widget.scale(0.80, 0.80)
        image_widget.translate(-30, 255)
        image_widget = menu2.add.image(image_path='Assets/eyan_logo.gif')

        image_widget.set_float(origin_position=True)
        image_widget.scale(0.80, 0.80)
        image_widget.translate(480, 0)
        image_widget = menu2.add.image(image_path='Assets/robo.gif')

        image_widget.set_float(origin_position=True)
        image_widget.scale(1, 1)
        image_widget.translate(10, 0)
        menu2.mainloop(surface)

    menu1 = pygame_menu.Menu('Game Inventor', 800, 600,
                            theme=pygame_menu.themes.THEME_ORANGE)
    menu1.add.button('Play',play)
    menu1.add.button('Instruction', Instruction)
    menu1.add.button('back',back)
    image_widget = menu1.add.image(image_path='Assets/ball_finder.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(0.80, 0.80)
    image_widget.translate(-30, 255)
    image_widget = menu1.add.image(image_path='Assets/eyan_logo.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(0.80, 0.80)
    image_widget.translate(480, 0)
    image_widget = menu1.add.image(image_path='Assets/robo.gif')

    image_widget.set_float(origin_position=True)
    image_widget.scale(1, 1)
    image_widget.translate(10, 0)

    menu1.mainloop(surface)
menu = pygame_menu.menu.Menu('Game Inventor', 800, 600,
                       theme=pygame_menu.themes.THEME_ORANGE)
def exit():
    os.system('python Thank_you.py')
    quit()

menu.add.button('Planet Explorer', game_first)
menu.add.button('Space Invader1', game_second)
menu.add.button('Space Invader2', game_third)
menu.add.button('3d ball finder', game_fourth)
menu.add.button('Quit', exit)
image_widget = menu.add.image(image_path='Assets/eyan_logo.gif')

image_widget.set_float(origin_position=True)
image_widget.scale(0.80, 0.80)
image_widget.translate(480, 0)
image_widget = menu.add.image(image_path='Assets/robo.gif')

image_widget.set_float(origin_position=True)
image_widget.scale(1, 1)
image_widget.translate(10, 0)
menu.mainloop(surface)
