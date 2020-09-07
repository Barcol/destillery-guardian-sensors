import RPi.GPIO as GPIO


class HardwareController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        output_channel_list = [17, 27]
        GPIO.setup(output_channel_list, GPIO.OUT)

    def start_water_cooling(self):
        print("Chłodzenie ON")
        GPIO.output(17, 1)

    def stop_water_cooling(self):
        print("Chłodzenie OFF")
        GPIO.output(17, 0)

    def start_heating(self):
        print("Grzałka ON")
        GPIO.output(27, 1)

    def stop_heating(self):
        print("Grzałka OFF")
        GPIO.output(27, 0)
