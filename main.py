from products import Product
from store import Store




def start(store: Store):
while True:
print("\n===== Welcome to Best Buy =====")
print("1. List all products in store")
print("2. Show total amount in store")
print("3. Make an order")
print("4. Quit")


choice = input("Enter your choice (1-4): ").strip()


if choice == "1":
products_list = store.get_all_products()
if not products_list:
print("No active products available in the store.")
else:
print("\nProducts in store:")
for product in products_list:
product.show()


elif choice == "2":
total_quantity = store.get_total_quantity()
print(f"Total quantity of all products in store: {total_quantity}")


elif choice == "3":
products_list = store.get_all_products()
if not products_list:
print("No active products available to order.")
continue


print("\nAvailable products:")
for idx, product in enumerate(products_list, start=1):
print(f"{idx}. {product.name} - Price: {product.price}, Quantity: {product.get_quantity()}")


shopping_list = []


while True:
prod_choice = input("Enter product number to buy (or 'done' to finish): ").strip()


if prod_choice.lower() == "done":
break


try:
product_idx = int(prod_choice) - 1
if not (0 <= product_idx < len(products_list)):
print("Invalid product number. Try again.")
continue
except ValueError:
print("Please enter a valid number.")
continue


product = products_list[product_idx]


qty_input = input(f"Enter quantity for {product.name}: ").strip()
try:
quantity = int(qty_input)
start(best_buy)