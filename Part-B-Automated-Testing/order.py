
def calculate_discount(total, discount_percent):
    """Calculate the final amount after applying a discount."""

    if total < 0:
        raise ValueError("Order total cannot be negative.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    discount = total * (discount_percent / 100)
    return round(total - discount, 2)


def calculate_shipping(subtotal):
    """Calculate shipping fee based on the order subtotal."""

    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if subtotal >= 50000:
        return 0.0

    return 2500.0


def calculate_order_total(unit_price, quantity, discount_percent=0):
    """Calculate the complete order total, including shipping."""

    if unit_price < 0:
        raise ValueError("Unit price cannot be negative.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    subtotal = unit_price * quantity
    discounted_total = calculate_discount(subtotal, discount_percent)
    shipping_fee = calculate_shipping(discounted_total)

    return round(discounted_total + shipping_fee, 2)
