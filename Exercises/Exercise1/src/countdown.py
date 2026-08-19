
from datetime import datetime

# samla events i en dict
events = {
    "summer_break": datetime(2026, 6, 9, 15, 0),
    "lia_start": datetime(2026, 9, 25, 8, 0),
    "christmas": datetime(2026, 12, 24),
    "bellas_birthday": datetime(2026, 12, 7),
    "new_year": datetime(2027, 1, 1),
    "graduation_party": datetime(2027, 6, 9, 16, 30)
}

# get date now

now = datetime.now()

with open("logs/countdown.log", "w") as file:
    for event, date in events.items():
        time_left = date - now
        file.write(f"{event}: {time_left}\n")