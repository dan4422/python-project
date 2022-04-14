import random

def shoot_game(player_list):
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
                        p1_shot = random.choices(ball, weights = [.355,.645], k = 1)
                        string_p1_shot = " ".join(p1_shot)
                        p1_shots.append(string_p1_shot)
                        print(p1_shots)
                        break
            elif player == player_list[1]:
                p2_shot = random.choices(ball, weights = [.428,.572], k = 1)
                string_p2_shot = " ".join(p2_shot)
                p2_shots.append(string_p2_shot)
                print(p2_shots)
        if p1_shots.count('Swish!') == 3:
            print(f"{player_list[0]} shot three 3's faster than Steph!")
            break
        elif p2_shots.count('Swish!') == 3:
            print(f"{player_list[1]} Wins!")
            break
