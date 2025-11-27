from src.sensor import Sensor
from src.display import Display
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    def __init__(self, location, capacity, plates=None,displays=None, sensors=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
        
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)
    
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
        self._log_car_activity(plate, "entered")
  
    def remove_car(self, plate):
        """
        Remove the plate number and update the displays.
        """
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
            self._log_car_activity(plate, "exited")
        else:
            # print(f"Plate {plate} not found in car park.")
            raise ValueError(f"Plate {plate} not found")
      
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
            
    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            
    def write_config(self):
        with open("config.json", "w") as f:
            json.dump({"location": self.location,
                        "capacity": self.capacity,
                        "log_file": str(self.log_file)}, f)
            
    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])