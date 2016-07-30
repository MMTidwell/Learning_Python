# IMPORTS ALL OF PEEWEE (NOT NORMALLY WHAT WE WOULD LIKE TO DO
from peewee import *

# MAKE THE DATABASE AND MAKE A CONNECTION TO SQLITE
# this will make a database called students.db
db = SqliteDatabase('students.db')


# MAKE THE MODEL
class Student(Model):
    # Attributes become fields or columns in the database table
    # CharField => field that holds characters, this is AKA varchar (variable character)
    #   max_length => length of field
    #   unique => makes sure that the username's are not the same
    username = CharField(max_length=255, unique=True)
    # IntegerField => holds integers
    #   default => if not supplied then it will default to 0
    points = IntegerField(default=0)

    # Tells model what database it belongs to
    # This is not actually a meta class.
    class Meta:
        # setting an attribute, calls the database that we created with db
        database = db

# LIST OF DICT
students = [
    {'username': 'kennethlove', 'points': 14718},
    {'username': 'chalkers', 'points': 11912},
    {'username': 'joykesten2', 'points': 7363},
    {'username': 'craigsdennis', 'points': 4079},
    {'username': 'davemcfarland', 'points': 14717},
]


def add_students():
    for student in students:
        try:
            Student.create(username=student['username'], points=student['points'])
        except IntegrityError:
            # gets student out of database
            student_record = Student.get(username=student['username'])
            # update points to current
            student_record.points = student['points']
            # saves new record
            student_record.save()


def top_student():
    # Student.select() => pulls all students out of db
    # .order_by() => orders the students by the arg inside the ()
    # Student.points.desc() => orders the students from top to bottom based on points
    #   asc goes from bottom up (small to large)
    # .get() => gets the first student
    student = Student.select().order_by(Student.points.desc()).get()
    return student

# if file is run locally and not imported:
# prevents code from being excited when you import a module
if __name__ == '__main__':
    # connects to database
    db.connect()
    # creates tables
    # safe=True => used so that if we run it multiple times we will not get an error
    db.create_tables([Student], safe=True)
    # adds the students to the db
    add_students()
    print('Our top student right now is: {0.username}.'.format(top_student()))

# TERMINAL AT THIS POINT:
# C:\Users\mittsy\Google Drive\PROGRAMMING\PYTHON\TreeHouse\Databases>sqlite3 students.db
# SQLite version 3.13.0 2016-05-18 10:57:30
# Enter ".help" for usage hints.
# sqlite> .tables
# student
# sqlite> select * from student;
# sqlite> .exit

# C:\Users\mittsy\Google Drive\PROGRAMMING\PYTHON\TreeHouse\Databases>python students.py
# Our top student right now is: davemcfarland.

# C:\Users\mittsy\Google Drive\PROGRAMMING\PYTHON\TreeHouse\Databases>python students.py
# Our top student right now is: kennethlove.
