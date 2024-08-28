from abc import ABC, abstractmethod

class ICinemaCalculation(ABC):
    @abstractmethod
    def calculate_admin_fee(self):
        pass

class RegularCinema(ICinemaCalculation):
    def __init__(self, price):
        self.price = price

    def calculate_admin_fee(self):
        # Setiap tipe bioskop menghitung biaya admin sendiri tanpa memodifikasi class lain
        return (self.price * 10) / 100

class DeluxeCinema(ICinemaCalculation):
    def __init__(self, price):
        self.price = price

    def calculate_admin_fee(self):
        return (self.price * 12) / 100

# Contoh penggunaan
regular_cinema = RegularCinema(price=100)
deluxe_cinema = DeluxeCinema(price=150)

print(f"Admin fee untuk RegularCinema: {regular_cinema.calculate_admin_fee()}")
print(f"Admin fee untuk DeluxeCinema: {deluxe_cinema.calculate_admin_fee()}")
