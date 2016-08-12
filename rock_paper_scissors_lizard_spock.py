# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""
https://en.wikipedia.org/wiki/Rock-paper-scissors#Additional_weapons
http://www.samkass.com/theories/RPSSL.html
http://www.cafepress.com/samkass
"""
import random

number_to_name = {0: 'Rock', 1: 'Spock', 2: 'Paper', 3: 'Lizard', 4: 'Scissor'}
name_to_number = dict(zip(number_to_name.values(), number_to_name.keys()))


def rspls1(player_name):
    player_number = name_to_number[player_name]
    computer_number = random.randint(0, 4)
    computer_name = number_to_name[computer_number]
    print("You choose {pn} and computer choose {cn}".format(pn=player_name, cn=computer_name))
    if 1 <= (player_number - computer_number) % 5 <= 2:
        print("You Win")
    elif player_number == computer_number:
        print("Tie !")
    else:
        print("You Lose")

rspls1("Rock")
rspls1("Paper")


winner_table = {
    'Rock': ['Scissor', 'Lizard'],
    'Spock': ['Scissor', 'Rock'],
    'Paper': ['Spock', 'Rock'],
    'Lizard': ['Paper', 'Spock'],
    'Scissor': ['Paper', 'Lizard']
}


def rspls2(player_name):
    computer_name = number_to_name[random.randint(0, 4)]
    print("You choose {pn} and computer choose {cn}".format(pn=player_name, cn=computer_name))
    if computer_name in winner_table[player_name]:
        print("You Win")
    elif computer_name == player_name:
        print("Tie !")
    else:
        print("Lose")

rspls2("Rock")
rspls2("Paper")
