import unittest
from elevator_maintenance import solution

class TestElevatorMaintenance(unittest.TestCase):

  def test_One(self):
      self.assertEqual(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]), "0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0")

  def test_Two(self):
      self.assertEqual(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]),"1.0,1.0.2,1.0.12,1.1.2,1.3.3")


if __name__ == '__main__':
  unittest.main()