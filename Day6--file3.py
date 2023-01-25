from abc import ABC, abstractmethod
class Product(ABC):
    @abstractmethod
    def cost_price(self):
         print(" product")

class laptop(Product):
    def selling_price(self):
        pass
    def cost_price(self):
        print("For laptop")
ob=laptop()
ob.cost_price()
 
