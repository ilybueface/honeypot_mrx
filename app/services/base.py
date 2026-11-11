from app.core.connection import Attempt, Connection
from datetime import datetime


class UniterService:
    def __init__(self):
        pass

    def process_auth_request(self, connection, login, password):
        attempt = Attempt(
            time_of_attempt=datetime.now(), username=login, password=password
        )
        connection.add_attempt(attempt)
