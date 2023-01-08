import unittest
import app


class TestApp(unittest.TestCase):

  def test_add(self):
    self.assertEqual(app.add(9,6), 15)
    self.assertEqual(app.add(8,5), 13)
    self.assertEqual(app.add(-1,-1),-2)
    self.assertEqual(app.add(100,5), 105)

if __name__ == '__main__':
  unittest.main()
