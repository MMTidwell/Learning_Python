# ASSERTIN CHALLENGE
# import unittest
#
# from string_fun import get_anagrams
#
#
# class AnagramTests(unittest.TestCase):
#   def test_in_anagrams(self):
#       self.assertIn('house', get_anagrams('treehouse'))
#
#   def test_not_in_anagrams(slef):
#       self.assertNotIn('code', get_anagrams(self))

import unittest
import membership_assertions


class DieTests(unittest.TestCase):
    def setUp(self):
        # self. number of dice = file_name . Class (number of dice)
        self.d6 = membership_assertions.Die(6)
        self.d8 = membership_assertions.Die(8)

    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertIn(self.d6.value, range(1, 7))

    def test_add(self):
        self.assertIsInstance(self.d6 + self.d8, int)

    def test_bad_sides(self):
        with self.assertRaises(ValueError):
            membership_assertions.Die(1)


class RollTest(unittest.TestCase):
    def setUp(self):
        self.hand1 = membership_assertions.Roll('1d2')
        self.hand3 = membership_assertions.Roll('3d6')

    def test_lower(self):
        # int is used because of __init__ in original class, 3 is the smallest number you can get
        self.assertGreaterEqual(int(self.hand3), 3)

    def test_upper(self):
        # 18 is the highest number you can roll with 3 dice
        self.assertLessEqual(int(self.hand3), 18)

    def test_membership(self):
        # 2 => refers to the number of dice
        test_die = membership_assertions.Die(2)
        test_die.value = self.hand1.results[0].value
        self.assertIn(test_die, self.hand1.results)

    # this test examines the value error in membership_assertions
    def test_bad_description(self):
        # with => context variable that can be changed
        # assertRaises a value error
        with self.assertRaises(ValueError):
            # file name with valueError.Class name(we know that the '2b6' is wrong as we are wanting to call
            # the value error
            membership_assertions.Roll('2b6')

    def test_adding(self):
        self.assertEqual(self.hand1+self.hand3,
                         sum(self.hand1.results)+sum(self.hand3.results))

if __name__ == '__main__':
    unittest.main()

