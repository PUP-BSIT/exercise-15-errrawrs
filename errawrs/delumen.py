class Car:

    brand = ""
    model = ""
    color = ""
    price = 0
    year = 0
        
    def set_brand(self, brand):
        self.brand = brand
   
    def set_model(self, model):
        self.model = model

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def set_year(self, year):
            self.year = year

    def show_car_info(self):
        print("Car Info:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Price:", self.price)
        print("Year:", self.year)

    def menu(self):
        while True:

            print("\n Car:")
            print("1. Brand: ")
            print("2. Model: ")
            print("3. Color: ")
            print("4. Price: ")
            print("5. Year: ")
            print("6. Show Car Info: ")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                brand = input("Enter the brand: ")
                self.set_brand(brand)

            elif choice == "2":
                model = input("Enter the model: ")
                self.set_model(model)
            
            elif choice == "3":
                color = input("Enter the color: ")
                self.set_color(color)

            elif choice == "4":
                try:
                    price = int(input("Enter the price: "))
                    self.set_price(price)
                except ValueError:
                    print("Invalid input! Please enter a valid number for price.")

            elif choice == "5":
                try:
                    year = int(input("Enter the price: "))
                    self.set_year(year)
                except ValueError:
                    print("Invalid input! Please enter a valid number for year.")

            elif choice == "6":
                self.show_car_info()

            elif choice == "7":
                print("Exiting the menu.")
                break

            else:
                print("Invalid choice, please try again.")