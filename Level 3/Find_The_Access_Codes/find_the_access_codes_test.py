import unittest
from find_the_access_codes import solution

class TestFindTheAccessCodes(unittest.TestCase):

  def test_One(self):
      self.assertEqual(solution([1, 1, 1]), 1)

  def test_Two(self):
      self.assertEqual(solution([1, 2, 3, 4, 5, 6]),3)


if __name__ == '__main__':
  unittest.main()