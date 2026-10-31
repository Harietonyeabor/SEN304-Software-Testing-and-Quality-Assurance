
def calculate_discount(total, discount_percent):
    """Calculate the final order total after applying a discount."""

    if total < 0:
        raise ValueError("Order total cannot be negative.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    discount = total * (discount_percent / 100)
    final_total = total - discount

    return final_total


def calculate_unit_price(order_total, quantity):
    """Calculate unit price and handle division by zero."""

    try:
        unit_price = order_total / quantity
        return unit_price

    except ZeroDivisionError:
        print("Error: Quantity must be greater than zero.")
        return None


# Main program
order_total = 5000
discount_percent = 10
quantity = 2

try:
    result = calculate_discount(order_total, discount_percent)
    print("Final order total:", result)

    unit_price = calculate_unit_price(order_total, quantity)

    if unit_price is not None:
        print("Unit price:", unit_price)

except ValueError as error:
    print("Input error:", error)
