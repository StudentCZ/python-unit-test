import unittest
import app


class TestApp(unittest.TestCase):

  def test_add(self):
    self.assertEqual(app.add(9,6), 15)
    self.assertEqual(app.add(8,5), 13)
    self.assertEqual(app.add(-1,-1),-2)
    self.assertEqual(app.add(100,5), 105)

  def test_types(self):
    user_id = '1'
    time_stamp = 123456
    latitude = 12367
    longitude = 13238
    speed = None or 3
    self.assertTrue(type(user_id)is str)
    self.assertTrue(type(time_stamp)is int)
    self.assertTrue(type(latitude)is int)
    self.assertTrue(type(longitude)is int)
    self.assertTrue(type(speed)is int or None)

  def test_boolean(self):
    testValue = True
    message = "Test Value is True"
    self.assertTrue(testValue,message)

if __name__ == '__main__':
  unittest.main()
