import unittest
from merge_the_tools import merge_the_tools


class TestMergeTheToolsCase(unittest.TestCase):
    def test_valid_example_one(self):
        input, k = "AABCADDD", 2
        expected = ["A", "BC", "AD", "D"]
        self.assertEqual(merge_the_tools(input, k), expected)


if __name__ == '__main__':
    unittest.main()
