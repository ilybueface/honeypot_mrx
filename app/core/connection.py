class Attempt:
    def __init__(self, username, password, time_of_attempt):
        self.username = username
        self.password = password
        self.time_of_attempt = time_of_attempt

    def __repr__(self):
        return f"Attempt(user='{self.username}', pass='{self.password}', time='{self.time_of_attempt}')"


class Connection:
    def __init__(
        self,
        id,
        start_time,
        lure_name,
        lure_type,
        address_of_attacker,
        port_of_attacker,
    ):
        self.id = id
        self.start_time = start_time
        self.lure_name = lure_name
        self.lure_type = lure_type
        self.address_of_attacker = address_of_attacker
        self.port_of_attacker = port_of_attacker
        self.attempts = []

    def add_attempt(self, attempt: Attempt):
        self.attempts.append(attempt)

    def get_attempt_count(self):
        return len(self.attempts)
