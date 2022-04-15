import config
import random
import os
from playoffs import playoff, finals
import pygame
import time

pygame.init()
swish_sound = pygame.mixer.Sound('swish.mp3')
miss_sound = pygame.mixer.Sound('miss.mp3')
bang_sound = pygame.mixer.Sound('bang.mp3')
three_sound = pygame.mixer.Sound('three.mp3')
playoff_sound = pygame.mixer.Sound('playoffs.mp3')
nba_sound = pygame.mixer.Sound('nba.mp3')
hawks_sound = pygame.mixer.Sound('hawks.mp3')
victory_sound = pygame.mixer.Sound('victory.mp3')
defense_sound = pygame.mixer.Sound('defense.mp3')
lose_sound = pygame.mixer.Sound('lose.mp3')
nba_sound.set_volume(.2)
playoff_sound.set_volume(.2)
hawks_sound.set_volume(.2)
defense_sound.set_volume(.2)
bang_sound.set_volume(.3)

def shoot_game(player_list,p1_average,p2_average):
    p1_shots = []
    p2_shots = []
    while True:
        for player in player_list:
            print(f"It's {player} turn to shoot!")
            ball = ['Swish!','Miss!']
            if player == player_list[0]:
                while True:
                    shoot = input('Press Enter to shoot!')
                    if shoot == '':
                        p1_shot = random.choices(ball, weights = [p1_average,(1-p1_average)], k = 1)
                        string_p1_shot = " ".join(p1_shot)
                        if string_p1_shot == 'Swish!':
                            swish_sound.play()
                        elif string_p1_shot == 'Miss!':
                            miss_sound.play()
                        p1_shots.append(string_p1_shot)
                        print(p1_shots)
                        break
            elif player == player_list[1]:
                p2_shot = random.choices(ball, weights = [p2_average,(1-p2_average)], k = 1)
                string_p2_shot = " ".join(p2_shot)
                if string_p1_shot == 'Swish!':
                    swish_sound.play()
                elif string_p1_shot == 'Miss!':
                    miss_sound.play()
                p2_shots.append(string_p2_shot)
                print(p2_shots)
        if p1_shots.count('Swish!') == 3:
            print("--------------------------------------------------------------")
            print(f"{player_list[0]} shot three 3's faster than {player_list[1]}!")
            return 1
        elif p2_shots.count('Swish!') == 3:
            print("--------------------------------------------------------------")
            print(f"{player_list[1]} shot three 3's faster than {player_list[0]}!")
            return 2

def game_miami():
    os.system('clear')
    from main import hawks_lose, hawks_win, main_menu2
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
                pygame.mixer.stop()
                lose_sound.play()
                print("--------------------------------------------------------------")
                print('The ball is passed to Clint Capela and he missed his mid range and you lost the game!')
                config.record = hawks_lose()
                user_choice = input('Press Enter to continue...')
                if user_choice == '':
                    main_menu2()
            elif "Clint Capela" not in config.starting_five:
                print("--------------------------------------------------------------")
                print("Clint Capela is not in the starting lineup choose a different option!")
        elif game_input == '2':
            if "Trae Young" in config.starting_five:
                pygame.mixer.stop()
                victory_sound.play()
                print("--------------------------------------------------------------")
                print('Trae Young takes a deep 3 as the last shot and sinks it! You win the game!')
                config.record = hawks_win()
                user_choice = input('Press Enter to continue...')
                if user_choice == '':
                    main_menu2()
            else:
                lose_sound.play()
                print("Trae Young is not in the starting lineup. You automatically lose for not putting in your best player.")
                config.record = hawks_lose()
                user_choice = input('Press Enter to continue...')
                if user_choice == '':
                    main_menu2()
        elif game_input == '3':
            print(f"You're a quitter coach {config.user_name.title()}!")
            break
        else:
            print("Try again!")

