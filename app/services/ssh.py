from app.core.connection import Connection
from base import UniterService


class SshService(UniterService):
    pass

conn1 = Connection(
    id="First_Conn",
    start_time="10:26",
    lure_name="ssh_lure",
    lure_type="low_interaction",
    address_of_attacker="192.168.1.50",
    port_of_attacker=22,
    max_failed_attempts=5,
)
