from unittest import TestCase
from quicksort import quicksort


class QuicksortTest(TestCase):
    def test_quicksort_positive(self):
        expected1 = [2, 3, 5, 6, 10]
        expected2 = [12, 13, 15, 16, 100]
        
        answer1 = quicksort([5, 3, 6, 2, 10])
        answer2 = quicksort([15, 13, 16, 12, 100])
    
        self.assertEqual(expected1, answer1)
        self.assertEqual(expected2, answer2)

    def test_quicksort_negative(self):
        expected1 = [-10, -6, - 5, -3, -2]
        expected2 = [-100, -16, -15, -13, -12]

        answer1 = quicksort([-5, -3, -6, -2, -10])
        answer2 = quicksort([-15, -13, -16, -12, -100])

        self.assertEqual(expected1, answer1)
        self.assertEqual(expected2, answer2)

    def test_quicksort_mixed_nums(self):
        expected1 = [-10, -6, - 5, 2, 3]
        expected2 = [-15, -13, -12, 16, 100]

        answer1 = quicksort([-5, 3, -6, -10, 2])
        answer2 = quicksort([16, -13, 100, -12, -15])

        self.assertEqual(expected1, answer1)
        self.assertEqual(expected2, answer2)
    
    