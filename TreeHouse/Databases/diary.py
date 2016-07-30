import datetime
import os
import sys
from collections import OrderedDict

from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    # TextField => holds any amount of text
    # varchar => not using due to varchar needing to have a max_length
    content = TextField()
    # .now => default sees this a function and does not need the (), w/o the () it will also state when it was written
    # .now() => if you put () after, the datetime will state what time the script was run and not written
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the tables if they do not exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
    """Show the menu"""
    # sets variable w/o value
    choice = None

    while choice != 'q':
        clear()
        print('Enter "q" to quit.')
        # menu.items() => gives tuple
        for key, value in menu.items():
            # value.__doc__ => is the doc string for add_entry
            print('{}) {}'.format(key, value.__doc__))
        choice = raw_input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()


def add_entry():
    """Add an entry"""
    print("Enter your entry. Press Ctrl+Z and Enter when finished.")
    data = sys.stdin.read().strip()

    if data:
        if raw_input("Save entry? Y/N ").lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!\n\n")


def view_entries(search_query=None):
    """View previous entries"""
    # view entries from most recent to oldest
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        # .where() => adds filter
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %S %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n' + '=' * len(timestamp))
        print('N) for next entry')
        print('D) to delete entry')
        print('Q) return to main menu')

        next_action = raw_input('Action: N/D/Q ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entries():
    """Search entries for a string"""
    view_entries(raw_input("Search query: "))


def delete_entry(entery):
    """Delete  an entry"""
    if raw_input('Are you sure? Y/N? ').lower() == 'y':
        entery.delete_instance()
        print('Entry was deleted. \n')


# OrderedDict => remembers the order items were added, this creating a list
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

# runs the file
# this will allow us to import the diary
if __name__ == '__main__':
    # makes sure that initialize runs and the db exist.
    initialize()
    menu_loop()
