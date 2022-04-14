import config
import games

def playoff():
    if config.record >= 1:
        print("You're going to the playoffs!")
        games.game_brooklyn()
    elif config.record == 0: 
        print("You lost both games and didn't make it to the playoffs! Better luck next year.")
        exit()
    else:
        print("something wrong with code")