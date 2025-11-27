import unittest
from src.car_park import CarPark
from src.sensor import EntrySensor, ExitSensor

class TestSensors(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Street", 100)
        self.entry = EntrySensor("E1", car_park=self.car_park)
        self.exit = ExitSensor("X1", car_park=self.car_park)
        
    # Test entry car
    def test_entry_sensor_detect_vehicle_adds_car(self):
        initial_bays = self.car_park.available_bays
        self.entry.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, initial_bays - 1)
        
    # Test exit car
    def test_exit_sensor_detect_vehicle_removes_car(self):
        # Add a car first so exit has something to remove
        self.car_park.add_car("TEST-123")
        initial_bays = self.car_park.available_bays
        
        self.exit.detect_vehicle()

        self.assertEqual(self.car_park.available_bays, initial_bays + 1)
        
if __name__ == "__main__":
    unittest.main()