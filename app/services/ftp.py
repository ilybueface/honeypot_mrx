from app.core.connection import Connection
from base import UniterService


class FtpService(UniterService):
    def __init__(self):
        pass


conn1 = Connection(
    id="First_Conn",
    start_time="10:26",
    lure_name="fpt_lure",
    lure_type="low_interaction",
    address_of_attacker="192.168.1.50",
    port_of_attacker=22,
    max_failed_attempts=5,
)

c = FtpService()
auf = c.process_auth_request(conn1, "t23e2", "32e33e")
print(f"Quantity of attempts in connection: {len(conn1.attempts)}")
