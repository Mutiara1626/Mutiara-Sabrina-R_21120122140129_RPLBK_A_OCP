class Cinema:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

class RegularCinema(Cinema):
    pass

class DeluxeCinema(Cinema):
    pass

class CalculatePriceCinemaService:
    def calculate_admin_fee(self, cinema):
        # Setiap kali menambahkan tipe bioskop baru, harus mengubah kode dengan cara menambahkan kondisi baru di if-elif statement.
        if isinstance(cinema, RegularCinema):
            return (cinema.price * 10) / 100
        elif isinstance(cinema, DeluxeCinema):
            return (cinema.price * 12) / 100
        else:
            # Jika tipe bioskop baru ditambahkan, kita harus memodifikasi kode ini juga
            raise Exception('Cinema not found!')

        return 0

# Contoh penggunaan
regular_cinema = RegularCinema(price=100, quantity=1)
deluxe_cinema = DeluxeCinema(price=150, quantity=1)

calculator = CalculatePriceCinemaService()

print(f"Admin fee untuk RegularCinema: {calculator.calculate_admin_fee(regular_cinema)}")
print(f"Admin fee untuk DeluxeCinema: {calculator.calculate_admin_fee(deluxe_cinema)}")
