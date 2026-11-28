import pytest
from app.core.connection import Connection, Attempt

def test_connection_is_active_cannot_be_modified():
    conn = Connection(
        lure_name="ssh_lure",
        lure_type="low_interaction",
        address_of_attacker="192.168.1.50",
        port_of_attacker=22,
    )

    with pytest.raises(AttributeError, match="modifying the is_active attribute is not allowed"):
        conn.is_active = False

def test_limit_of_connection_attempts():
    conn2 = Connection(
        lure_name="ftp_lure",
        lure_type="low_interaction",
        address_of_attacker="192.168.1.49",
        port_of_attacker=21,
        max_failed_attempts=3,
    )

    attempt = Attempt('mrx', 'mrx12345', '10:36')
    conn2.add_attempt(attempt)
    conn2.add_attempt(attempt)
    conn2.add_attempt(attempt)
    conn2.add_attempt(attempt)
    assert len(conn2.attempts) == 3
    assert conn2.is_active is False