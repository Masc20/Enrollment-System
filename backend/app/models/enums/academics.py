from enum import Enum
from datetime import datetime

# Year Level
class YearLevel(str, Enum):
    FIRST = "1st Year"
    SECOND = "2nd Year"
    THIRD = "3rd Year"
    FOURTH = "4th Year"

# Semester
class Semesters(str, Enum):
    FIRST_SEM = "1st Semester"
    SECOND_SEM = "2nd Semester"
    THIRD_SEM = "3rd Semester"
    FOURTH_SEM = "4th Semester"
