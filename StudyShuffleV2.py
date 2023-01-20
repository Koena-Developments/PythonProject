from random import choice


class Student:
    def __init__(self):
        self.name = ""
        self.Grade = int()
        self.Subjects = []

    def add_information(self):
        self.name = str(input("Please enter name ")).title()
        self.Grade = int(input("Please enter grade "))
        i = 3
        while i > len(self.Subjects):
            subjects = str(input("Please enter your subject ")).title()

            if len(subjects) == 0:
                print("Can't leave space blank")
            else:
                self.Subjects.append(subjects)
        return print(f'{self.Subjects}\t, Hello {self.name}, You are to study {choice(self.Subjects)} for 2hrs')

    def reshuffle(self):
        reshuffle = str(input("would you like to reshuffle (Yes/No) ")).title()
        if reshuffle == "Yes":
            print(f'from list {self.Subjects}\t, here is the subject you should study {choice(self.Subjects)}')
        else:
            exit(reshuffle)
        return 0

    # if maths is the chosen subject the program should use the grade of student as well as the subject that's shuffled
    # to find PAST PAPERS AND NOTES
    def study_material(self):
        pass

    # I want this function to take in input from user and return a summarized answer from the internet
    def take_in(self):
        pass


if __name__ == '__main__':
    student = Student()
    print(student.add_information())
    print(student.reshuffle())
