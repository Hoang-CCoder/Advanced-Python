# Tạo lớp với phương thức khởi tạo __init__
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    # Phương thức cho đối tượng thực hiện hành động
    def speak(self):
        return f"{self.name} says {self.sound}"

# Khởi tạo đối tượng từ lớp
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

print(dog.speak())  # Output: Dog says Woof
print(cat.speak())  # Output: Cat says Meow
