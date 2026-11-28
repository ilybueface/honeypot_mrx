from datetime import datetime, timezone
import uuid


class Attempt:
    def __init__(self, username: str, password: str, time_of_attempt: datetime) -> None:
        self.username = username
        self.password = password
        self.time_of_attempt = time_of_attempt

    def __repr__(self) -> str:
        return f"Attempt(user='{self.username}', pass='{self.password}', time='{self.time_of_attempt}')"


class Connection:
    MAX_FAILED_ATTEMPTS: int = 3

    def __init__(
        self,
        lure_name: str,
        lure_type: str,
        address_of_attacker: str,
        port_of_attacker: int,
        max_failed_attempts: int = MAX_FAILED_ATTEMPTS,
    ) -> None:
        self.id = uuid.uuid4().hex
        self.start_time = datetime.now(timezone.utc)
        self.lure_name = lure_name
        self.lure_type = lure_type
        self.address_of_attacker = address_of_attacker
        self.port_of_attacker = port_of_attacker
        self.max_failed_attempts = max_failed_attempts
        self.attempts: list[Attempt] = []
        self._is_active: bool = True
        self.end_time: datetime | None = None
        self.pending_username: str | None = None

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        raise AttributeError("modifying the is_active attribute is not allowed")

    def add_attempt(self, attempt: Attempt) -> None:
        if not self._is_active:
            print(f"Conn {self.id}. Connection terminated")
            return
        self.attempts.append(attempt)
        if self.get_attempt_count() >= self.max_failed_attempts:
            self.disconnect()

    def get_attempt_count(self) -> int:
        return len(self.attempts)

    def disconnect(self) -> None:
        if self._is_active:
            self._is_active = False
            self.end_time = datetime.now(timezone.utc)
            print(
                f"Conn {self.id} Connection to {self.address_of_attacker} terminated after {self.get_attempt_count()} attempts."
            )


conn1 = Connection(
    lure_name="ssh_lure",
    lure_type="low_interaction",
    address_of_attacker="192.168.1.50",
    port_of_attacker=22,
    max_failed_attempts=5,
)

conn2 = Connection(
    lure_name="ftp_lure",
    lure_type="low_interaction",
    address_of_attacker="192.168.1.49",
    port_of_attacker=21,
    max_failed_attempts=5,
)