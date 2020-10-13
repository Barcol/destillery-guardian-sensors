from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO

sensor = W1ThermSensor()


class Sensors:
    def __init__(self):
        for sensor in W1ThermSensor.get_available_sensors():
            print(sensor.id, "wybadał temperaturę: ", sensor.get_temperature())

    def results(self):
        return {
            "temperature_mash": [sensor for sensor in W1ThermSensor.get_available_sensors() if sensor.id == "0004734d57ff"][0].get_temperature(),
            "temperature_steam": [sensor for sensor in W1ThermSensor.get_available_sensors() if sensor.id == "0004734dcdff"][0].get_temperature(),
            "mass_obtained": 200,  # TODO: moduł odczytujący masę
            "heating_power": GPIO.input(27),
            "liquid_reached_critical_level": False
        }
