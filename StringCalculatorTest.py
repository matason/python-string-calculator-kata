import unittest
from StringCalculator import add

class TestStringCalculator(unittest.TestCase):
  def test_add_empty_string(self):
    self.assertEqual(add(""), 0)

  def test_add_single_number(self):
    self.assertEqual(add("1"), 1)

  def test_add_comma_separated_numbers(self):
    self.assertEqual(add("1,2"), 3)

  def test_unknown_number_of_arguments(self):
    self.assertEqual(add("1,2", "4,5"), 12)
    self.assertEqual(add("1,2", "4,5", ""), 12)

  def test_new_line_separator(self):
    self.assertEqual(add("1\n2,3"), 6)

if __name__ == '__main__':
  unittest.main()
