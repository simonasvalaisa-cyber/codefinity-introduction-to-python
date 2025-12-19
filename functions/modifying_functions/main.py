def apply_discount(price, discount=0.05):
    discounted_price = price * (1 - discount)
    return discounted_price

def apply_tax(price, tax=0.07):
    taxed_price = price * (1 + tax)
    return taxed_price

def calculate_total(price, discount=0.05, tax=0.07):
    total_cost = price * (1 + tax) * (1 - discount)
    return total_cost

total = calculate_total(120)
custom_total = calculate_total(100, discount=0.10, tax=0.08)
print("Total cost with default discount and tax: $", total)
print("Total cost with custom discount and tax: $", custom_total)
