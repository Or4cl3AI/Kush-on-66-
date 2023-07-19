```python
# settings.py

# Database settings
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'kush_on_66',
    'user': 'root',
    'password': 'password'
}

# Email settings
CONTACT_EMAIL = '[email protected]'

# App settings
APP_NAME = 'Kush on 66'
APP_STORE_URL = 'https://www.apple.com/app-store/'
GOOGLE_PLAY_URL = 'https://play.google.com/store'

# Product categories
PRODUCT_CATEGORIES = ['flowers', 'concentrates', 'edibles', 'others']

# DOM Element IDs
DOM_IDS = {
    'product_list': 'product-list',
    'product_detail': 'product-detail',
    'review_list': 'review-list',
    'chat_window': 'chat-window',
    'order_form': 'order-form',
    'delivery_option': 'delivery-option',
    'pickup_option': 'pickup-option'
}

# Message names
MESSAGE_NAMES = {
    'product_browse': 'product-browse',
    'product_detail': 'product-detail',
    'review_read': 'review-read',
    'recommendation_get': 'recommendation-get',
    'chat_start': 'chat-start',
    'order_place': 'order-place',
    'delivery_schedule': 'delivery-schedule',
    'pickup_schedule': 'pickup-schedule'
}

# Function names
FUNCTION_NAMES = {
    'browse_products': 'browse_products',
    'read_reviews': 'read_reviews',
    'get_recommendations': 'get_recommendations',
    'start_chat': 'start_chat',
    'place_order': 'place_order',
    'schedule_delivery': 'schedule_delivery',
    'schedule_pickup': 'schedule_pickup'
}
```