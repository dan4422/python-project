import config
import games


def playoff():
    from main import main_menu3
    if config.record >= 1:
        print("You're going to the playoffs!")
        main_menu3()
    elif config.record == 0: 
        print("You lost both games and didn't make it to the playoffs! Better luck next year.")
        exit()
    else:
        print("something wrong with code")

def finals():
    from main import main_menu4
    print('You made it to the finals!')
    main_menu4()