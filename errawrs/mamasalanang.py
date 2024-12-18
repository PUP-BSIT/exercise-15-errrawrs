class Mamasalanang:
    def __init__(self):
        self.name = "Gerald Mamasalanang"
        self.age = 19
        self.major = "Information Technology" 
        self.school = "PUP Taguig"  

    def name_property(self):
        return self.name

    def age_property(self):
        return self.age

    def major_property(self):
        return self.major

    def school_property(self):
        return self.school

    def greet(self):
        print(f"Hello, my name is {self.name} and I am a student at {self.school}.")

    def study(self):
        print(f"I am studying {self.major} at {self.school}.")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age} years old.")

    def change_major(self, new_major):
        self.major = new_major
        print(f"Now I am studying {self.major}.")

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Major: {self.major}, School: {self.school}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Greet")
            print("2. Study")
            print("3. Birthday")
            print("4. Change Major")
            print("5. Info")
            print("6. Exit")
            
            choice = input("Select an option: ")
            
            if choice == "1":
                self.greet()
            elif choice == "2":
                self.study()
            elif choice == "3":
                self.birthday()
            elif choice == "4":
                new_major = input("Enter the new major: ")
                self.change_major(new_major)
            elif choice == "5":
                self.info()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

