class Car:

    brand = ""
    model = ""
    color = ""
    price = 0
    year = 0
        
    def get_brand(self, brand):
        self.brand = brand

    def get_model(self, model):
        self.model = model

    def get_color(self, color):
        self.color = color

    def get_price(self, price):
        self.price = price

    def get_year(self, year):
        self.years.append(year)

    def show_car_info(self):
        print("Car Info:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Price:", self.price)
        print("Year:", self.year)

    def menu(self):
        while True:

            print("\n Car Menu:")
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
                self.get_brand(brand)
            elif choice == "2":
                model = input("Enter the model: ")
                self.get_model(model)
            elif choice == "3":
                color = input("Enter the color: ")
                self.get_color(color)
            elif choice == "4":
                try:
                    price = int(input("Enter the price: "))
                    self.get_price(price)
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            elif choice == "5":
                try:
                    year = int(input("Enter the year: "))
                    self.get_year(year)
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            elif choice == "6":
                self.show_car_info()
            elif choice == "7":
                print("Exiting the menu.")
                break
            else:
                print("Invalid choice, please try again.")