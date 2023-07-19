```python
from .database import DatabaseConnection

class Product:
    def __init__(self, product_id, product_name, product_type, product_description, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_type = product_type
        self.product_description = product_description
        self.product_price = product_price

    @classmethod
    def get_all_products(cls):
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return [cls(*product) for product in products]

    @classmethod
    def get_product_by_id(cls, product_id):
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
            product = cursor.fetchone()
            return cls(*product) if product else None

    def save(self):
        with DatabaseConnection() as cursor:
            cursor.execute(
                "INSERT INTO products (product_id, product_name, product_type, product_description, product_price) VALUES (%s, %s, %s, %s, %s)",
                (self.product_id, self.product_name, self.product_type, self.product_description, self.product_price)
            )

    def update(self):
        with DatabaseConnection() as cursor:
            cursor.execute(
                "UPDATE products SET product_name = %s, product_type = %s, product_description = %s, product_price = %s WHERE product_id = %s",
                (self.product_name, self.product_type, self.product_description, self.product_price, self.product_id)
            )

    def delete(self):
        with DatabaseConnection() as cursor:
            cursor.execute("DELETE FROM products WHERE product_id = %s", (self.product_id,))
```