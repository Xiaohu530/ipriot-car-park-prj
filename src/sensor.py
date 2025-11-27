class Sensor:
  def __init__(self, id, is_active=False, car_park=None):
    self.id = id
    self.is_active = is_active
    self.car_park = car_park
    
  def __str__(self):
    status = "ON" if self.is_active else "OFF"
    return f"{self.id}: {status}"
  
class EntrySensor(Sensor):
  pass

class ExitSensor(Sensor):
  pass