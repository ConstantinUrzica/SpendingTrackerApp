# This is a sample Python script.
import datetime
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json

if __name__ == '__main__':

    # TODO: create a function for reading the database.

    # Load the database
    with open('database.json', 'r+') as file:
        data = json.load(file)
        # Read input from client
        print("Please enter the amount: ")
        amount = input()
        print("Please enter the appropriate tag [FOOD, BILLS, ENTERTAINMENT, EXTRA, ...]")
        tag = input()
        currentDate = str(datetime.datetime.now()).split(' ')[0]

        # retrieve last index and increment it
        newCurrentIndex = str(int(data['lastIndex']) + 1)

        # Form the object and append it
        currentSpendingEntry = {
            "amount": amount,
            "tag": tag,
            "date": currentDate
        }
        print("DEBUG:", currentSpendingEntry)
        data["entries"][newCurrentIndex] = currentSpendingEntry
        data["lastIndex"] = newCurrentIndex
        file.seek(0)
        json.dump(data, file)





