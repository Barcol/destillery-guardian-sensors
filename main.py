import json
from time import sleep

import requests
from sensors import Sensors
from hardware_controller import HardwareController

hardware_controller = HardwareController()
sensors = Sensors()


def cool_hardware_down():
    print("Trwa kończenie pracy systemu.")
    hardware_controller.stop_heating()
    print("Trwa wychładzanie par. Potrwa minutę.")
    sleep(60)
    hardware_controller.stop_water_cooling()
    print("Trwa zamykanie przeływu w chłodnicy. Potrwa 15 sekund.")
    sleep(15)
    hardware_controller.cleanup_pins()
    print("Zakończono pracę systemu")


def send_results(session_id, results):
    requests.post(f"http://127.0.0.1:8000/sessions/{session_id}/results",
                  data=json.dumps(results))


def stop_session(session_id, message):
    cool_hardware_down()
    requests.put(f"http://127.0.0.1:8000/sessions/{session_id}/finish",
                 data=json.dumps({"termination_reason": message}))


def handle_results(session_id, results):
    print(results)
    send_results(session_id, results)
    if results["temperature_steam"] > 82:
        print("Temperatura par: ", results["temperature_steam"])
        stop_session(session_id, "Zakończona z powodu przekroczenia temperatury")
    if results["mass_obtained"] > 500:
        print("Masa uzysku: ", results["mass_obtained"])
        stop_session(session_id, "Zakończona z powodu nadmiaru odebranego uzysku")
    if results["liquid_reached_critical_level"]:
        print("Przekroczono krytyczny poziom cieczy.")
        stop_session(session_id, "Zakończona z powodu przekroczenia wysokości cieszy")


def handle_session(session):
    print("Znaleziono trwającą sesję: ", session["name"])
    hardware_controller.start_water_cooling()
    hardware_controller.start_heating()

    while not session["is_finished"]:
        sleep(session["time_interval"])
        handle_results(session['id'], sensors.results())
        session = requests.get(f"http://127.0.0.1:8000/sessions/{session['id']}").json()


def main():
    try:
        while True:
            print("Szukam aktywnej sesji.")
            r = requests.get("http://127.0.0.1:8000/sessions/")
            for session in r.json():
                if not session["is_finished"]:
                    handle_session(session)
            sleep(5)
    except KeyboardInterrupt:
        print("Ręczne zatrzymanie.")
        cool_hardware_down()


if __name__ == "__main__":
    main()
