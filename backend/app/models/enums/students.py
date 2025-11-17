from enum import Enum

# Admission Status
class AdmissionStatus(str, Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    DENIED = "Denied"

# Enrollment Status
class EnrollmentStatus(str, Enum):
    REGULAR = "Regular"
    IRREGULAR = "Irregular"

# Student Type
class StudentType(str, Enum):
    OLD = "Old"
    NEW = "New"
    TRANSFEREE = "Transferee"