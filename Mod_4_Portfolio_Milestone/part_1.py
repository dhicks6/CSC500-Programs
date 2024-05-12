class ItemToPurchase:
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
        return total_cost

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self):
        item_name = input("Enter the item name: ")
        item_price = float(input("Enter the item price: "))
        item_quantity = int(input("Enter the item quantity: "))
        item = ItemToPurchase(item_name, item_price, item_quantity)
        self.items.append(item)

    def calculate_total_cost(self):
        total_cost = sum(item.print_item_cost() for item in self.items)
        return total_cost

    def display_costs(self):
        total = self.calculate_total_cost()
        print("\nTotal: $", total)

def main():
    cart = ShoppingCart()
    print("Please enter details for two items.")

    for _ in range(2):
        cart.add_item()
    
    print("\nTOTAL COST")
    cart.display_costs()

if __name__ == "__main__":
    main()