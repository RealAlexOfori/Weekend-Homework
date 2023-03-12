import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Jack")

    def test_guest_has_name(self):
        self.assertEqual("Jack", self.guest.name)

if __name__ == '__main__':
    unittest.main() 