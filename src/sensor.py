from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    def __init__(self, id, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park
    
    def __str__(self):
        status = "ON" if self.is_active else "OFF"
        return f"{self.id}: {status}"
  
    @abstractmethod
    def update_car_park(self, plate):
        pass
  
    def _scan_plate(self):
        """
        Scan the plate
        """
        return 'FAKE-' + format(random.randint(0, 999), "03d")
  
    def detect_vehicle(self):
        """
        Detect vehicle
        """
        plate = self._scan_plate()
        self.update_car_park(plate)
    
class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        if plate:
            self.car_park.remove_car(plate)
            print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
        else:
            print("No cars available to exit")
    
    def _scan_plate(self):
        if self.car_park and self.car_park.plates:
            return random.choice(self.car_park.plates)
        else:
            return None