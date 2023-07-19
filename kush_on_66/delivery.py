```python
from .database import Database
from .order import Order

class Delivery:
    def __init__(self, db_params):
        self.db = Database(db_params)

    def schedule_delivery(self, order_id, user_id, delivery_address, delivery_time):
        order = Order(self.db)
        order_info = order.get_order(order_id, user_id)

        if order_info['order_status'] != 'Ready for delivery':
            return 'Order is not ready for delivery.'

        delivery_data = {
            'order_id': order_id,
            'user_id': user_id,
            'delivery_address': delivery_address,
            'delivery_time': delivery_time,
            'delivery_status': 'Scheduled'
        }

        self.db.insert('deliveries', delivery_data)
        return 'Delivery has been scheduled.'

    def update_delivery_status(self, order_id, user_id, new_status):
        delivery_info = self.db.select('deliveries', {'order_id': order_id, 'user_id': user_id})

        if not delivery_info:
            return 'No delivery found for this order.'

        self.db.update('deliveries', {'delivery_status': new_status}, {'order_id': order_id, 'user_id': user_id})
        return 'Delivery status has been updated.'

    def get_delivery_info(self, order_id, user_id):
        delivery_info = self.db.select('deliveries', {'order_id': order_id, 'user_id': user_id})

        if not delivery_info:
            return 'No delivery found for this order.'

        return delivery_info
```