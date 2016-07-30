from __future__ import print_function

import re

# names_file, data, and names_file.close() will allow you to open, read, and close the file
# Original: names_file = open('names.txt', encoding='utf-8')
#   This does not work with python 2.7. When you take out the encoding='utf-8' things work fine.
names_file = open('names.txt')
data = names_file.read()
names_file.close()

# print(data)
#   C:\Users\mittsy\Google Drive\PROGRAMMING\PYTHON\TreeHouse\Reg_Expressions>python address_book.py
#   Tidwell     Mittsy      mtidwell506@gmail.com       817-301-6167        student
#   Kessler     Tim         patrialt@gmail.com          210-900-7128        developer       USAA
#   Mcwhorter   Mary        marymcw@gmail.com           817-261-1248        retired
#   Askins      Andrea      andreaa@agacistore.com      817-706-4138        recruiter       Agaci
#   Kendrick    Mel                                     817-992-8105        Store Opps      EBT
#   Gental      Tammy                                   609-306-9075        Sales Rep       Mary Kay
#   Stanley     Noil                                    972-670-0058        Developer
#   Tidwell     Russell     russtidwell78@yahoo.com     817-675-1664        Contractor

last_name = r'Love'
first_name = r'Kenneth'

print('___Searching by name, and variables___')
# Prints and finds the word 'Tidwell' or 'Mittsy'
# r => raw string
# re.match => only checks the beginning of the string
# re.search => checks the whole txt file
print(re.match(r'Love', data))
print(re.search(r'Kenneth', data))
# Returns this while it should be: <_sre.SRE_Match object; span=(0, 4), match='Love'>
#   <_sre.SRE_Match object at 0x000000000266A510>
#   <_sre.SRE_Match object at 0x000000000266A510>

# Prints the same as above but with variables instead of words
print(re.match(last_name, data))
print(re.search(first_name, data))
#   <_sre.SRE_Match object at 0x0000000000EEA510>
#   <_sre.SRE_Match object at 0x0000000000EEA510>

print('\n___Searching by escape hatches___')
print(re.match(r"\w,\w", data))
# Prints phone numbers
print(re.search(r'\(\d\d\d\)-\d\d\d-\d\d\d\d', data))
#   Only give the first line of the txt file
#   None
#   None


# ESCAPES CHALLENGE
# def first_number(arg):
#    return (re.search(r'\d', arg))


# def numbers(arg1, arg2):
#     return (re.search(r'\d' * arg1, arg2))

print('\n___Searching by escape hatches and counts___')
# searching for one or more letters
# want to find \w (word characters) + (1 or more word characters)
print(re.findall(r'\w*,\w+', data))
# ? => makes '()' optional
# re.search => searches the first line of txt file
print(re.search(r'\(?\d{3}\)?-?\s\d{3}-\d{4}', data))
# searches all of the txt file
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
#   ['Love, Kenneth', 'Teacher, Treehouse', 'McFarland, Dave', 'Teacher, Treehouse', 'Arthur, King', 'King, Camelot',
#        'sterberg, Sven', 'Governor, Norrbotten', ', Tim', 'Enchanter, Killer', 'Carson, Ryan', 'CEO, Treehouse',
#        'Doctor, The', 'Lord, Gallifrey', 'Exampleson, Example', 'Example, Example', 'Obama, Barack', 'President,
#        'United', 'Chalkley, Andrew', 'Teacher, Treehouse', 'Vader, Darth', 'Lord, Galactic', 'Sanz, Mar',
#        'Minister, Spanish']
#   <_sre.SRE_Match object at 0x00000000026304A8>
#   ['(555) 555-5555', '(555) 555-5554', '(555) 555-5543', '555-555-5552', '555 555-5551', '(555) 555-5553',
#        '(555) 555-4444']


print('\n___Sets___')
# prints out all emails
# + at the end makes it show multiple
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# looks for treehouse in the txt file
# Only have to type same letter once, so Treehouse turns into trehous
print(re.findall(r'\b[trehous]+\b', data, re.I))
print(re.findall(r'\b[trehous]{9}\b', data, re.I))
#   ['kenneth@teamtreehouse.com', 'dave@teamtreehouse.com', 'king_arthur@camelot.co.uk',
#       'governor@norrbotten.co.se', 'tim@killerrabbit.com', 'ryan@teamtreehouse.com',
#       'doctor+companion@tardis.co.uk', 'me@example.com', 'president.44@us.gov',
#       'andrew@teamtreehouse.com', 'darth-vader@empire.gov', 'mtfvs@spain.gov']
#   ['Treehouse', 'Treehouse', 'se', 'Treehouse', 'The', 'us', 'Treehouse']
#   ['Treehouse', 'Treehouse', 'Treehouse', 'Treehouse']



