"""
Simple Online Shopping System using classes.
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (₹{self.price})"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        total = 0
        print("Items in cart:")
        for p in self.items:
            print(f"- {p.name}: ₹{p.price}")
            total += p.price
        print(f"Total amount: ₹{total}")


products = [
    Product("Book", 200),
    Product("Pen", 20),
    Product("Headphones", 1500),
]

cart = Cart()

while True:
    print("\n=== Online Shopping System ===")
    print("1. View products")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Available products:")
        for i, p in enumerate(products, start=1):
            print(f"{i}. {p}")
    elif choice == "2":
        index = int(input("Enter product number to add: "))
        if 1 <= index <= len(products):
            cart.add_product(products[index - 1])
        else:
            print("Invalid product number.")
    elif choice == "3":
        cart.view_cart()
    elif choice == "4":
        print("Exiting Online Shopping System.")
        break
    else:
        print("Invalid choice.")
