import unittest
from timedelta_handson import time_delta


class TestTimeDelta(unittest.TestCase):
    def test_long_list_of_dates(self):
        """
        HackerRank 'Test case 1'
        """
        input_list = []
        with open('./fixtures/100_dates_input.txt', 'r') as f:
            n_tests = int(next(f))
            # print(f"Number of dates to convert: {n_tests}")
            for line in f:
                input_list.append(line.strip())

        expected_list = []
        with open('./fixtures/100_dates_expected.txt', 'r') as f:
            for line in f:
                expected_list.append(line.strip())

        self.assertEqual(len(input_list), 2*len(expected_list))

        for i, expected in enumerate(expected_list):
            # print("Testing: ", input_list[2*i], "-", input_list[2*i+1])
            timedelta_output = time_delta(input_list[2*i], input_list[2*i + 1])
            self.assertEqual(expected, timedelta_output)


if __name__ == "__main__":
    unittest.main()