print('\n__Negation___')
# prints all email addresses that leaves off the .gov in the email
print(re.findall(r'''
    \b@[-\w\d.]*    # first word boundary, an @, and then any number of characters
    [^gov\t]        # ignore one or more of the letters g, o, or v and a tab
    \b              # match another word boundary
    # re,VERBOSE => lets us write our patterns out over multiple lines, ignoring whitespace and comments
''', data, re.VERBOSE|re.I))
print(re.findall(r'''
    \b[-\w]*,   # Find a wound boundary, 1+ hyphens or hcaracters, and a comma
    \s          # Find 1 whitespace
    [-\w ]+     # Ignore a tabs and newlines
    [^\t\n]     # Ignore tabs and newlines
    \b
''', data, re.X))
#   ['@teamtreehouse.com', '@teamtreehouse.com', '@camelot.co.uk', '@norrbotten.co.se', '@killerrabbit.com',
#       '@teamtreehouse.com', '@tardis.co.uk', '@example.com', '@us.', '@teamtreehouse.com', '@empire.', '@spain.']
#   ['Love, Kenneth', 'Teacher, Treehouse', 'McFarland, Dave', 'Teacher, Treehouse', 'Arthur, King', 'King, Camelot',
#       'sterberg, Sven-Erik', 'Governor, Norrbotten', 'Enchanter, Killer Rabbit Cave', 'Carson, Ryan', 'CEO,
#       Treehouse', 'Doctor, The', 'Lord, Gallifrey', 'Exampleson, Example', 'Example, Example Co', 'Obama, Barack',
#       'President, United States of America', 'Chalkley, Andrew', 'Teacher, Treehouse', 'Vader, Darth', 'Lord,
#       Galactic Empire', 'Sanz, Mar', 'Minister, Spanish Govt']



# Create a variable named good_numbers that is an re.findall() where the pattern matches anything in string except
#   the numbers 5, 6, and 7.
string = '1234567890'
good_numbers = re.findall(r'[^{5-7}]', string)


print('\n___Groups___')
print(re.findall(r'''
    # groups are defined with ()
    # [-\w ]+ => looks for the last name
    # \s[-\w +)\t => space[first name ]+ tab
    ([-\w ]+,\s[-\w ]+)\t          # first and last names
    #[-\w\d.+] => checks for words, numbers, ., +
    # +@ => checks @ sign
    # [-w\w\d\.]+)\t => checks for words, letters, numbers, and . after @ sign then checks for tab
    ([-\w\d.+]+@[-\w\d.]+)\t      # email
    # \(?\d{3}\)? => checks for () around area code as well as gets area code
    # ?\s?\d{3} => checks for '-' after area code, then gets the first 3 numbers of phone
    # \d{4})\t => gets last 4 pf phone then checks for tab
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})\t # phone
    # [\w\s]+, => words, character, and spaces
    # \s[\w\s]+)\t  => words, character, and spaces and tab
    ([\w\s]+,\s[\w\s]+)\t           # job
    (@[\w\d]+)                      # twitter
''', data, re.X))
#   THESE ARE MISSING A FEW DUE TO NOT MATCHING EXACTLY
#   [('Love, Kenneth', 'kenneth@teamtreehouse.com', '(555) 555-5555', 'Teacher, Treehouse', '@kennethlove'),
#       ('Carson, Ryan', 'ryan@teamtreehouse.com', '(555) 555-5543', 'CEO, Treehouse', '@ryancarson'),
#       ('Obama, Barack', 'president.44@us.gov', '555 555-5551', 'President, United States of America', '@potus44'),
#       ('Chalkley, Andrew', 'andrew@teamtreehouse.com', '(555) 555-5553', 'Teacher, Treehouse', '@chalkers'),
#       ('Vader, Darth', 'darth-vader@empire.gov', '(555) 555-4444', 'Sith Lord, Galactic Empire', '@darthvader')]
print(re.findall(r'''
    # ^ => marks the beginning of the string
    # * => optional
    ^([-\w ]*,\s[-\w ]+)\t          # first and last names
    ([-\w\d.+]+@[-\w\d.]+)\t      # email
    # ? => makes phone optional
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # phone
    ([\w\s]+,\s[\w\s.]+)\t?           # job
    # $ => marks the end of a string
    # ? => makes twitter optional
    (@[\w\d]+)?$                      # twitter
# re.MULTILINE or re.M => turns one big string into a lot of smaller strings
''', data, re.X|re.M))
#   [('Love, Kenneth', 'kenneth@teamtreehouse.com', '(555) 555-5555', 'Teacher, Treehouse\t', '@kennethlove'),
#       ('McFarland, Dave', 'dave@teamtreehouse.com', '(555) 555-5554', 'Teacher, Treehouse', ''),
#       ('Arthur, King', 'king_arthur@camelot.co.uk', '', 'King, Camelot', ''), (', Tim', 'tim@killerrabbit.com', '',
#       'Enchanter, Killer Rabbit Cave', ''), ('Carson, Ryan', 'ryan@teamtreehouse.com', '(555) 555-5543', 'CEO,
#       Treehouse\t', '@ryancarson'), ('Doctor, The', 'doctor+companion@tardis.co.uk', '', 'Time Lord, Gallifrey', ''),
#       ('Exampleson, Example', 'me@example.com', '555-555-5552', 'Example, Example Co.\t', '@example'),
#       ('Obama, Barack', 'president.44@us.gov', '555 555-5551', 'President, United States of America\t', '@potus44'),
#       ('Chalkley, Andrew', 'andrew@teamtreehouse.com', '(555) 555-5553', 'Teacher, Treehouse\t', '@chalkers'),
#       ('Vader, Darth', 'darth-vader@empire.gov', '(555) 555-4444', 'Sith Lord, Galactic Empire\t', '@darthvader')]