def game_houston():
    os.system('clear')
    from main import hawks_lose, hawks_win
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
            lose_sound.play()
            print("--------------------------------------------------------------")
            print("You lose the game because you did not have enough scoring. Now the team is sad.")
            config.record = hawks_lose()
            user_choice = input('Press Enter to continue...')
            if user_choice == '':
                playoff()
        elif game_input == '2':
            if "Bogdan Bogdanovic" in config.starting_five or "Kevin Huerter" in config.starting_five:
                pygame.mixer.stop()
                three_sound.play()
                print("--------------------------------------------------------------")
                print('You stopped the Rockets from winning by scoring more threes with Bogdan and/or Kevin and won the game!')
                config.record = hawks_win()
                user_choice = input('Press Enter to continue...')
                if user_choice == '':
                    playoff()
            else:
                lose_sound.play()
                print("You told your team to shoot more 3's but you didn't have your best wing shooters in the starting lineup. So you lost the game!")
                config.record = hawks_lose()
                user_choice = input('Press Enter to continue...')
                if user_choice == '':
                    playoff()
        elif game_input == '3':
            print(f"You're a quitter coach {config.user_name.title()}!")
            exit()
        else:
            print("Try again!")

def game_brooklyn():
    os.system('clear')
    from main import hawks_lose, hawks_win
    while True:
        game_input = input("""
Your team the Atlanta Hawks is playing the Brooklyn Nets in the ECF Finals!
We need you to choose a defensive game plan to stop Kevin Durant.
Who do you put on Kevin Durant to contest his game?: 
1. Put Deandre Hunter on KD!
2. Put Trae Young on KD!
3. Give up.
        """)

        if game_input == '1':
            if "Deandre Hunter" in config.starting_five:
                pygame.mixer.stop()
                defense_sound.play()
                print(" ")
                print("You won the game! Even though Kevin Durant still went off for 40 points. Deandre Hunter was able to stop him on his last possession!")
                hawks_win()
                time.sleep(2)
                user_choice = input('Press Enter to continue...')
                if user_choice == '':
                    finals()
            else:
                pygame.mixer.stop()
                lose_sound.play()
                print("You didn't put Deandre Hunter in the starting lineup to guard Kevin Durant!")
                print("You've let your team down and lost in the Eastern Conference Finals.")
                print('Season is over. Have fun in Cancun!')
                exit()
        elif game_input == '2':
                pygame.mixer.stop()
                lose_sound.play()
                print('You put Trae Young the smallest player in the NBA on one the best scorers in the league and you lost in the ECF!')
                print('Season is over. Have fun in Cancun!')
                exit()
        elif game_input == '3':
            print(f"You're a quitter coach {config.user_name.title()}!")
            exit()
        else:
            print("Try again!")


def game_goldenstate():
    os.system('clear')
    while True:
        hawks_sound.play()
        game_input = input("""
Your team the Atlanta Hawks is playing in the NBA Finals against the Warriors!
Steph Curry is going off in the 3 point land against the Hawks
While Trae Young and Bogdan Bogdanovic is shooting lights out against the Warriors
For this game, we need to choose either Trae Young or Bogdan Bogdanovic to play a game and win the finals!
Who do you choose to shoot your team's last chances?
1. Trae Young
2. Bogdan Bogdanovic
3. Give up.
        """)

        if game_input == '1':
            print("--------------------------------------------------------------")
            print("Great Choice! You chose me Trae Young to shoot your final shots. In order to win you must make 3 shots before Steph")
            player_list = ["Trae Young", "Steph Curry"]
            points = shoot_game(player_list,p1_average=.355,p2_average=.428)
            if points == 1:
                pygame.mixer.stop()
                bang_sound.play()
                print("Congratulations! You won the NBA Finals! You beat the game!")
                time.sleep(8)
                exit()
            elif points == 2:
                pygame.mixer.stop()
                lose_sound.play()
                print("Awww you lost. Seasons over. Try starting all over again!")
        elif game_input == '2':
            print("--------------------------------------------------------------")
            print("Great Choice! You chose me Bogdan Bogdanovic to shoot your final shots. In order to win you must make 3 shots before Steph")
            player_list2 = ["Bogdan Bogdanovic", "Steph Curry"]
            points = shoot_game(player_list2,p1_average=.384,p2_average=.428)
            if points == 1:
                pygame.mixer.stop()
                bang_sound.play()
                print("Congratulations! You won the NBA Finals! You beat the game!")
                time.sleep(8)
                exit()
            elif points == 2:
                print("Awww you lost. Seasons over. Try starting all over again!")
                pygame.mixer.stop()
                lose_sound.play()
        elif game_input == '3':
            print(f"You're a quitter coach {config.user_name.title()}!")
            exit()
        else:
            print("Try again!")