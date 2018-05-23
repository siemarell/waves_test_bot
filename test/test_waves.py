import unittest
from waves import waves


class TestWaves(unittest.TestCase):

    def test_validate_valid_address(self):
        self.assertTrue(waves.validate_address('3N3Cn2pYtqzj7N9pviSesNe8KG9Cmb718Y1'))

    def test_validate_invalid_address(self):
        self.assertFalse(waves.validate_address('3N3Cn2aYtqzj7N9pviSesNe8KG9Cmb718Y1'))

if __name__ == '__main__':
    unittest.main()