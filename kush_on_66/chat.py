```python
import datetime
from database import DatabaseConnection

class Chat:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = DatabaseConnection()

    def start_chat(self):
        chat_id = self.db.insert('chats', {'user_id': self.user_id, 'start_time': datetime.datetime.now()})
        return chat_id

    def send_message(self, chat_id, message):
        self.db.insert('messages', {'chat_id': chat_id, 'user_id': self.user_id, 'message': message, 'time': datetime.datetime.now()})

    def get_messages(self, chat_id):
        messages = self.db.select('messages', {'chat_id': chat_id})
        return messages

    def end_chat(self, chat_id):
        self.db.update('chats', {'end_time': datetime.datetime.now()}, {'id': chat_id})
```