import time
import random


def print_pause(message: str):
    """
    This method do the printing + the small pause
    """
    print(message)
    time.sleep(2)


def play_again():
    """
    Asks the player if he wants to play again or no
    """ 
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print("Excellent! Restarting the game ...")
        play()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def cave(items: list, enemy: str):
    """
    When the player enters the cave
    """ 
    if "wand" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause(
            "You've been here before, and gotten all"
            " the good stuff. It's just an empty cave now."
        )
        print_pause("You walk back to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause(
            "Your eye catches a glint of metal behind a rock."
        )
        print_pause("You have found the Magical Wand of Ogoroth!")
        print_pause(
            "You discard your rusty old magic wand and take the Wand of Ogoroth with you."
        )
        print_pause("You walk back out to the field.")
        items.append("wand")
    field(items, enemy)


def house(items: list, enemy: str):
    """
    When the player enters the house
    """ 
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door "
        "opens and out steps a " + enemy + "."
    )
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    if "wand" not in items:
        print_pause(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny, rusty old magic wand.")
    while True:
        choice_two = input(
            "Would you like to (1) cast a spell or (2) run away?"
        )
        if choice_two == "1":
            if "wand" in items:
                print_pause(
                    "As the " + enemy + " moves to attack, "
                    "you unsheath your new sword."
                )
                print_pause(
                    "The Magical Wand of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the attack."
                )
                print_pause(
                    "But the " + enemy + "takes one look at "
                    "your shiny new toy and runs away!"
                )
                print_pause(
                    "You have rid the town of the " + enemy + ". You are victorious!\n"
                )
            else:
                print_pause("You do your best...")
                print_pause(
                    "but your rusty old magic wand is no match for the " + enemy + "."
                )
                print_pause("You have been turned into a frog!")
            play_again()
            break
        if choice_two == "2":
            print_pause(
                "You run back into the field. "
                "Luckily, you don't seem to have been followed."
            )
            field(items, enemy)
            break


def intro(items: list, enemy: str):
    """
    The game introduction, including introducing the enemy
    """ 
    print_pause(
        "You find yourself standing in an open field, filled "
        "with grass and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a " + enemy + " is somewhere around "
        "here, and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty"
        "(but not very effective) rusty old magic wand."
    )


def field(items: list, enemy: str):
    """
    After the game introduction, showing what happens in the field
    """ 
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    while True:
        choice_one = input("(Please enter 1 or 2).\n")
        if choice_one == "1":
            house(items, enemy)
            break
        elif choice_one == "2":
            cave(items, enemy)
            break


def play():
    """
    Init the game
    """
    items = []
    enemeis = [
        "wicked fairie", "pirate",
        "dragon", "troll", "gorgon"
    ]
    enemy = random.choice(enemeis)

    intro(items, enemy)
    field(items, enemy)


if __name__ == "__main__":
    play()