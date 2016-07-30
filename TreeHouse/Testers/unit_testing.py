# All the info we need for unit testing is in the python standard library
#   These will need to be imported each time they are used
#   Set-up-
#   Tear-down-
# Must run unit test on the side panel with files in order to run all test in file
#   if you run unit test inside the file then only one will run


# STEPS FOR UNITTEST
#   1. Import unittest
#   2. Group test in test case
#   3. Test have to start with 'test'


# TEST CHALLENGE 2
# class SimpleTestCase(unittest.TestCase):
#    def test_simple(self):
#        assert 10 - 10 == 0



import unittest
from moves import Move


class MoveTests(unittest.TestCase):
    # test has to start with test
    def test_five_plus_five(self):
        # assert => what comes after assert must be true
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        # even tho it is false, the not behind assert makes it true
        assert not 1 + 1 == 3

if __name__ == '__main__':
    unittest.main()
