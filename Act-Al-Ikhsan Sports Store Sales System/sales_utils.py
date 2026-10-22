def calculate_total(price, quantity):
    total = price * quantity
    return total

def calculate_discount(total):
    if total >= 300:
        discount = total * 0.15
        return discount
    elif total >= 200:
        discount = total * 0.10
        return discount
    elif total >= 100:
        discount = total * 0.05
        return discount
    else:
        discount = 0.0
        return discount

def calculate_final(total, discount):
    final = total - discount
    return final