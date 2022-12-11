# Create an empty list that will store subjects to be shuffled
import sys
from random import choice


def add() -> object:
    # declare an empty list
    subjects = []
    # Create a box full of motivational quotes ;)
    GuiltBox = ["Oh well, i guess you gonna miss-out on that dream car that you always wanted :(",
                "Think about your goals", "You are gonna have a family that is gonna depend on you, so invest in "
                                          "yourself now so that you are earning more than average",
                "Your wife should earn way less than you",
                "Which girl would want to confide in someone who is lazy to achieve goals for themselves."]

    # prompt user to enter name
    name = input("Please enter your name: ").title()

    # welcomes user to the program
    print(f"Hello {name}, Welcome to study Timetable")

    # Conditional statement
    while True:

        new_subjects = str(input("please enter your subjects: "))

        subjects.append(new_subjects)

        print(f"You have entered the following subject: {new_subjects}")

        option = input("Are you done entering your subject: yes or no: ")

        if option == "yes":
            break
        else:
            continue

    print(subjects)
    # Ask if user would like to study now or later

    OPTION = input("Would you like to study now?").title()

    if OPTION == "Yes":
        print(f"hey {name} you are to study: ", choice(subjects), " For 2hrs")
        return subjects, name, new_subjects
    else:
        print(choice(GuiltBox))


def main():
    add()


main()



