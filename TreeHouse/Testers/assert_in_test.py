# Assert test a condition in your code that must be met


# ASSERT TRUE AND ASSERT FALSE OBJECTIVE:
#   import unittest
#   from string_fun import is_palindrome
#
#   class PalindromeTestCase(unittest.TestCase):
#       def test_good_palindrome(self):
#           self.assertTrue(is_palindrome("tacocat"))
#
#       def test_bad_palindrome(self):
#           self.assertFalse(is_palindrome(self))


import unittest
import moves

class MoveTests(unittest.TestCase):
    # test has to start with test
    def setUp(self):
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()

    def test_five_plus_five(self):
        # assert => what comes after assert must be true
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        # even tho it is false, the not behind assert makes it true
        assert not 1 + 1 == 3

    def test_equal(self):
        self.assertEqual(self.rock, moves.Rock())

    def test_not_equal(self):
        self.assertNotEqual(self.rock, self.paper)

    def test_rock_better_than_scissors(self):
        # assertGreater => a > b
        self.assertGreater(self.rock, self.scissors)

    def test_paper_worse_than_scissors(self):
        # assertLess => a < b
        self.assertLess(self.paper, self.scissors)
if __name__ == '__main__':
    unittest.main()


