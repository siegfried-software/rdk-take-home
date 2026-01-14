import unittest
from main import sortAndFindMedian

class TestAlgorithms(unittest.TestCase):
    # The following tests should pass if they ARE equal
    def test_eq_1(self):
        numbers = [5, 3, 1, 8, 9, 10, 2, 7, 6, 4] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        median1 = 5.5
        median2 = sortAndFindMedian(numbers)
        self.assertAlmostEqual(median1, median2)
    
    def test_eq_2(self):
        numbers = [11, 1, 91, 85, 157] # [1, 11, 85, 91, 157]
        median1 = 85
        median2 = sortAndFindMedian(numbers)
        self.assertAlmostEqual(median1, median2)

    def test_eq_3(self):
        numbers = [1007, 762, -111, 942, -7] # [-111, -7, 762, 942, 1007]
        median1 = 762
        median2 = sortAndFindMedian(numbers)
        self.assertAlmostEqual(median1, median2)

    def test_eq_4(self):
        numbers = [3, 2, 1] # [1, 2, 3]
        median1 = 2
        median2 = sortAndFindMedian(numbers)
        self.assertAlmostEqual(median1, median2)

    def test_eq_5(self):
        numbers = [3] # [3]
        median1 = 3
        median2 = sortAndFindMedian(numbers)
        self.assertAlmostEqual(median1, median2)

    # The following tests should pass if they AREN't equal
    def test_not_eq_1(self):
        numbers = [5, 3, 1, 8, 9, 10, 2, 7, 6, 4] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        median1 = 8
        median2 = sortAndFindMedian(numbers)
        self.assertNotAlmostEqual(median1, median2)

    def test_not_eq_2(self):
        numbers = [819, 222, 712, 1232, 908, 21312, 898, 566] # [222, 566, 712, 819, 898, 908, 1232, 21312]
        median1 = 200
        median2 = sortAndFindMedian(numbers)
        self.assertNotAlmostEqual(median1, median2)
    
    def test_not_eq_3(self):
        numbers = [3] # [3]
        median1 = 5
        median2 = sortAndFindMedian(numbers)
        self.assertNotAlmostEqual(median1, median2)

if __name__ == "__main__":
    unittest.main()
 
