from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

for sensor in W1ThermSensor.get_available_sensors():
    print(sensor.id, "wybadał temperaturę: ", sensor.get_temperature())


class Sensors:
    def __init__(self):
        self.mass_obtained = 0

    def results(self):
        return {
            "temperature_mash": W1ThermSensor.get_available_sensors()["SENSOR_MASH_ID"].get_temperature(),
            "temperature_steam": W1ThermSensor.get_available_sensors()["SENSOR_STEAM_ID"].get_temperature(),
            "mass_obtained": "ODCZYT_MASY()",  # TODO: moduł odczytujący masę
            "heating_power": "ON/OFF",
            "liquid_reached_critical_level": False
        }
