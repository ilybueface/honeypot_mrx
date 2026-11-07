from datetime import datetime


class Attempt:
    def __init__(self, username, password, time_of_attempt):
        self.username = username
        self.password = password
        self.time_of_attempt = time_of_attempt

    def __repr__(self):
        return f"Attempt(user='{self.username}', pass='{self.password}', time='{self.time_of_attempt}')"


class Connection:
    MAX_FAILED_ATTEMPTS: int = 3

    def __init__(
        self,
        id,
        start_time,
        lure_name,
        lure_type,
        address_of_attacker,
        port_of_attacker,
        max_failed_attempts: int = MAX_FAILED_ATTEMPTS,
    ):
        self.id = id
        self.start_time = start_time
        self.lure_name = lure_name
        self.lure_type = lure_type
        self.address_of_attacker = address_of_attacker
        self.port_of_attacker = port_of_attacker
        self.max_failed_attempts = max_failed_attempts
        self.attempts = []
        self.is_active = True
        self.end_time = None

    def add_attempt(self, attempt: Attempt):
        if not self.is_active:
            print(f"Conn {self.id}. Connection terminated")
            return
        self.attempts.append(attempt)
        if self.get_attempt_count() >= self.max_failed_attempts:
            self.disconnect()

    def get_attempt_count(self):
        return len(self.attempts)

    def disconnect(self):
        if self.is_active:
            self.is_active = False
            self.end_time = datetime.now()
            print(
                f"Conn {self.id} Connection to {self.address_of_attacker} terminated after {self.get_attempt_count()} attempts."
            )
