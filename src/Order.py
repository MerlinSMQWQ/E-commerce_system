from datetime import datetime
from enum import Enum
from User import User
from Product import Product

class Order:
    def __init__(self, order_id: str, user: User, product: Product, quantity: int):
        self.order_id = order_id
        self.user = user
        self.product = product
        self.quantity = quantity
        self.created_time = datetime.now()
        self.status = OrderStatus.UNPAID

        self.product.stock -= self.quantity


class OrderStatus(Enum):
    UNPAID = 1
    PAID = 2
    CANCELLED = 3