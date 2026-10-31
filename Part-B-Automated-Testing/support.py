
def create_support_ticket(customer_name, issue, priority="normal"):
    """Create a customer support ticket."""

    if not customer_name.strip():
        raise ValueError("Customer name cannot be empty.")

    if not issue.strip():
        raise ValueError("Issue description cannot be empty.")

    if priority not in ("low", "normal", "high"):
        raise ValueError("Priority must be low, normal, or high.")

    ticket = {
        "customer_name": customer_name.strip(),
        "issue": issue.strip(),
        "priority": priority,
        "status": "open"
    }

    return ticket


def get_response_time(priority):
    """Return the expected response time based on ticket priority."""

    if priority == "high":
        return 4

    elif priority == "normal":
        return 24

    elif priority == "low":
        return 48

    else:
        raise ValueError("Invalid ticket priority.")


def close_support_ticket(ticket):
    """Close an open support ticket."""

    if ticket["status"] == "closed":
        raise ValueError("Ticket is already closed.")

    ticket["status"] = "closed"

    return ticket
