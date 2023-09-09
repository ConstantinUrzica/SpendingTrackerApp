import json
import datetime
import traceback
import csv
from constants import *


def load_data(file_name):
    try:
        with open(file_name, 'r+') as file:
            data = json.load(file)
            return data
    except Exception as ex:
        print(traceback.format_exc())


def get_user_data():
    print("Please enter the amount: ")
    amount = input()
    print("Please enter the appropriate tag [FOOD, BILLS, ENTERTAINMENT, EXTRA, ...]")
    tag = input()
    current_date = str(datetime.datetime.now()).split(' ')[0]
    return amount, tag, current_date


def add_new_entry(data, amount, tag, current_date, new_current_index):
    current_spending_entry = {
        "amount": amount,
        "tag": tag,
        "date": current_date
    }
    data["entries"][new_current_index] = current_spending_entry
    data["lastIndex"] = new_current_index
    data["balance"] = float(data["balance"]) - float(amount)
    return data


def commit_updates(data):
    try:
        with open(DATABASE, 'r+') as file:
            file.seek(0)
            json.dump(data, file)
    except Exception as ex:
        print(traceback.format_exc())


def get_next_index(previous_index):
    return str(int(previous_index) + 1)


def export_to_csv(data, out_path):
    try:
        with open(out_path, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, data['entries']['1'].keys())
            writer.writeheader()
            writer.writerows(data['entries'].values())
    except Exception as ex:
        print(traceback.format_exc())
