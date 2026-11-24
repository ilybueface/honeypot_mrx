from app.core.connection import Connection
from app.services.base import UniterService


class FTPService(UniterService):
    def handle_login(self, connection: Connection, username: str):
        connection.pending_username = username

    def handle_password(self, connection: Connection, password: str):
        if connection.pending_username is None:
            return
        self.process_auth_request(connection, connection.pending_username, password)
        connection.pending_username = None

    def handle_data(self, connection: Connection, data: str):
        parts = data.split(maxsplit=1)

        if len(parts) != 2:
            return

        command, argument = parts
        if command == "USER":
            self.handle_login(connection, argument)
        elif command == "PASS":
            self.handle_password(connection, argument)


if __name__ == "__main__":
    conn1 = Connection(
        id="First_Conn",
        start_time="10:26",
        lure_name="ftp_lure",
        lure_type="low_interaction",
        address_of_attacker="192.168.1.50",
        port_of_attacker=22,
        max_failed_attempts=5,
    )
    c = FTPService()
    c.handle_data(conn1, "mrx")
    c.handle_data(conn1, "mrx tunder1234")
