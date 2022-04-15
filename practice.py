import random
import pygame
import config
import os

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

def practice1():
    pygame.mixer.stop()
    os.system('clear')
    while True:
        print("--------------------------------------------------------------")
        practice_input = input("""
Welcome to practice. Here you can see your team practice and get a hint on how to beat your next opponent.
Choose an option:
1. Talk to the assistant coach
2. Tell your team to run 10 suicides
3. Shoot a 3!
4. Go back to the previous menu    
        """)
        
        
        if practice_input == '1':
            print(f"""
You go up to the assistant coach and ask him about the game plan

You: Hey coach, how's it going. What's our best game plan against the Miami Heat?

Assistant Coach: Hey coach {config.user_name.title()}! Team is looking good and in shape. 

Assistant Coach: Against Miami, I think Trae Young is our best player to be able to disrupt Miami's defense.

Assistant Coach: We should make sure Trae is in our starting lineup!
""")
        elif practice_input == '2':
            print("""
You tell your team to stop what they are doing and to run 10 suicides immediately!

The whole team looks upset and starts lining up on the baseline to run suicides.

Gorgui Dieng the 3rd string center yells "I'm tired of this. you're not even a real coach! I'm out!"

Gorgui Dieng quits the team thanks to your suicides.
            """)
        elif practice_input == '3':
            print("You pick up a basketball and try shooting a 3.")
            shots = ['Miss!','Miss!','Swish!',"Miss!"]
            shot = random.choice(shots)
            if shot == 'Swish!':
                swish_sound.play()
                print(shot)
            elif shot == 'Miss!':
                miss_sound.play()
                print(shot)
        elif practice_input == '4':
            from main import main_menu1
            main_menu1()

def practice2():
    pygame.mixer.stop()
    os.system('clear')
    while True:
        print("--------------------------------------------------------------")
        practice_input = input("""
Welcome to practice. Here you can see your team practice and get a hint on how to beat your next opponent.
Choose an option:
1. Talk to the assistant coach
2. Bring dinner for the team
3. Shoot a 3!
4. Go back to the previous menu    
        """)
        
        
        if practice_input == '1':
            print(f"""
You go up to the assistant coach and ask him about the game plan

You: Hey coach, good game against the Heat. Now what's our best game plan against the Houston Rockets?

Assistant Coach: Hey coach {config.user_name.title()}! What a game that was. 

Assistant Coach: Against Houston, we really need to score a lot of threes.

Assistant Coach: We should make sure Bogdan or Kevin is in our starting line up!
""")
        elif practice_input == '2':
            print(f"""
You bring dinner to your exhausted team.

The team is elated and starts chanting we love coach {config.user_name.title()}!
            """)
        elif practice_input == '3':
            print("You pick up a basketball and try shooting a 3.")
            shots = ['Miss!','Miss!','Swish!',"Miss!"]
            shot = random.choice(shots)
            if shot == 'Swish!':
                swish_sound.play()
                print(shot)
            elif shot == 'Miss!':
                miss_sound.play()
                print(shot)
        elif practice_input == '4':
            from main import main_menu2
            main_menu2()

def practice3():
    pygame.mixer.pause()
    os.system('clear')
    while True:
        print("--------------------------------------------------------------")
        practice_input = input("""
Welcome to practice. Here you can see your team practice and get a hint on how to beat your next opponent.
Choose an option:
1. Talk to the assistant coach
2. Throw an alley oop to Clint Capela
3. Shoot a 3!
4. Go back to the previous menu    
        """)
        
        
        if practice_input == '1':
            print(f"""
You go up to the assistant coach and ask him about the game plan

You: Hey coach, Go us for making to the Eastern Conference Finals! Now what's our best game plan against the Brooklyn Nets?

Assistant Coach: Hey coach {config.user_name.title()}! Yeah what a time.

Assistant Coach: Against Brooklyn, we need someone who can guard Kevin Durant and contest his shots!

Assistant Coach: We should make sure Deandre Hunter is on the starting lineup!
""")
        elif practice_input == '2':
            print(f"""
A ball bounces to you and Clint is looking at you and pointing to the rim.

Hinting that he wants an alley oop. You throw the alley oop and he dunks it.

Clint says thanks coach {config.user_name.title()}!
            """)
        elif practice_input == '3':
            print("You pick up a basketball and try shooting a 3.")
            shots = ['Miss!','Miss!','Swish!',"Miss!"]
            shot = random.choice(shots)
            if shot == 'Swish!':
                swish_sound.play()
                print(shot)
            elif shot == 'Miss!':
                miss_sound.play()
                print(shot)
        elif practice_input == '4':
            from main import main_menu3
            main_menu3()

def practice4():
    pygame.mixer.stop()
    os.system('clear')
    while True:
        print("--------------------------------------------------------------")
        practice_input = input("""
Welcome to practice. Here you can see your team practice and get a hint on how to beat your next opponent.
Choose an option:
1. Talk to the assistant coach
2. Give the team a pep talk
3. Shoot a 3!
4. Go back to the previous menu    
        """)
        
        
        if practice_input == '1':
            print(f"""
You go up to the assistant coach and ask him about the game plan

You: Hey coach, WE'RE IN THE NBA FINALS! What do we do about the Golden State Warriors?

Assistant Coach: Hey coach {config.user_name.title()}! All our hard work paid off!

Assistant Coach: Honestly, in the finals we just have to trust our team and our players.

Assistant Coach: Statistically, Steph Curry is the best shooter out there! So we just need to be statistically better!
""")
        elif practice_input == '2':
            coach_choice = input(f"""
You told the team to gather up so you can make one last pep talk before the game.

The team gathers up and you make your speech. The team is motivated more than ever!

Even Gorgui Dieng comes back to the team and apologizes to you so he can be on the team again.

Gorgui Dieng: Sorry coach {config.user_name.title()} about storming out last time. I'd love to play for you again.

Do you let him back in the team? (yes/no):
            """).lower()
            if coach_choice == 'yes':
                print("--------------------------------------------------------------")
                print(f"""
You let him back in cause you're a good coach. 🥲

Gorgui Dieng: Thanks Coach! You're the best!""")
            elif coach_choice == 'no':
                print("--------------------------------------------------------------")
                print(f"""
Gorgui Dieng throws a ball at your feet and storms off! 🏀

Gorgui Dieng: You suck! 🤬
                """)
        elif practice_input == '3':
            print("You pick up a basketball and try shooting a 3.")
            shots = ['Miss!','Miss!','Swish!',"Miss!"]
            shot = random.choice(shots)
            if shot == 'Swish!':
                swish_sound.play()
                print(shot)
            elif shot == 'Miss!':
                miss_sound.play()
                print(shot)
        elif practice_input == '4':
            from main import main_menu4
            main_menu4()