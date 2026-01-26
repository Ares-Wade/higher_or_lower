import art
from game_data import data
import random

def user_choice():
    choice = input("Does \'a\' or \'b\' have more instagram followers? ").lower()

    if choice != "a" and choice != "b":
        return user_choice()
    return choice

def which_is_greater(a_followers, b_followers):
    if a_followers > b_followers:
        return "a"
    return "b"

def print_choice(choice):
    print(f"{choice["description"]} {choice["name"]} from {choice["country"]}")


def game():
    score = 0
    #print logo
    print(art.logo)

    # get first time choice A
    choice_a = random.choice(data)

    # print A info
    print_choice(choice_a)

    print(art.vs)

    # get choice B
    #print choice B info
    choice_b = random.choice(data)
    print_choice(choice_b)

    #get user input for which has more followers

    #compare A & B followers

    while len(data) > 0 and user_choice() == which_is_greater(choice_a["follower_count"], choice_b["follower_count"]):
        score += 1

        print("\n" * 20)
        print(art.logo)
        print(f"You're correct! You have a score of {score}")

        #set previous second choice to be the first choice
        choice_a = choice_b
        print_choice(choice_a)

        print(art.vs)

        #randomize choice b
        choice_b = random.choice(data)
        print_choice(choice_b)

    print(art.logo)
    print(f"End of game, you got a score of {score}!")






game()