class Product:
def __init__(self, name: str, price: float, quantity: int):
if not name:
raise ValueError("Product name cannot be empty.")
if price < 0:
raise ValueError("Product price cannot be negative.")
if quantity < 0:
raise ValueError("Product quantity cannot be negative.")


self.name = name
self.price = price
self.quantity = quantity
self.active = True


def get_quantity(self) -> int:
return self.quantity


def set_quantity(self, quantity: int):
if quantity < 0:
raise ValueError("Quantity cannot be negative.")
self.quantity = quantity
if self.quantity == 0:
self.deactivate()
else:
self.activate()


def is_active(self) -> bool:
return self.active


def activate(self):
self.active = True


def deactivate(self):
self.active = False


def show(self):
status = "Active" if self.active else "Inactive"
print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Status: {status}")


def buy(self, quantity: int) -> float:
if quantity <= 0:
raise ValueError("Purchase quantity must be greater than zero.")
if quantity > self.quantity:
raise ValueError(f"Cannot buy {quantity} units. Only {self.quantity} available.")


total_price = self.price * quantity
self.set_quantity(self.quantity - quantity)
return total_price