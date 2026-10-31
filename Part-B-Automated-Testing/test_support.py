
import pytest

from support import (
    create_support_ticket,
    get_response_time,
    close_support_ticket
)


# ==========================================
# TESTS FOR SUPPORT TICKET CREATION
# ==========================================

def test_create_ticket_with_valid_details():
    ticket = create_support_ticket(
        "Ada",
        "Unable to complete payment"
    )

    assert ticket["customer_name"] == "Ada"
    assert ticket["issue"] == "Unable to complete payment"
    assert ticket["priority"] == "normal"
    assert ticket["status"] == "open"


def test_create_ticket_with_high_priority():
    ticket = create_support_ticket(
        "John",
        "Payment failed",
        "high"
    )

    assert ticket["priority"] == "high"


def test_create_ticket_with_low_priority():
    ticket = create_support_ticket(
        "Mary",
        "General enquiry",
        "low"
    )

    assert ticket["priority"] == "low"


def test_create_ticket_with_empty_customer_name():
    with pytest.raises(ValueError):
        create_support_ticket("", "Payment issue")


def test_create_ticket_with_whitespace_customer_name():
    with pytest.raises(ValueError):
        create_support_ticket("   ", "Payment issue")


def test_create_ticket_with_empty_issue():
    with pytest.raises(ValueError):
        create_support_ticket("Ada", "")


def test_create_ticket_with_invalid_priority():
    with pytest.raises(ValueError):
        create_support_ticket("Ada", "Payment issue", "urgent")


# ==========================================
# TESTS FOR RESPONSE TIME
# ==========================================

def test_high_priority_response_time():
    assert get_response_time("high") == 4


def test_normal_priority_response_time():
    assert get_response_time("normal") == 24


def test_low_priority_response_time():
    assert get_response_time("low") == 48


def test_response_time_with_invalid_priority():
    with pytest.raises(ValueError):
        get_response_time("urgent")


# ==========================================
# TESTS FOR CLOSING SUPPORT TICKETS
# ==========================================

def test_close_open_support_ticket():
    ticket = create_support_ticket(
        "Ada",
        "Unable to log in"
    )

    closed_ticket = close_support_ticket(ticket)

    assert closed_ticket["status"] == "closed"


def test_close_already_closed_ticket():
    ticket = create_support_ticket(
        "Ada",
        "Unable to log in"
    )

    close_support_ticket(ticket)

    with pytest.raises(ValueError):
        close_support_ticket(ticket)

        
# ==========================================
# INTEGRATED SUPPORT-TICKET PATH TEST
# ==========================================

def test_high_priority_ticket_response_and_closure():
    ticket = create_support_ticket(
        "Ada",
        "Payment failed",
        "high"
    )

    response_time = get_response_time(ticket["priority"])
    closed_ticket = close_support_ticket(ticket)

    assert response_time == 4
    assert closed_ticket["status"] == "closed"

