class BasicMath:
    def __init__(self):
        self.value_1 = 0
        self.value_2 = 0
        self.total = 0

    def get_number(self, ):
        self.value_1 = float(input("Enter a number: "))
        self.value_2 = float(input("Enter a number: "))

        print("\n")

    def add(self):
        self.total = self.value_1 + self.value_2

        print(f"{self.value_1} + {self.value_2} = {self.total}")
        print("\n")
    
    def subtract(self):
        self.total = self.value_1 - self.value_2

        print(f"{self.value_1} - {self.value_2} = {self.total}")
        print("\n")
    
    def multiply(self):
        self.total = self.value_1 * self.value_2

        print(f"{self.value_1} * {self.value_2} = {self.total}")
        print("\n")
    
    def divide(self):
        try:
            self.total = self.value_1 / self.value_2

            print(f"{self.value_1} / {self.value_2} = {self.total}")
            print("\n")
        except ZeroDivisionError:
            print("zero can't be divided by zero")

    def display_menu(self):
        math = BasicMath()

        while True:
            print("1. Input number")
            print("2. Addition")
            print("3. Subtraction")
            print("4. Multiplication")
            print("5. Division")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n")
                try:
                    math.get_number()
                except ValueError:
                    print("Enter a valid value")
                
                print("\n")
            elif choice == "2":
                print("\n")

                math.add()
            elif choice == "3":
                print("\n")

                math.subtract()
            elif choice == "4":
                print("\n")

                math.multiply()
            elif choice == "5":
                print("\n")

                math.divide()
                
                print("\n")
            elif choice == "6":
                print("Exiting...")
                print("\n")
                break
            else:
                print("Invalid input!!!")
                print("\n")