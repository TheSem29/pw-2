class Car:
    def __init__(self, license_plate, year, horsepower):
        self.license_plate = license_plate
        self.year = year
        self.horsepower = horsepower

    def get_age(self):
        return 2025 - self.year

    def _get_power_coeff(self):
        if self.horsepower <= 70:
            return 0.8
        elif 71 <= self.horsepower <= 100:
            return 1.0
        elif 101 <= self.horsepower <= 150:
            return 1.2
        else:
            return 1.5

    def _get_age_coeff(self):
        age = self.get_age()
        if age <= 3:
            return 0.9
        elif 4 <= age <= 7:
            return 1.0
        elif 8 <= age <= 10:
            return 1.1
        else:
            return 1.3

    def calculate_premium(self, base_tariff=4000):
        km = self._get_power_coeff()
        kva = self._get_age_coeff()
        return base_tariff * km * kva



car = Car("A123BC77", 2018, 110)

print(f"Стоимость полиса: {car.calculate_premium():.2f} руб.")
