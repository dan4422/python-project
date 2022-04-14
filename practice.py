import random
import config

def practice1():
    while True:
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
            shots = ['Miss','Miss','Swish',"Miss"]
            print(random.choice(shots))
        elif practice_input == '4':
            from main import main_menu1
            main_menu1()

def practice2():
    while True:
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
            shots = ['Miss','Miss','Swish',"Miss"]
            print(random.choice(shots))
        elif practice_input == '4':
            from main import main_menu2
            main_menu2()