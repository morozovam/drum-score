import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # There is dummy test


if __name__ == "__main__":
    unittest.main()
