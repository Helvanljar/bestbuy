
from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product] = None):
        """Initialize the store with a list of products."""
        self.products = products if products is not None else []

    def add_product(self, product: Product):
        """Add a product to the store."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in the store.")

    def get_total_quantity(self) -> int:
        """Return total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Return a list of active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Buy multiple products at once.

        shopping_list: list of tuples (Product, quantity)
        Returns total price of the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.name} is not in the store.")
            total_price += product.buy(quantity)
        return total_price


# Test code
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products_active = best_buy.get_all_products()

    print("Total quantity in store:", best_buy.get_total_quantity())
    order_cost = best_buy.order([(products_active[0], 1),
                                 (products_active[1], 2)])
    print(f"Order cost: {order_cost} dollars.")
