# E-commerce Cart Pricing

## Overview

Day 01 challenge: a shopping cart built with **composition**. `Product` and `CartItem` are composed into a `ShoppingCart` that aggregates quantities by SKU, computes subtotals, and applies a percentage discount. Invalid inputs (negative prices, nonpositive quantities, discounts outside 0–100%) are rejected with `ValueError`.

## Tasks

- [x] Create `Product(sku, name, unit_price)` and `CartItem(product, quantity)`.
- [x] Implement `ShoppingCart.add_item()`, `remove_item()`, `subtotal()` and `total()` with a percentage discount.
- [x] Reject negative prices, nonpositive quantities, and discounts outside 0–100%.

## Pass Checks

- [x] Two units of ₹500 and one unit of ₹200 give subtotal ₹1,200.
- [x] A 10% discount gives total ₹1,080.
- [x] Adding an existing SKU updates its quantity instead of duplicating it.

## Code

```python
class Product:
    def __init__(self, sku, name, unit_price):
        if unit_price < 0:
            raise ValueError("Unit Price cannot be negative")
        self.sku = sku
        self.name = name
        self.unit_price = unit_price

class CartItem:
    def __init__(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        sku = product.sku
        if sku in self.items:
            self.items[sku].quantity += quantity
        else:
            self.items[sku] = CartItem(product, quantity)

    def remove_item(self, sku):
        if sku in self.items:
            del self.items[sku]

    def subtotal(self):
        return sum(item.product.unit_price * item.quantity
                   for item in self.items.values())

    def total(self, discount=0):
        if not 0 <= discount <= 100:
            raise ValueError("Discount must be between 0 and 100")
        discount_amount = self.subtotal() * discount / 100
        return self.subtotal() - discount_amount
```

## How the Code Satisfies the Tasks

- **Product**: validates `unit_price >= 0`, stores `sku`, `name`, `unit_price`.
- **CartItem**: validates `quantity > 0`, holds a `Product` reference and quantity.
- **ShoppingCart**: uses a dict keyed by SKU so duplicate SKUs aggregate quantity instead of duplicating.
- **add_item**: validates quantity, then either increments existing or creates new `CartItem`.
- **remove_item**: deletes the SKU entry if present.
- **subtotal**: sums `unit_price * quantity` across items.
- **total**: validates discount range, subtracts the percentage discount from subtotal.

## Sample Behavior

```python
p1 = Product("P001", "Keyboard", 500)
p2 = Product("P002", "Mouse", 200)

cart = ShoppingCart()
cart.add_item(p1, 1)
cart.add_item(p1, 1)   # aggregates -> quantity 2
cart.add_item(p2, 1)

print("Subtotal:", cart.subtotal())        # 1200
print("Total:", cart.total(10))            # 1080.0
print("Keyboard Quantity:", cart.items["P001"].quantity)  # 2
```

## Running the example

```bash
cd "Exercise/E-commerce Cart Pricing"
python code.py
```

Expected output:

```
Subtotal: 1200
Total: 1080.0
Keyboard Quantity: 2
```

## Interview Questions

1. **Why is a cart better modeled with composition than inheritance?**
   A cart *has* products and cart items; it is not a kind of product. Composition models "has-a" relationships, keeps responsibilities separated, and allows the cart to aggregate arbitrary products without a rigid class hierarchy.

2. **How do you prevent duplicate SKUs in the cart?**
   Store items in a dictionary keyed by SKU. On `add_item`, if the SKU already exists, increment its quantity instead of inserting a new `CartItem`, preserving a single source of truth per product.

3. **Where should validation live — Product, CartItem, or ShoppingCart?**
   Validate at the boundary where data enters: `Product` validates price, `CartItem`/`add_item` validate quantity, and `total` validates discount. This keeps each class responsible for its own invariants.

4. **How would you handle a discount that makes the total negative?**
   Either clamp the result to zero or reject the discount configuration. The current implementation assumes discounts are 0–100%, so the total cannot go negative; a fixed-amount discount would need explicit clamping.

5. **What is the time complexity of `subtotal()` and `add_item()`?**
   `add_item()` is O(1) amortized (dict lookup/insert). `subtotal()` is O(n) where n is the number of distinct SKUs, since it iterates over all items.
