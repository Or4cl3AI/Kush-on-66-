```python
from database import Database
from user import User
from product import Product

class Order:
    def __init__(self, user_id, product_id, order_quantity, order_type):
        self.order_id = None
        self.user_id = user_id
        self.product_id = product_id
        self.order_quantity = order_quantity
        self.order_status = "Pending"
        self.order_type = order_type

    def place_order(self):
        db = Database()
        user = User.get_user(self.user_id)
        product = Product.get_product(self.product_id)

        if user and product:
            self.order_id = db.insert_order(self.user_id, self.product_id, self.order_quantity, self.order_status, self.order_type)
            return self.order_id
        else:
            return None

    @staticmethod
    def get_order(order_id):
        db = Database()
        order_data = db.get_order(order_id)
        if order_data:
            return Order(order_data['user_id'], order_data['product_id'], order_data['order_quantity'], order_data['order_type'])
        else:
            return None

    def update_order_status(self, new_status):
        db = Database()
        self.order_status = new_status
        db.update_order_status(self.order_id, new_status)
```
