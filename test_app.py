import unittest
import app


class TestApp(unittest.TestCase):

  def test_add(self):
    result = app.add(9,6)
    self.assertEqual(result, 15)

if __name__ == '__main__':
  unittest.main()
