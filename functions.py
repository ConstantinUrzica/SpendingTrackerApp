import json
import datetime
from constants import *


def load_data(file_name):
    with open(file_name, 'r+') as file:
        return json.load(file)


def get_user_data():
    print("Please enter the amount: ")
    amount = input()
    print("Please enter the appropriate tag [FOOD, BILLS, ENTERTAINMENT, EXTRA, ...]")
    tag = input()
    current_date = str(datetime.datetime.now()).split(' ')[0]
    return amount, tag, current_date


def add_new_entry(data, amount, tag, current_date, new_current_index):
    with open(DATABASE, 'r+') as file:
        # Form the object and append it
        current_spending_entry = {
            "amount": amount,
            "tag": tag,
            "date": current_date
        }
        data["entries"][new_current_index] = current_spending_entry
        data["lastIndex"] = new_current_index
        file.seek(0)
        json.dump(data, file)
