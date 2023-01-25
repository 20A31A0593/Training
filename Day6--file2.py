class Animal:
    def eat(self):
        pass
    def sound(self):
        print("Sound")
class Dog(Animal):
    def sound(self):
        print("barks")
        pass
class cat(Animal):
    def sound(self):
        print("Meow")
        pass
d=Dog()
c=cat()
d.sound()
c.sound()
