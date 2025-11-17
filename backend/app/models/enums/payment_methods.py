from enum import Enum


# Payment Method
class PaymentMethod(str, Enum):
    CASH = "Cash"
    CARD = "Card"
    ONLINE = "Online"