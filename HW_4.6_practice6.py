class Product:
    # Class attributes
    store_name = "ITC Online Store"
    product_count = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.product_count += 1
        self.id = Product.product_count

    def display_product(self):
        print(f"Product {self.id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value()}")

    def total_value(self):
        return self.price * self.quantity

    @classmethod
    def get_product_count(cls):
        return cls.product_count

    @staticmethod
    def is_valid_price(price):
        return price > 0


# Create products (validate price first)
products = []
data = [("Laptop", 800, 5), ("Mouse", 15, 20), ("Keyboard", 30, 10)]

for name, price, quantity in data:
    if Product.is_valid_price(price):
        products.append(Product(name, price, quantity))

# Display everything
print(f"========== {Product.store_name.upper()} ==========")
print()

total_inventory = 0
for p in products:
    p.display_product()
    print()
    total_inventory += p.total_value()

print(f"Total Products: {Product.get_product_count()}")
print(f"Total Inventory Value: ${total_inventory}")