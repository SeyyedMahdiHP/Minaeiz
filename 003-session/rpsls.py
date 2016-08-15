import random
name_to_number = {'pa': 0, 'ro': 1, 'li': 2, 'sc': 3, 'sp': 4}
number_to_name = dict(zip(name_to_number.values(), name_to_number.keys()))

winner_table = {
    0: [1, 4],
    1: [2, 3],
    2: [0, 4],
    3: [0, 2],
    4: [1, 3]
}


def rpsls(player):
    player_number = name_to_number[player]
    computer_number = random.randint(0, 4)
    print("You choose : {0}".format(player))
    print("Computer choose : {0}".format(number_to_name[computer_number]))
    if computer_number == player_number:
        return "Tie"
    elif computer_number in winner_table[player_number]:
        return "You Win"
    elif computer_number not in winner_table[player_number]:
        return "You Lose"


print(rpsls("ro"))