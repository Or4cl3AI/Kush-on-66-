```python
import random
from kush_on_66.database import Database
from kush_on_66.product import Product

class Recommendation:
    def __init__(self, user):
        self.user = user
        self.db = Database()

    def get_recommendations(self):
        user_preferences = self.user.preferences
        all_products = self.db.get_all_products()
        recommended_products = []

        for product in all_products:
            if product.product_type in user_preferences:
                recommended_products.append(product)

        if len(recommended_products) > 5:
            recommended_products = random.sample(recommended_products, 5)

        return recommended_products

    def display_recommendations(self):
        recommended_products = self.get_recommendations()
        for product in recommended_products:
            print(f"Product Name: {product.product_name}")
            print(f"Product Type: {product.product_type}")
            print(f"Product Description: {product.product_description}")
            print(f"Product Price: {product.product_price}")
            print("\n")
```