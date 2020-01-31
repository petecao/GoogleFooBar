import unittest
from en_route_salute import solution

class TestEnRouteSalute(unittest.TestCase):

  def test_One(self):
      self.assertEqual(solution(">----<"), 2)

  def test_Two(self):
      self.assertEqual(solution("<<>><"),4)


if __name__ == '__main__':
  unittest.main()