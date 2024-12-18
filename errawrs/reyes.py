import datetime
import os

def clrscr():
    os.system("cls")

def pause():
    input("Press enter to continue...")

class AttendanceManagement:
    records = {}
    present_count = {}
    total_days = 0

    # Method 1: Add a person
    def add_person(self, name_person):
        if name_person not in self.records:
            self.records[name_person] = []
            self.present_count[name_person] = 0
            print(f"{name_person} has been added to the attendance.")
        else:
            print(f"{name_person} is already in the system.")

    # Method 2: Mark attendance
    def mark_attendance(self, name_person, attendance_date):
        if name_person not in self.records:
            print(f"{name_person} is not registered in the system.")
            return

        if attendance_date not in self.records[name_person]:
            self.records[name_person].append(attendance_date)
            self.present_count[name_person] += 1
            self.total_days = max(self.total_days, 
                              len(self.records[name_person]))
            print(f"Attendance marked for {name_person} on {attendance_date}.")
        else:
            print(f"{name_person} is already marked on {attendance_date}.")
   
    #Method 3: Getting valid date      
    def get_valid_date(self):
        while True:
            try:
                year = int(input("Enter year (YYYY): "))
                month = int(input("Enter month (1-12): "))
                day = int(input("Enter day (1-31): "))
                return datetime.date(year, month, day).isoformat()
            except ValueError:
                print("Error!. Please enter valid  year, month, and day.")

    # Method 4: Get individual attendance
    def get_attendance(self, name_person):
        if name_person in self.records:
            return self.records[name_person]
        else:
            print(f"{name_person} is not registered in the system.")
            return None

    # Method 5: Summarize attendance
    def summarize_attendance(self):
        print("\nAttendance Summary:")
        for name_person, attendance_date in self.records.items():
            total_present = self.present_count[name_person]
            print(f"{name_person}: Present {total_present} time(s).")
        print(f"\nTotal days attendance has been marked: {self.total_days}")

    # Method 6: Reset attendance
    def reset_attendance(self):
        for name_person in self.records:
            self.records[name_person] = []
            self.present_count[name_person] = 0
        self.total_days = 0
        print("Attendance records have been reset.\n")

    # Menu
    def get_menu(self):
        while True:
            print("=========================================")
            print("||  Attendance Management System Menu  ||")
            print("=========================================")
            print("1. Add Person")
            print("2. Mark Attendance")
            print("3. Get Individual Attendance")
            print("4. Attendance Summary")
            print("5. Reset Attendance")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                person_name = input("Enter the person's name: ")
                self.add_person(person_name)
            elif choice == "2":
                person_name = input("Enter the person's name: ")
                attendance_date = self.get_valid_date()
                self.mark_attendance(person_name, attendance_date)
            elif choice == "3":
                person_name = input("Enter the person's name: ")
                attendance_date = self.get_attendance(person_name)
                if attendance_date is not None:
                    print(f"{person_name}")
                    print("Attendance:")
                    for attendance in attendance_date:
                        print(f"{attendance}")
            elif choice == "4":
                self.summarize_attendance()
            elif choice == "5":
                self.reset_attendance()
            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            
            clrscr()
            pause()

