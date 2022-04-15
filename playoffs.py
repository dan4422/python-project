import config
import games
import pygame


def playoff():
    from main import main_menu3
    pygame.mixer.stop()
    if config.record >= 1:
        print(" ")
        print("You're going to the playoffs!")
        print(" ")
        user_choice = input('Press Enter to continue...')
        if user_choice == '':
            main_menu3()
    elif config.record == 0: 
        print("You lost both games and didn't make it to the playoffs! Better luck next year.")
        exit()

def finals():
    from main import main_menu4
    print(" ")
    print('You made it to the finals!')
    print(" ")
    user_choice = input('Press Enter to continue...')
    if user_choice == '':
        main_menu4()