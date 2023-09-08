class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model 

  def move(self):
    print("drive!")
class Boat:
   def __init__(self, brand, model):
     self.brand = brand 
     self.model= model 
   def move(self):
     print("sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model 

  def move(self):
    print("Fly!")

car1 = Car("ford", "mustang")
boat1 = Boat("ibizat", "touring 20")
plane1 = Plane("boeing", "747")

for x in(car1, boat1, plane1):
  x.move()