from app.core.connection import Connection
from base import UniterService


class FtpService(UniterService):
    def handle_login(self, connection: Connection, username: str):
        connection.pending_username = username

    def handle_password(self, connection: Connection, password: str):
        if connection.pending_username is None:
            return
        self.process_auth_request(connection, connection.pending_username, password)
        connection.pending_username = None

conn1 = Connection(
    id="First_Conn",
    start_time="10:26",
    lure_name="ftp_lure",
    lure_type="low_interaction",
    address_of_attacker="192.168.1.50",
    port_of_attacker=21,
    max_failed_attempts=5,
)
