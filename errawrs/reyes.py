class AttendanceManagement:
    # Method 1: 
    def add_person(self, name_person):
        if name_person not in self.records:
            self.records[name_person] = []
            self.present_count[name_person] = 0
            print(f"{name_person} has been added to the attendance.")
        else:
            print(f"{name_person} is already in the system.")

    # Method 2:
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
            print(f"{name_person} is already marked  on {attendance_date}.")

    # Method 3: 
    def get_attendance(self, name_person):
        if name_person in self.records:
            return self.records[name_person]
        else:
            print(f"{name_person} is not registered in the system.")
            return None

    # Method 4:
    def summarize_attendance(self):
        print("\nAttendance Summary:")
        for name_person, attendance_date in self.records.items():
            total_present = self.present_count[name_person]
            print(f"{name_person}: Present {total_present} time(s).")
        print(f"\nTotal days attendance has been marked: {self.total_days}")

    # Method 5: 
    def reset_attendance(self):
        for name_person in self.records:
            self.records[name_person] = []
            self.present_count[name_person] = 0
        self.total_days = 0
        print("Attendance records have been reset.\n")

    def menu(self):
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

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                person_name = input("Enter the person's name: ")
                self.add_person(person_name)
            elif choice == "2":
                person_name = input("Enter the person's name: ")
                attendance_date = (input("Enter the date (YYYY-MM-DD): "))
                self.mark_attendance(person_name, attendance_date)
            elif choice == "3":
                person_name = input("Enter the person's name: ")
                attendance_date = self.get_attendance(person_name)
                if attendance_date is not None:
                    print(f"{person_name}'s Attendance: {attendance_date}")
            elif choice == "4":
                self.summarize_attendance()
            elif choice == "5":
                self.reset_attendance()
            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Initialize the  without a constructor
attendance_system = AttendanceManagement()

# Initialize the necessary variables directly
attendance_system.records = {}
attendance_system.present_count = {}
attendance_system.total_days = 0

# Run the system interactively
attendance_system.menu()
