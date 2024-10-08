# Lớp cha Animal và các lớp con với đa hình phương thức speak
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Hàm đa hình có thể nhận mọi đối tượng là động vật
def animal_sound(animal):
    print(animal.speak())

# Sử dụng đa hình
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof
animal_sound(cat)  # Output: Meow
