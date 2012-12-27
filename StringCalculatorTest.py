import unittest
from StringCalculator import add

class TestStringCalculator(unittest.TestCase):
  def test_add_empty_string(self):
    self.assertEqual(add(""), 0)

  def test_add_single_number(self):
    self.assertEqual(add("1"), 1)


if __name__ == '__main__':
  unittest.main()
