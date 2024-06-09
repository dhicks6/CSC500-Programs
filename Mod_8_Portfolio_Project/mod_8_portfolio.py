# The ItemToPurchase class is a class with a constructor to make items
class ItemToPurchase:
    def __init__(self, item_name, item_price, item_quantity, item_description):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Method to print the cost of the item
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
        return total_cost

# The ShoppingCart class is a class with a constructor to make a shopping cart
# allowing us to use functions to add, remove and edit items in the shopping cart
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Method to add an item to the shopping cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Method to remove an item from the shopping cart   
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    # Method to modify an item's details in the shopping cart
    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                if item.item_description != "":
                    cart_item.item_description = item.item_description
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    # Method to get the total number of items in the cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # Method to get the total cost of the cart
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    # Method to print the total cost and details of items in the cart
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    # Method to print the descriptions of items in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

    # Method to calculate the total cost of items in the cart (not used)
    def calculate_total_cost(self):
        total_cost = sum(item.print_item_cost() for item in self.items)
        return total_cost

    # Method to display the total cost (not used)
    def display_costs(self):
        total = self.calculate_total_cost()
        print("\nTotal: $", total)

# Function to print the menu and handle user options
def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "Choose an option: "
    )
    option = ""
    while option != "q":
        option = input(menu).strip()
        if option == "a":
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
        elif option == "r":
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)
        elif option == "c":
            item_name = input("Enter the item name: ")
            item_quantity = int(input("Enter the new quantity: "))
            # Use a default price and description to modify only the quantity
            item = ItemToPurchase(item_name, 0, item_quantity, "")
            cart.modify_item(item)
        elif option == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif option == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        elif option != "q":
            print("Invalid option. Please choose again.")

# Main function to initialize the shopping cart and start the menu
def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    print_menu(cart)

if __name__ == "__main__":
    main()
