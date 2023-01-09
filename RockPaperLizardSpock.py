import random
from random import randint


def name_to_number(name):
    if name == "rock":
        number = 0
        return number
    elif name == "Spock":
        number = 1
        return number
    elif name == "paper":
        number = 2
        return number
    elif name == "lizard":
        number = 3
        return number
    elif name == "scissors":
        number = 4
        return number


def number_to_name(number):
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "Spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name


def rpsls(player_choice):
    player_choise_number = name_to_number(player_choice)
    computer_choise_number = random.randint(0, 4)
    computer_choise = number_to_name(computer_choise_number)
    
    if (player_choise_number - computer_choise_number) % 5 == 0:
        print "Player chooses", player_choice, '\nComputer chooses', computer_choise, "\nPlayer and computer tie!\n"
        
    elif (player_choise_number - computer_choise_number) % 5 == 1:
        print "Player chooses", player_choice, '\nComputer chooses', computer_choise, "\nPlayer Win!!\n"

    elif (player_choise_number - computer_choise_number) % 5 == 2:
        print "Player chooses", player_choice, '\nComputer chooses', computer_choise, "\nPlayer Win!!\n"
        
    elif (player_choise_number - computer_choise_number) % 5 == 3:
        print "Player chooses", player_choice, '\nComputer chooses', computer_choise, "\nComputer Win!\n"
        
    elif (player_choise_number - computer_choise_number) % 5 == 4:
        print "Player chooses", player_choice, '\nComputer chooses', computer_choise, "\nComputer Win!\n"



rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




