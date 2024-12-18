from errawrs.mamasalanang import Mamasalanang
from errawrs.victorioso import InventoryManager
from errawrs.mosquito import BasicMath
from errawrs.delumen import Car
from errawrs.reyes import AttendanceManagement

def menu_members():
    print("==================================")
    print("||   Welcome! Select a Person!  ||")
    print("==================================")
    print("[1] Ivan Delumen")
    print("[2] Gerald Mamasalanang")
    print("[3] Michael Angelo Mosquito")
    print("[4] Simone Jake Reyes")
    print("[5] Daniel Victorioso")
    print("[6] Exit")

def main_function():
    while True:
        menu_members()

        choice = input("Enter your Choice: ")

        if choice == '1':
            delumen = Car()
            delumen.menu()
        elif choice == '2':
            student_instance = Mamasalanang()
            student_instance.display_menu()
        elif choice == '3':
            michael = BasicMath()
            michael.display_menu()
        elif choice == '4':
            reyes = AttendanceManagement()
            reyes.get_menu()
            print("Simone")
        elif choice == '5':
            victorioso = InventoryManager()
            victorioso.display_menu()
        elif choice == '6':
            print("Exiting")
            break
        else:
            print("Invalid Choice")

main_function()