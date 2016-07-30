from __future__ import print_function

# copy => allows us to make copies
from copy import copy
from functools import partial, reduce
# imports json files
import json
from operator import attrgetter, itemgetter


class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)


def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return {}
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]


BOOKS = get_books('books.json')
# reverse=True => flips the answer around
pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)
pages_sort2 = sorted(BOOKS, key=attrgetter('number_of_pages'), reverse=True)
print(pages_sort2[0].number_of_pages, pages_sort2[-1].number_of_pages)
#   245 1141
#   1141 245


# Raw_books => list of dict.
RAW_BOOKS = get_books('books.json', raw=True)
# key => **kwargs to sorted that says to use this thing as the key you are going to be sorting by
pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
#   1975 2011


important_list = [5, 3, 1, 2, 4]
# important_list.sort()       # Bad idea, sorts list in place
# sorted() => returns a copy of the sorted list without changing the list permanently.
print(sorted(important_list))
print(important_list)
#   [1, 2, 3, 4, 5]
#   [5, 3, 1, 2, 4]


a = [1, 2, 3]

def double(n):
    return n * 2
print(list(map(double, a)))
#   [2, 4, 6]


### MAP ###
# mapping is focused more on application or apply
def sales_price(book):
    """Apply a 20% discount to the book's original price"""
    # book => is a copy of a book, this will not modify the original book in the json file
    book = copy(book)
    # takes 20% off and rounds to the nearest 2 digits
    book.price = round(book.price-book.price*.2, 2)
    return book

# gets sales book with map for sales price
sales_books = list(map(sales_price, BOOKS))
# puts sales_price(book) into the for loop for each book in BOOKS
sales_books2 = [sales_price(book) for book in BOOKS]
print(BOOKS[0].price)
print(sales_books[0].price)
#   13.55
#   10.84


### FILTER ###
# filter is focused more on a question
def is_long_book(book):
    """Does a book have 600+ pages"""
    return book.number_of_pages >= 600

# filter (for larger programs)
long_books = list(filter(is_long_book, BOOKS))
# comprehension (for simple filters)
long_books2 = [book for book in BOOKS if book.number_of_pages >= 600]
print(len(BOOKS))
print(len(long_books))
print(len(long_books2))
#   28
#   12
#   12


### CHAINING ###
def has_roland(book):
    # any() => returns true or false if any of the intervals passed into the intervals are true
    return any(['Roland' in subject for subject in book.subjects])


def titlecase(book):
    book = copy(book)
    # title => give us back the title case on title
    book.title = book.title.title()
    return book

# list => comes first
# map => works form the inside out
# filter => if filter is done first then we are only title casing the filtered books
print(list(map(titlecase, filter(has_roland, BOOKS))))
#       [The Drawing Of The Three (The Dark Tower, Book 2), Song Of Susannah (The Dark Tower, Book 6), The
#           Dark Tower (The Dark Tower, Book 7), The Waste Lands (The Dark Tower, Book 3), Wizard And Glass,
#           Wolves Of The Calla (The Dark Tower, Book 5), The Gunslinger (The Dark Tower, Book 1)]


def is_good_deal(book):
    # returns book less then $5
    return book.price <= 5

# sorted() => sorts all of the books
# filter() => filters all of the books by is_good_deal
# map() => maps sales_price
# key=attrgetter => gets attribute price
#   FOUND ALL SALE BOOKS, THEN FOUND WHAT WAS $5 OR LESS, THEN SORTED THEM BY PRICE
cheap_books = sorted(
    filter(is_good_deal, map(sales_price, BOOKS)),
    key=attrgetter('price')
)

print(cheap_books)
print(cheap_books[0])
print(cheap_books[0].price)
#   [Needful things, Wizard and glass, Misery, The Gunslinger (The Dark Tower, Book 1), Pet sematary,
#       The Shining]
#   Needful things
#   2.8


# As a dumb American, I don't understand Celsius temperatures. Using c_to_f and a list comprehension, create
#   a variable named good_temps. Convert each Celsius temperature into Fahrenheit, but only if the Celsius
#   temperature is between 9 and 32.6.
temperatures = [
    37,
    0,
    25,
    100,
    13.2,
    29.9,
    18.6,
    32.8
]


def c_to_f(temp):
    """Returns Celsius temperature as Fahrenheit"""
    return temp * (9/5) + 32

good_temps = [c_to_f(temp) for temp in temperatures if temp > 9 and temp < 32.6]


### REDUCE ###
def product(x, y):
    return x * y

print(reduce(product, [1, 2, 3, 4, 5]))
#   120

'''This one is a bit messier than the one above using reduce'''
total = 1
for x in [1, 2, 3, 4, 5]:
    total = x * total

print(total)
#   120

def add_book_prices(book1, book2):
    return book1 + book2

