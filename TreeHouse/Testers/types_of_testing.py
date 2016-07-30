# When making test try to complete about 90% or better on test that are being run in code



# Unittest
# All the info we need for unit testing is in the python standard library
#   These will need to be imported each time they are used
# Must run unit test on the side panel with files in order to run all test in file
#   if you run unit test inside the file then only one will run


# STEPS FOR UNITTEST
#   1. Import unittest
#   2. Group test in test case
#   3. Test have to start with 'test'

import unittest


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




# Assert Testing
#   when using assert testing it must be met
import unittest

class MoveTests(unittest.TestCase):
    def test_five_plus_five(self):
        # assert => what comes after assert must be true
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        # even tho it is false, the not behind assert makes it true
        assert not 1 + 1 == 3



# Doc testing- can be test written inside a doc string inside of your code. They are very similar to doc string
def build_cells(width, height):
    # doc test are run side of doc strings and start with >>>
    # white space is needed on top and bottom of doc test due to python
    # the result you are looking for is directly under >>> without anything in front of it
    # if you type in something that it is not expecting you will get a failure on test run
    """create and return a width x height of 2-tuples

    >>> cells = build_cells(2, 2)
    >>> len(cells)
    4

    """
    cells = []
    for y in range(height):
        for x in range(width):
            cells.append((x, y))
    return cells

