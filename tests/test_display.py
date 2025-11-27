import unittest
from src.display import Display
from src.car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.id = 1
        self.message = "Welcome to the car park"
        self.is_on = True
        self.car_park = CarPark("123 Example Street", 100)
        self.display = Display(self.id, self.message, self.is_on)
        
    # Test object initialization
    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        
    # Test message update
    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")