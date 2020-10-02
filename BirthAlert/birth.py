#!/usr/bin/env python3

import datetime
import time
import os

date = datetime.date.today().strftime("%d/%m")

# List of birthday
listBirthday = {
        "test":"28/09", "test2": "29/09",
        "Chloé":"01/10", "Diane":"05/02", "Maman":"25/09",
        "Papa":"18/12"
        }

def checkBirthdate():
    isBirth = 0
    for person, birthdate in listBirthday.items():
        if date in birthdate:
            isBirth = 1
            os.system('notify-send "Birthday : ' + person + ' ' + birthdate + '"')
    if isBirth == 0:
        os.system('notify-send "No birthday today !" ')

if __name__ == "__main__":
    time.sleep(300)
    checkBirthdate()
