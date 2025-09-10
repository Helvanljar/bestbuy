from typing import List, Tuple
from products import Product




class Store:
def __init__(self, products: List[Product] = None):
self.products = products if products is not None else []


def add_product(self, product: Product):
if not isinstance(product, Product):
raise TypeError("Only Product instances can be added.")
self.products.append(product)


def remove_product(self, product: Product):
if product in self.products:
self.products.remove(product)
else:
raise ValueError("Product not found in the store.")


def get_total_quantity(self) -> int:
return sum(product.get_quantity() for product in self.products)


def get_all_products(self) -> List[Product]:
return [product for product in self.products if product.is_active()]


def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
total_price = 0.0
for product, quantity in shopping_list:
if product not in self.products:
raise ValueError(f"{product.name} is not in the store.")
total_price += product.buy(quantity)
return total_price