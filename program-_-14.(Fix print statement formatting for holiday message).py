week_days = ['mon','tue','wed','thu','fri','sat','sun']

for work in week_days:
    if work in ['sat','sun','mon','tue','wed']:
        print(f"working day is: {work}")
    elif work == 'thu':
        print(f"half work day is: {work}")
    else:
        print(f"holiday day is: {work}")
