```python
from database import Database
from product import Product

class Review:
    def __init__(self, review_id, user_id, product_id, review_text, review_rating):
        self.review_id = review_id
        self.user_id = user_id
        self.product_id = product_id
        self.review_text = review_text
        self.review_rating = review_rating

    @staticmethod
    def get_reviews(product_id):
        db = Database()
        reviews = db.query("SELECT * FROM reviews WHERE product_id = ?", (product_id,))
        return [Review(*review) for review in reviews]

    def save(self):
        db = Database()
        db.execute("INSERT INTO reviews (user_id, product_id, review_text, review_rating) VALUES (?, ?, ?, ?)",
                   (self.user_id, self.product_id, self.review_text, self.review_rating))

    def update(self):
        db = Database()
        db.execute("UPDATE reviews SET review_text = ?, review_rating = ? WHERE review_id = ?",
                   (self.review_text, self.review_rating, self.review_id))

    def delete(self):
        db = Database()
        db.execute("DELETE FROM reviews WHERE review_id = ?", (self.review_id,))
```