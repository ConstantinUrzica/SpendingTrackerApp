from src.functions import *
from src.constants import *

if __name__ == '__main__':
    # Load the data
    data = load_data(DATABASE)

    # Get user input
    amount, tag, current_date = get_user_data()

    # Retrieve last index and increment it
    new_current_index = str(int(data['lastIndex']) + 1)

    # Update database
    add_new_entry(data, amount, tag, current_date, new_current_index)
