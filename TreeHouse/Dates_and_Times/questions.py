# quiz that asks 10 randomized questions for adding and multiply

class Question(object):
    # the answer to the question
    answer = None
    # info that goes into the question
    text = None


class Add(Question):
    # __init__ will override.We are adding in num1 and num2, as these will hold the values going into the questions.
    def __init__(self, num1, num2):
        # self.text => the question
        self.text = "{} + {}".format(num1, num2)
        # self.anser => the answer to the question
        self.answer = num1 + num2


class Multiply(Question):
    # Basically the same as above, but multiply instead of adding
    def __init__(self, num1, num2):
        self.text = '{} * {}'.format(num1, num2)
        self.answer = num1 * num2

# TEST RUN
# >>> sys.path.extend(['C:\\Users\\mittsy\\Google Drive\\PROGRAMMING\\PYTHON\\TreeHouse\\Dates_and_Times'])
# >>> from questions import Add
# >>> add1 = Add(5, 7)
# >>> add1.text
# '5 + 7'
# >>> add1.answer
# 12