# The test.py file is designed to test the functionality of the W class using Python's unittest framework.
import unittest
from W_class import W

class Test(unittest.TestCase):

    def setUp(self):
        self.instance = W(30, 80.5, 10, 5, 2024)

    # This method tests the get_dates method of the W class. It defines an expected list of dates and checks if the output from get_dates() method matches this list.
    def test_get_dates(self):
        expected_dates = ['2024-10-05', '2023-10-05', '2022-10-05', '2021-10-05', '2020-10-05']
        self.assertEqual(self.instance.get_dates(), expected_dates)

    # This method tests the temp method of the W class. It checks if the output is a list. Then, it asserts that this list contains 5 temperature readings and finally verifies that each element in the list is either an integer or a float.
    def test_temp(self):
        temp_data = self.instance.temp()
        self.assertIsInstance(temp_data, list)
        self.assertEqual(len(temp_data), 5)
        for temp in temp_data:
            self.assertIsInstance(temp, (int, float))

    # The last method tests the aggregate method of the W class. It checks that the average, minimum, and maximum temperature attributes are not None, ensuring that these calculations were performed.
    def test_aggregate(self):
        self.instance.aggregate()
        self.assertIsNotNone(self.instance.avg_temp)
        self.assertIsNotNone(self.instance.min_temp)
        self.assertIsNotNone(self.instance.max_temp)

# Call the unittest
if __name__ == '__main__':
    unittest.main()
