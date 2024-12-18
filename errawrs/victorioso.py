import os

MAX_CAP = 100  

def clrscr():
    os.system("cls")

def pause():
    input("Press enter to continue...")

class InventoryManager:
    def __init__(self):
        self.invntry = {}
        self.curr_cap = 0

    def add_item(self, item_name, quanti):
        item_name_lwr = item_name.lower()

        if self.curr_cap + quanti > MAX_CAP:
            print(f"Cannot add {quanti} {item_name}(s). Exceeds max capacity.")
            return

        if item_name_lwr in self.invntry:
            self.invntry[item_name_lwr] += quanti
        else:
            self.invntry[item_name_lwr] = quanti

        self.curr_cap += quanti
        print(f"{quanti} {item_name}(s) have been added.")

    def remove_item(self, item_name):
        item_name_lwr = item_name.lower()

        if item_name_lwr in self.invntry:
            self.curr_cap -= self.invntry[item_name_lwr]
            del self.invntry[item_name_lwr]
            print(f"{item_name} has been removed from the inventory.")
        else:
            print(f"{item_name} is not in the inventory.")

    def update_item_quanti(self, item_name, new_quanti):
        item_name_lwr = item_name.lower()

        if item_name_lwr not in self.invntry:
            print(f"{item_name} is not in the inventory.")
            return

        if self.curr_cap - self.invntry[item_name_lwr] + new_quanti > MAX_CAP:
            print(f"Cannot update {item_name}. Exceeds max capacity.")
            return

        self.curr_cap = (self.curr_cap - self.invntry[item_name_lwr] +
                         new_quanti)
        self.invntry[item_name_lwr] = new_quanti
        print(f"The quantity of {item_name} has been updated to {new_quanti}.")

    def view_inventory(self):
        if not self.invntry:
            print("The inventory is empty.")
        else:
            print("Inventory List:")
            for item_name, quanti in self.invntry.items():
                print(f"- {item_name.capitalize()}: {quanti}")

    def search_item(self, item_name):
        item_name_lwr = item_name.lower()

        if item_name_lwr in self.invntry:
            print(f"{item_name} is in the inventory with a quantity "
                  f"of {self.invntry[item_name_lwr]}.")
        else:
            print(f"{item_name} is not in the inventory.")

    def display_menu(self):
        while True:
            print("\nInventory Manager:")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Item quantity")
            print("4. View Inventory")
            print("5. Search for an Item")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                item_name = input("Enter the item name: ")
                try:
                    quanti = int(input("Enter the quantity: "))
                    self.add_item(item_name, quanti)
                except ValueError:
                    print("Please enter a valid number for quantity.")
            elif choice == "2":
                item_name = input("Enter the item name: ")
                self.remove_item(item_name)
            elif choice == "3":
                item_name = input("Enter the item name: ")
                try:
                    new_quanti = int(input("Enter the new quantity: "))
                    self.update_item_quanti(item_name, new_quanti)
                except ValueError:
                    print("Please enter a valid number for quantity.")
            elif choice == "4":
                self.view_inventory()
            elif choice == "5":
                item_name = input("Enter the item name: ")
                self.search_item(item_name)
            elif choice == "6":
                print("Exiting Inventory Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            
            pause()
            clrscr()
