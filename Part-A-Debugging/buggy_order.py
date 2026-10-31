# Initial buggy order discount program

def calculate_discount(total, discount_percent):

    if total < 0
        raise ValueError("Order total cannot be negative.")

    discount = total * discount_percent

    final_total = total - discount

    if final_total < 0:
        final_total = 0

    discount_ratio = total / discount

    return final_total

# Main program
order_total = 5000
discount_percent = 10

result = calculate_discount(order_total, discount_percent)

print("Final order total:", result)
