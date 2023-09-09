from src.functions import *
from src.constants import *

if __name__ == '__main__':
    # Load the data
    data = load_data(DATABASE)
    print("DEBUG: data=", data)

    # Get user input
    amount, tag, current_date = get_user_data()

    # Retrieve last index and increment it
    new_current_index = get_next_index(data['lastIndex'])

    # Update data
    data = add_new_entry(data, amount, tag, current_date, new_current_index)

    # Commit updates to database
    commit_updates(data)

    # Export to CSV
    # export_to_csv(data, CSVFILE)
