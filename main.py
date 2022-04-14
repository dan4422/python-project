import random
import config
from games import game_miami, game_houston
from practice import practice1, practice2
import os

def start():
    config.user_name = input('What is your name?: ')
    print(f"""
Hello {config.user_name.title()}. You are now the new coach of the Atlanta Hawks! Congrats!

The Atlanta Hawks are a fringe playoff team fighting to get into the 8th seed. There is 2 more regular season games before playoffs!
If you win one more game you will be in the playoffs and continue. If you lose both games, you will not be in the playoffs and the season will be over.

Your first rule of business is to choose your starting 5 lineup!
Here's a list of player's names on the Hawks and it is your job to choose the best 5 players to start the game.
    """)

def choose_starting_five():
    config.starting_five = []
    print(", ".join(config.hawks_players))
    print(" ")
    while True:
        user_choice = input('Choose your starting 5!(Make sure to input their full name): ').title()
        if user_choice not in config.hawks_players:
            print('That player is not on our team!')
        elif user_choice in config.hawks_players:
            config.starting_five.append(user_choice)
        
        if len(config.starting_five) == 5:
            print(" ")
            print('Great job picking your starting 5 coach! Here is a list of your starting five:')
            print(", ".join(config.starting_five).title())
            break

def main_menu1():
    while True:
        user_input = input(f"""
Now that you have chosen your starting 5. It is time to play the remaining 2 games of the season!
Choose to practice or play the game against your next opponent, the Miami Heat!
Enter the number for the option you want to go with, coach {config.user_name.title()}.
1. Practice
2. Play game against the Miami Heat
3. Quit
        """)

        if user_input == '1':
            practice1()
        elif user_input == '2':
            game_miami()
        elif user_input == '3':
            print(f"You're a quitter coach {config.user_name.title()}!")

def hawks_lose():
    print("""
You just lost the game against the Miami Heat!
It's alright you got one more chance to make the playoffs.
Your next opponent is the Houston Rockets.
Make sure to win this one or the season will be over.
    """)

def hawks_win():
    print("""Congrats! You made it to the playoffs. Now the next game should be less pressure, but be sure to win!
    """)

def main_menu2():
    while True:
        user_input = input(f"""
It is time to play the last game of the season!
Choose to practice or play the game against your next opponent, the Houston Rockets!
Or you can change your starting lineup!
Enter the number for the option you want to go with, coach {config.user_name.title()}.
1. Practice
2. Play game against the Houston Rockets
3. Change your starting lineup
4. Quit
        """)

        if user_input == '1':
            practice2()
        elif user_input == '2':
            from games import game_houston
            game_houston()
        elif user_input == '3':
            from main import choose_starting_five
            choose_starting_five()
        elif user_input == '4':
            print(f"You're a quitter coach {config.user_name.title()}!")