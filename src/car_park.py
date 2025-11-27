from sensor import Sensor
from display import Display
from datetime import datetime

class CarPark:
    def __init__(self, location, capacity, plates=None,displays=None, sensors=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
    
    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."
  
    def register(self, component):
        """
        Register sensors and displays.
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
      
  
    def add_car(self, plate):
        """
        Record the plate and update the displays.
        """
        self.plates.append(plate)
        self.update_displays()
  
    def remove_car(self, plate):
        """
        Remove the plate number and update the displays.
        """
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
        else:
            print(f"Plate {plate} not found in car park.")
      
    @property
    def available_bays(self):
        """
        Calculate avaiable bays.
        If more cars than capacity, return 0 instead of negative number.
        """
        return max(self.capacity - len(self.plates), 0)
  
    def update_displays(self):
        """
        Update the displays.
        """
        data = {
            "available_bays": self.available_bays, "temperature": 25,
            "time": datetime.now().strftime("%H:%M:%S")
        }
        
        for display in self.displays:
            display.update(data)