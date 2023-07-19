```python
import sys
from kush_on_66 import user, product, review, recommendation, chat, order, delivery, pickup, database, utils, settings

def main():
    # Initialize the database
    db = database.init_db(settings.DATABASE_URI)

    # Create a user session
    user_session = user.UserSession(db)

    # Main app loop
    while True:
        print("Welcome to Kush on 66 app!")
        print("1. Browse Products")
        print("2. Read Reviews")
        print("3. Get Recommendations")
        print("4. Chat with Budtender")
        print("5. Place an Order")
        print("6. Schedule Delivery")
        print("7. Schedule Pickup")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product.browse_products(db)
        elif choice == '2':
            review.read_reviews(db)
        elif choice == '3':
            recommendation.get_recommendations(db, user_session)
        elif choice == '4':
            chat.start_chat(db, user_session)
        elif choice == '5':
            order.place_order(db, user_session)
        elif choice == '6':
            delivery.schedule_delivery(db, user_session)
        elif choice == '7':
            pickup.schedule_pickup(db, user_session)
        elif choice == '8':
            print("Thank you for using Kush on 66 app. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```