print('\n___Named Groups___')
line = re.search(r'''
    # ?P<name> => this is what makes it a name
    ^(?P<Name>[-\w ]*,\s[-\w ]+)\t                  # first and last names
    (?P<Email>[-\w\d.+]+@[-\w\d.]+)\t               # email
    (?P<Phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t       # phone
    (?P<Job>[\w\s]+,\s[\w\s.]+)\t?                  # job
    (?P<Twitter>@[\w\d]+)?$                         # twitter
''', data, re.X|re.M)
print(line)
print(line.groupdict())
#   <_sre.SRE_Match object at 0x0000000002626C68>
#   {'Email': 'kenneth@teamtreehouse.com', 'Phone': '(555) 555-5555', 'Job': 'Teacher, Treehouse\t',
#       'Twitter': '@kennethlove', 'Name': 'Love, Kenneth'}


# Name Group Challenge
#   Create a variable names that is an re.match() against string. The pattern should provide two groups, one for a
#       last name match and one for a first name match. The name parts are separated by a comma and a space.
string = 'Perotto, Pier Giorgio'
names = re.match(r'(\w+), ([\w ]+)', string)

# Email Groups Challenge
#   1. Create a new variable named contacts that is an re.search() where the pattern catches the email address and
#       phone number from string. Name the email pattern email and the phone number pattern phone. The comma and
#       spaces * should not* be part of the groups.
#   2. Great! Now, make a new variable, twitters that is an re.search() where the pattern catches the Twitter
#       handle for a person. Remember to mark it as being at the end of the string. You'll also want to use the
#       re.MULTILINE flag.
string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s
    (?P<phone>\d{3}-\d{3}-\d{4})
''', string, re.X|re.M)

twitters = re.search(r'(?P<twitter>@[\w\d]+)$', string, re.M)


print('\n___Compiling and Loops___')
# Saves pattern in a state and used as a regular expression
# Make sure that you take out the string that it is pulling info from, this will make it more generic and run
#   against a lot of different things
line = re.compile(r'''
    # ?P<name> => this is what makes it a name
    ^(?P<Name>[-\w ]*,\s[-\w ]+)\t                  # first and last names
    (?P<Email>[-\w\d.+]+@[-\w\d.]+)\t               # email
    (?P<Phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t       # phone
    (?P<Job>[\w\s]+,\s[\w\s.]+)\t?                  # job
    (?P<Twitter>@[\w\d]+)?$                         # twitter
''', re.X|re.M)
# This is where you are going to specify the string tha you will be pulling from
print(re.search(line, data).groupdict())
print(line.search(data).groupdict())
# Gives back an iterable of each non-overlapping match
# .finditer() => gives us an iterable full of match objects
for match in line.finditer(data):
    print(match.group('Name'))
#   {'Email': 'kenneth@teamtreehouse.com', 'Phone': '(555) 555-5555', 'Job': 'Teacher, Treehouse\t',
#       'Twitter': '@kennethlove', 'Name': 'Love, Kenneth'} {'Email': 'kenneth@teamtreehouse.com',
#       'Phone': '(555) 555-5555', 'Job': 'Teacher, Treehouse\t', 'Twitter': '@kennethlove', 'Name': 'Love, Kenneth'}
#   Love, Kenneth
#   McFarland, Dave
#   Arthur, King
#   , Tim
#   Carson, Ryan
#   Doctor, The
#   Exampleson, Example
#   Obama, Barack
#   Chalkley, Andrew
#   Vader, Darth


print('\n___Creating Subgroups___')
line = re.compile(r'''
    ^(?P<Name>(?<last>[-\w ]*),\s(?P<first>[-\w ]+))\t                  # first and last names
    (?P<Email>[-\w\d.+]+@[-\w\d.]+)\t                                   # email
    (?P<Phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t                           # phone
    (?P<Job>[\w\s]+,\s[\w\s.]+)\t?                                      # job
    (?P<Twitter>@[\w\d]+)?$                                             # twitter
''', re.X|re.M)
for match in line.finditer(data):
    print('{first} {last} <{Email}>'.format(**match.groupdict()))
# not working due to syntax error but might work in python 3


# PLAYERS DICTS AND CLASS CHALLENGE
#   1. Create a variable named players that is an re.search() or re.match() to capture three groups: last_name,
#      first_name, and score. It should include re.MULTILINE.
#   2.Wow! OK, now, create a class named Player that has those same three attributes, last_name, first_name, and
#       score. I should be able to set them through __init__.
string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
    ^(?P<last_name>[\w\s]+),\s
    (?P<first_name>[\w\s]+):\s
    (?P<score>[\d]+)?$
''', string, re.X|re.M)


class Player:
    def  __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score