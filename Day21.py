# Abstraction
# - Abstraction is nothing but Hiding the Important details and showing only the necessary details
# - By using Abstraction we can hide Important details or buisness logic


# abc -> Abstract Base Class
# - Allows us to create abstract base class

# ABC -> Base class
# - It is a Base class for making other classes abstract.
# - When we Inherit from ABC , our class becomes abstract class


from abc import ABC, abstractmethod

# parent class
class Car(ABC):

    def details(self,_brand,color,price):
        self._brand=_brand
        self.color=color
        self.price=price

        print(f"Brand = {self._brand} , Color = {self.color} and Price ={self.price}")


    @abstractmethod
    def start(self):
        print("Car Start.....logical part")

# child class
class tesla(Car):
    def carDetails(self,_brand,color,price):
        self.details(_brand,color,price)
    
    # must be overriden absract method in child class
    def start(self):
        print("tesla is car started....")
    
tesla1=tesla()
tesla1.start()
tesla1.carDetails("Tesla","White","$92,223")

# cant create instance of a abstract class