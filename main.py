import asyncio
import json

import requests

from sensors import Sensors

sensors = Sensors()


def send_results(session_id, results):
    requests.post(f"http://127.0.0.1:8000/sessions/{session_id}/results",
                  data=json.dumps(results))


def handle_results(results):
    if results["temperature_mash"] > 82:
        stop_heating()
    if results["mass_remaining"] < 100:
        stop_heating()
    if results["liquid_reached_critical_level"]:
        stop_heating()


async def main():
    r = requests.get("http://127.0.0.1:8000/sessions/")
    for session in r.json():
        if not session["is_finished"]:
            print(session)
            while not session["is_finished"]:
                await asyncio.sleep(session["time_interval"])
                send_results(session['id'], sensors.results())


asyncio.run(main())
