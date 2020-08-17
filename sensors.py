import random


class Sensors:
    def __init__(self):
        pass

    def results(self):
        return {"temperature_mash": random.randint(60, 100),
                "temperature_steam": random.randint(60, 100),
                "mass_obtained": random.randint(5, 300),
                "heating_power": random.randint(500, 1000)}
