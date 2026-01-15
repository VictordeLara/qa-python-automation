def calculate_total(price,discout_rate,tax_rate):
    discout = price * discout_rate
    tax = (price - discout) * tax_rate
    total = price - discout + tax
    return round(total,2)