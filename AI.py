import time
import schedule
import platform
import ctypes
import pyttsx3
from pynotifier import Notification

class AI:
    def __init__(self, name):
        self.name = name

    def remind_medicine(self):
        message = "약 드실 시간입니다."
        print(f"{self.name}: {message}")

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  
        engine.setProperty('volume', 1.0)  
        engine.say(message)
        engine.runAndWait()


def main():
    ai = AI("어시스턴트")

    schedule.every().day.at("09:00").do(ai.remind_medicine)
    schedule.every().day.at("17:12").do(ai.remind_medicine)
    schedule.every().day.at("19:00").do(ai.remind_medicine)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
