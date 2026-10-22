from sales_utils import *

class Sales:
    def __init__(self, custName, proName, price, quantity):
        self.custName = custName
        self.proName = proName
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return(
            ""
            "~~~ AL-IKHSAN SPORTS STORE ~~~\n"
            f"Customer Name: {self.custName}\n"
            f"Product Name: {self.proName}\n"
            f"Price: RM {self.price:.2f}\n"
            f"Quantity: {self.quantity}\n"
        )

    def display_receipt(self):
        total = calculate_total(self.price, self.quantity)
        discount = calculate_discount(total)
        final = calculate_final(total, discount)

        print(self)
        print("~~~ RECEIPT ~~~")
        print(f"Total Sales: RM {total:.2f}")
        print(f"Discount: {discount:.2f}")
        print(f"Final Total: {final:.2f}")
        print("Thank you for shopping with us.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

name = input("Enter name: ")
product = input("Enter product: ")
price = input("Enter price: ")
quantity = input("Enter quantity: ")

S = Sales(name, product, price, quantity)
S.display_receipt()