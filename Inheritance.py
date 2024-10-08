# Lớp cha Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Lớp con Dog kế thừa từ lớp Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Lớp con Cat kế thừa từ lớp Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Khởi tạo đối tượng lớp con
dog = Dog("Dog")
cat = Cat("Cat")

print(dog.speak())  # Output: Dog barks
print(cat.speak())  # Output: Cat meows
