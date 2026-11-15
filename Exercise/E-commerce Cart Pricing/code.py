class Product :
    def __init__(self, sku, name, unit_price):
        if unit_price < 0 :
            raise ValueError("Unit Price cannot be negative")
        self.sku = sku 
        self.name = name
        self.unit_price = unit_price

class CartItem:
    def __init__(self, product, quantity):
        if quantity <= 0 :
            raise ValueError("Quantity must be positive")
        self.product = product 
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if quantity <= 0 :
            raise ValueError("Quantity must be positive")
        sku = product.sku

        if sku in self.items: 
            self.items[sku].quantity += quantity 
        else :
            self.items[sku] = CartItem(product, quantity)

    def remove_item(self, sku) :
        if sku in self.items:
            del self.items[sku]

    def subtotal(self):
        return sum(
            item.product.unit_price * item.quantity 
            for item in self.items.values()
        )

    def total(self, discount = 0 ):
        if not 0<= discount <=100 :
            raise ValueError("Discount must be between 0 and 100 ")

        discount_amount = self.subtotal() * discount / 100 
        return self.subtotal() - discount_amount
    
p1 = Product("P001", "Keyboard", 500)
p2 = Product("P002", "Mouse", 200)

cart = ShoppingCart()

cart.add_item(p1, 1)
cart.add_item(p1, 1)
cart.add_item(p2, 1)

print("Subtotal:", cart.subtotal())
print("Total:", cart.total(10))
print("Keyboard Quantity:", cart.items["P001"].quantity)