# list comprehension: b.price for b in BOOKS
total = reduce(add_book_prices, [b.price for b in BOOKS])
print(total)


### RECURSION ###
# keep building up on the same thing, reduce is so much easier
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
#   120


# Finish the prereqs function so that it recursively finds all of the prerequisite course titles in courses
#   (like "Object-Oriented Python" is a prerequisite for "Django Basics"). You should add() the title of the
#   prerequisite to the pres set and then call prereqs again with the child courses. In the end, return the
#   prereqs set.
courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                        'title': 'Object-Oriented Python',
                        'prereqs': [{'count': 1,
                                     'title': 'Python Collections',
                                     'prereqs': [{'count': 0,
                                                  'title': 'Python Basics',
                                                  'prereqs': []}]},
                                    {'count': 0,
                                     'title': 'Python Basics',
                                     'prereqs': []},
                                    {'count': 0,
                                     'title': 'Setting Up a Local Python Environment',
                                     'prereqs': []}]},
                       {'count': 0,
                        'title': 'Flask Basics',
                        'prereqs': []}]}


def prereqs(data, pres=None):
    pres = pres or set()
    # for each prereq in this courses prereq:
    for prereq in data['prereqs']:
        # add title of this prereq course, then
        pres.add(prereq['title'])
        # use recursive call to find further prereq of this course, if any
        prereqs(prereq, pres)
    # return current
    return pres


### LANBDA ###
# are supposed to be only one line long
# can not contain assignments
# only want to reference one time
# can give names but they really don't have to, in fact it is a little weird if named
# lanbda automatically returns the last value calculated
# lambda x, y: x + y => is kinda like def in set up
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
print(total)
#   225.3

long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
print(len(list(long_books)))
#   12

good_deals = filter(lambda book: book.price <= 6, BOOKS)
print (len(list(good_deals)))
#   6F

# Use a lambda and filter() to create a variable named high_cal with only the items in meals where the
#   "calories" value is greater than 1000.
meals = [
    {'name': 'cheeseburger',
     'calories': 750},
    {'name': 'cobb salad',
     'calories': 250},
    {'name': 'large pizza',
     'calories': 1500},
    {'name': 'burrito',
     'calories': 1050},
    {'name': 'stir fry',
     'calories': 625}
]

high_cal = filter(lambda meal: meal['calories'] > 1000, meals)

# Use reduce() and a lambda to find the longest string in strings. Save this value in the variable longest.
#   Remember, reduce() takes two arguments and you can write an if statement like: give_me_this if this_
#   thing > that_thing else give_me_that.

from functools import reduce

strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
    "A day without sunshine is like, you know, night.",
    "Get your facts first, then you can distort them as you please.",
    "My grandmother started walking five miles a day when she was sixty. She's ninety-seven know and we don't know where she is.",
    "Life is hard. After all, it kills you.",
    "All my life, I always wanted to be somebody. Now I see that I should have been more specific.",
    "Everyone's like, 'overnight sensation.' It's not overnight. It's years of hard work.",
]

longest = reduce(lambda x, y: x if len(x) > len(y) else y, strings)


### PARTIALS ###
# They allow us to partially call on a function that we need
def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price-book.price*discount, 2)
    return book

# mark_down => function being called
# discount => arg
standard = partial(mark_down, discount=.2)
print(standard(BOOKS[0]).price)
print(standard(BOOKS[5]).price)
#   10.84
#   6.39
half = partial(mark_down, discount=.5)
print(half(BOOKS[0]).price)
print(half(BOOKS[5]).price)
#   6.78
#   4.0

# mark down all of the books
half_price_books = map(half, filter(is_long_book, BOOKS))
print(list(half_price_books))
#   [11/22/63, Bag of bones, Dreamcatcher, Duma Key, It, Needful things, The dark tower (The Dark Tower,
#       Book 7), The stand, The Tommyknockers, The Waste Lands (The Dark Tower, Book 3), Wizard and glass,
#       Wolves of the Calla (The Dark Tower, Book 5)]


### CURRYING ###
# can call on a function if that function does not have enough arg will fill in as many arg as it can and
#   send you a new one
def curried_f(x, y=None, z=None):
    def f(x, y, z):
        return x**3 + y**2 + z

    if y is not None and z is not None:
        return f(x, y, z)
    if y is not None:
        return lambda z: f(x, y,z)

    return lambda y, z=None: (
        f(x, y, z) if (y is not None and z is not None)
        else (lambda z: f(x, y, z)))

print(curried_f(2, 3, 4))
#   21
g = curried_f(2)
print(g)
h = g(3)
print(h)
i = h(4)
print(i)
#   <function <lambda> at 0x0000000002817128>
#   <function <lambda> at 0x0000000002817198>
#   21
