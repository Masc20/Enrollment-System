from enum import Enum

# Admin roles
class AdminRole(str, Enum):
    ADMIN = "Admin"
    ENCODER = "Encoder"
    AUDITOR = "Auditor"
    SCHEDULER = "Scheduler"
