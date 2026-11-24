from app.core.connection import Attempt, Connection


class DataLord:
    def __init__(self):
        self.attempts: list[Attempt] = []

    def add_attempt(self, attempt: Attempt):
        self.attempts.append(attempt)

c = DataLord()
conn1 = Connection(
    id="First_Conn",
    start_time="10:26",
    lure_name="ssh_lure",
    lure_type="low_interaction",
    address_of_attacker="192.168.1.50",
    port_of_attacker=22,
    max_failed_attempts=5,
)

conn2 = Connection(
    id="Firs_Conn",
    start_time="10:27",
    lure_name="ssh_lure",
    lure_type="low_interaction",
    address_of_attacker="192.168.1.50",
    port_of_attacker=22,
    max_failed_attempts=5,
)
a = Attempt('mrx', '398282', 10)
attempts_conn1 = [
    Attempt("mrx", "398282", 10),
    Attempt("admin", "admin123", 12),
]

attempts_conn2 = [
    Attempt("root", "toor", 8),
    Attempt("guest", "guest", 15),
]

for attempt in attempts_conn1:
    conn1.add_attempt(attempt)
    c.add_attempt(attempt)

for attempt in attempts_conn2:
    conn2.add_attempt(attempt)
    c.add_attempt(attempt)

