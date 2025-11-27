from sensor import Sensor
from display import Display

class CarPark:
  def __init__(self, location, capacity, plates=None, displays=None, sensors=None):
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
    
    :param component: A generic placeholder either a Sensor or a Display.
    """
    if not isinstance(component, (Sensor, Display)):
      raise TypeError("Object must be a Sensor or Display")
    
    if isinstance(component, Sensor):
      self.sensors.append(component)
    elif isinstance(component, Display):
      self.displays.append(component)
      
  
  def add_car(self):
    """
    Record the plate and update the displays.
    
    :param self: Description
    """
    pass
  
  def remove_car(self):
    """
    Remove the plate number and update the displays.
    
    :param self: Description
    """
    pass
  
  def update_displays():
    """
    Update the displays.
    """
    pass