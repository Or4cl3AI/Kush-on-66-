```python
from .database import Database
from .order import Order

class Pickup:
    def __init__(self):
        self.db = Database()

    def schedule_pickup(self, order_id, user_id, pickup_time):
        order = self.db.get_order(order_id, user_id)
        if order and order.order_type == 'pickup':
            order.pickup_time = pickup_time
            self.db.update_order(order)
            return True
        return False

    def get_pickup_status(self, order_id, user_id):
        order = self.db.get_order(order_id, user_id)
        if order and order.order_type == 'pickup':
            return order.pickup_time
        return None

    def cancel_pickup(self, order_id, user_id):
        order = self.db.get_order(order_id, user_id)
        if order and order.order_type == 'pickup':
            order.pickup_time = None
            self.db.update_order(order)
            return True
        return False
```