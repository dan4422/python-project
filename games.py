import config
import os

def game_miami():
    from main import hawks_lose, hawks_win, main_menu1, main_menu2
    while True:
        game_input = input("""
Your team the Atlanta Hawks are playing against the Miami Heat!
So far it is neck to neck. You call a timeout in the 4th quarter with 35 seconds left!
The game is tied 101 - 101.
You need to draw up a play so that your team will be up.
Which play do you choose?: 
1. Inbound pass to Clint Capela to shoot a midrange
2. Pass to Trae Young to shoot a 3 at the top of the key
3. Give up
        """)

        if game_input == '1':
            if "Clint Capela" in config.starting_five:
                print('The ball is passed to Clint Capela and he missed his mid range and you lost the game!')
                hawks_lose()
                main_menu2()
            elif "Clint Capela" not in config.starting_five:
                print("Clint Capela is not in the starting lineup choose a different option!")
        elif game_input == '2':
            if "Trae Young" in config.starting_five:
                print('Trae Young takes a deep 3 as the last shot and sinks it! You win the game!')
                hawks_win()
                main_menu2()
            else:
                print("Trae Young is not in the starting lineup. You automatically lose for not putting in your best player.")
                hawks_lose()
                main_menu2()
        elif game_input == '3':
            print(f"You're a quitter coach {config.user_name.title()}!")
        else:
            print("Try again!")

def game_houston():
    while True:
        game_input = input("""
Your team the Atlanta Hawks are playing against the Houston Rockets!
Unfortunately, the team is losing by 9 points.
You call a timeout.
You need to draw up a play so that your team will win the game.
Which gameplan do you go with?: 
1. Play defense and take more layups.
2. Play defense and shoot 3's!
3. Give up.
        """)

        if game_input == '1':
            print("You lose the game because you did not have enough scoring. Now the team is sad.")
        elif game_input == '2':
            if "Bogdan Bogdanovic" in config.starting_five or "Kevin Huerter" in config.starting_five:
                print('You stopped the Rockets from winning by scoring more threes with Bogdan and/or Kevin')
            else:
                print("You told your team to shoot more 3's but you didn't have your best wing shooters in the starting lineup. So you lost the game!")
        elif game_input == '3':
            print(f"You're a quitter coach {config.user_name.title()}!")
        else:
            print("Try again!")