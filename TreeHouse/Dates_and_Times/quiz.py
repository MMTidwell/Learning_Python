# THERE IS A __FUTURE__ PROBLEM WITH THIS FILE THAT I CAN NOT FIND. THE PROGRAM WILL SAY "You got 0 answers correct out of 10." HOWEVER WHEN COPY/PASTE INTO PYTHON 3 IT WORKS PERFECTLY.

from __future__ import print_function

import random
import datetime

from questions import Add, Multiply


class Quiz(object):
    questions = []
    answers = []

    def __init__(self):
        # Generate 10 random q w numbers from 1-10
        # Add these q into self.questions
        # Question_types is set the pull the Add and Multiply classes from questions.py
        question_types = (Add, Multiply)
        # '_' shows python the we dont care about the value that comes out, we just want it counted
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            # grabs random question with random numbers
            question = random.choice(question_types)(num1, num2)
            # adds questions into the self.questions
            self.questions.append(question)

    def take_quiz(self):
        # Asks the q
        # Log the start time
        # Log if the q was right
        # Log end time
        # show summary
        self.start_time = datetime.datetime.now()
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
        return self.summary()

    def ask(self, question):
        # Log start time
        # capture the answer
        # check the answer
        # log the end time
        # if the answer is right send back true
        # else send back False
        # send back elapsed time
        correct = False
        questions_start = datetime.datetime.now()
        answer = input(question.text + ' = ')

        if answer == str(question.answer):
            correct = True

        questions_end = datetime.datetime.now()
        return correct, questions_end - questions_start

    def total_correct(self):
        # return the total number of correct answers
        total = 0
        for answer in self.answers:
            # checking for Truth
            if answer[0]:
                total += 1
                return total
        return total

    def summary(self):
        # print how many were right and total q
        print('You got {} answers correct out of {}.'.format(self.total_correct(), len(self.questions)))
        # print the total time for quiz
        print('That took {} seconds'.format((self.end_time - self.start_time).seconds))


Quiz().take_quiz()


# CHECK TO SEE IF THE CLASS QUIZ IS WORKING
# >>> sys.path.extend(['C:\\Users\\mittsy\\Google Drive\\PROGRAMMING\\PYTHON\\TreeHouse\\Dates_and_Times'])
# >>> from quiz import Quiz
# >>> quiz1 = Quiz()
# >>> quiz1.answers
# []
# >>> quiz1.questions
# [<questions.Add object at 0x00000000030149E8>, <questions.Multiply object at 0x0000000003014978>, <questions.Add object at 0x0000000003014748>, <questions.Add object at 0x00000000030149B0>, <questions.Add object at 0x0000000003014908>, <questions.Multiply object at 0x00000000030147F0>, <questions.Add object at 0x0000000003014860>, <questions.Add object at 0x0000000003014A20>, <questions.Add object at 0x0000000003014A58>, <questions.Multiply object at 0x0000000003014A90>]
# >>> quiz1.questions[0].text
# '10 + 1'
# >>> quiz1.answers[0].answer
# >>> quiz1.questions[0].answer
# 11
