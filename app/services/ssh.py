from app.core.connection import Connection
from base import UniterService


class SshService(UniterService):
    pass

    def handle_data(self, connection: Connection, data: str):
        parts = data.split(maxsplit=1)

        if len(parts) != 2:
            return

        log, pas = parts
        self.process_auth_request(connection, log, password=pas)

conn1 = Connection(
    id="First_Conn",
    start_time="10:26",
    lure_name="ssh_lure",
    lure_type="low_interaction",
    address_of_attacker="192.168.1.50",
    port_of_attacker=22,
    max_failed_attempts=5,
)
c = SshService()
c.handle_data(conn1, 'mrx')
c.handle_data(conn1, 'mrx tunder1234')
print(conn1.attempts)
print(conn1.get_attempt_count())