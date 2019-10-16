DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def determine_next_day(days_ago=0, days_before=0, was_day=0):
    index = 0
    tomorrow = 0
    total_days = days_ago + days_before + was_day
    max_index = len(DAYS) - 1 # As there are only 7 days max_index can be from 0 to 6

    """
    If the total number of days exceeds max possible days of week then
    loop around to the beggining of the week.
    """
    if (total_days > max_index):
        # Subtract 1 in order to give the valid array offset not just number of days.
        index = (total_days % max_index) - 1
    else:
        index = total_days

    if (index is max_index):
        # If current day is Sunday, the next day has to be Monday, i.e. index 0
        tomorrow = 0
    else:
        tomorrow = index + 1
        
    print(str(days_ago) + " days ago and " + str(days_before) + " days before that, was " + DAYS[was_day] + ".")
    print("Today is " + DAYS[index] + ".")
    print("Tomorrow is " + DAYS[tomorrow] + ".")


determine_next_day(days_ago=4, days_before=5, was_day=2)