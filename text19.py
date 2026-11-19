from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self):
        return 2025 - self.joining_year

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.name} is a {self.get_role()} and has been using the platform for {self.years_on_platform()} years."


class Customer(User):
    def get_role(self):
        return "Customer"


class Vendor(User):
    def get_role(self):
        return "Vendor"


customer = Customer("Ganga", 2022)
vendor = Vendor("Anu", 2020)

print(customer)
print(vendor)