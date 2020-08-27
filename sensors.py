import random


class Sensors:
    def __init__(self):
        self.mass_obtained = 0

    def results(self):
        self.mass_obtained += random.randint(5, 50)
        return {
            "temperature_mash": random.randint(60, 100),
            "temperature_steam": random.randint(70, 82),
            "mass_obtained": self.mass_obtained,
            "heating_power": random.randint(500, 1000),
            "liquid_reached_critical_level": False
        }
