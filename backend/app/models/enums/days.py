from enum import Enum

# Week Days/Ends
class Week(str, Enum):
    # Week Days
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"

    # Week Ends
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"