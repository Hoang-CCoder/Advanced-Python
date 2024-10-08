class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Tạo các đối tượng Singleton
s1 = Singleton()
s2 = Singleton()

# Kiểm tra cả hai đối tượng đều là cùng một thể hiện
print(s1 is s2)  # Output: True
