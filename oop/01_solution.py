class Car:
    total_car=0
    def __init__(self,model,brand):
      self.__model=model
      self.__brand=brand
      Car.total_car+=1

    def full_name(self):
      return f'{self.__brand} {self.__model}' 

    def get_brand(self):
       return self.__brand
    def fuel_type(self):
       return 'Petrol or Deisel'
    @staticmethod
    def general_static_method():
       return 'Car is a modern Technology with AI'

    @property
    def model(self):
       return self.__model
my_car=Car('toyota','corrola')
print(my_car.get_brand())

print(my_car.full_name())

class ElectricCar(Car):
   def __init__(self, model,brand,battery_Size):
      super().__init__(brand,model)
      self.battery_Size=battery_Size
   def fuel_type(self):
        return 'Electric Charge'

my_ecar=ElectricCar("Tesla","Model S","85kWH")
# print(my_ecar.battery_Size)
# print(my_ecar.full_name())
# print(my_car.get_brand())
# print(my_ecar.fuel_type())
# print(my_car.total_car)
# print(Car.general_static_method())
# print(my_car.general_static_method())
my_car._Car__model='city'
print(my_car.model)
print(isinstance(my_car,Car))
print(isinstance(my_ecar,ElectricCar))

class Engine:
   def engine_info(self):
      return 'engine of electric car'
class Battery:
   def Battery_info(self):
         return 'battery of electric car'
class Electric_Engine(Battery,Engine,Car):
   pass

multiple_Inheritance_check=Electric_Engine('tesla','t1')
print(multiple_Inheritance_check.Battery_info())