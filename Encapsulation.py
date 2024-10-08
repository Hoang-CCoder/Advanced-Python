class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Thuộc tính private

    # Phương thức để xem số dư
    def get_balance(self):
        return self.__balance

    # Phương thức để gửi tiền vào tài khoản
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

# Khởi tạo tài khoản ngân hàng
account = BankAccount("John", 1000)
print(account.get_balance())  # Output: 1000

account.deposit(500)
print(account.get_balance())  # Output: 1500
