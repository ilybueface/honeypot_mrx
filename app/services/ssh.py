from app.core.connection import Connection
from app.services.base import UniterService


class SSHService(UniterService):
    pass

    def handle_data(self, connection: Connection, data: str):
        parts = data.split(maxsplit=1)

        if len(parts) != 2:
            return

        log, pas = parts
        self.process_auth_request(connection, log, password=pas)


if __name__ == "__main__":
    conn1 = Connection(
        id="First_Conn",
        start_time="10:26",
        lure_name="ssh_lure",
        lure_type="low_interaction",
        address_of_attacker="192.168.1.50",
        port_of_attacker=22,
        max_failed_attempts=5,
    )
    c = SSHService()
    c.handle_data(conn1, "mrx")
    c.handle_data(conn1, "mrx tunder1234")
