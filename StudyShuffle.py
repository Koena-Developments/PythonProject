# Create an empty list that will store subjects to be shuffled
from random import choice


def add() -> object:
    # declare an empty list
    subjects = []

    # prompt user to enter name

    name = input("Please enter your name: ").title()

    # welcomes user to the program

    print(f"Hello {name}, Welcome to study Timetable")
    # Conditional statement,
    while True:
        # new_subjects variable holds prompt for user to enter subjects

        new_subjects = input("please enter your subjects:")
        # the new_subject variable value is added to the 'subjects' list
        subjects.append(new_subjects)

        print(f"You have entered the following subject: {new_subjects}")

        option = input("Are you done entering your subject: yes or no")

        if option == "yes":
            break
        else:
            continue

    # print out the list
    print(subjects)
    #
    print(f"hey {name} you are to study: ", choice(subjects), " For 2hrs")
    return subjects, name, new_subjects


add()
# first step find out if we can post this project on git-hub and slowly update it online if so then that is our first
# task

# BUGs
# just incase the user enter the same subject twice, we need to use sets instead of a list


# New features{urgent features before friday Upcoming features}
# I want to be able to store the subjects permanently for different people who use this program
# I want the program to be able to read out the subjects you are to study, for the sake of blind people
# create a user interface for the project


# Future features
# I want the program to be able to use machine learning to recommend types of subjects that are tailored for you (user)
