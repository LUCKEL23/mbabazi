import json
import os


DATA_FILE = "students_and_hostels.json"


# PART A: DATA SETUP & OCCUPANCY OVERVIEW
# Predefine at least three hostel blocks, each with a fixed number 
# of rooms and a maximum capacity per room,
#  using a suitable data structure.
#  When the programme starts, print a brief occupancy overview.

hostels = [
    {
        "hostel_name" : "Eastern Wing Hostel",
        "no_rooms" : 10,
        "currently_occupied": 0,
        "room_capacity" : 4
    },
    {
        "hostel_name" : "Western Wing Hostel",
        "no_rooms" : 15,
        "currently_occupied": 0,
        "room_capacity" : 4
    },
    {
        "hostel_name" : "Southern Wing Hostel",
        "no_rooms" : 20,
        "currently_occupied": 0,
        "room_capacity" : 4
    }
]

students = []


# PART E: FILE PERSISTENCE

def load_data():
    """Loads hostels and students data from a file with graceful error handling."""
    if not os.path.exists(DATA_FILE):
        print(f"INFO '{DATA_FILE}' not found.")
        return hostels, students

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            print("SUCCESS Data successfully loaded from file.")
            return data["hostels"], data["students"]

    except (json.JSONDecodeError, KeyError):
        # Gracefully handle corrupted, empty, or improperly formatted files
        print(f"WARNING '{DATA_FILE}' is damaged or corrupted! Reverting to default data...")
        return hostels, students
    except Exception as e:
        print(f"[ERROR] Unexpected error while loading file: {e}")
        return hostels, students


def save_data(hostels, students):
    """Saves current state of hostels and students back to the JSON file."""
    data = {"hostels": hostels, "students": students}
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print("SUCCESS All changes saved to file.")
    except Exception as e:
        print(f"ERROR Could not save data to file: {e}")


# Initialize global database on startup
hostels, students = load_data()

def room_overview(hostels):

    print(f"\n----------OCCUPANCY OVERVIEW----------")
    
    for hostel in hostels:
        total_rooms_per_hostel = hostel['no_rooms'] * hostel['room_capacity']
        occupied = hostel["currently_occupied"]
        available = total_rooms_per_hostel - occupied
        print(f"\n")
        print(f"HOSTEL NAME : {hostel['hostel_name']}")
        print(f"TOTAL NUMBER OF ROOMS : {hostel['no_rooms']}")
        print(f"EACH ROOM HAS ACAPACITY OF : {hostel['room_capacity']}")
        print(f"ROOMS OCCUPIED : {hostel['currently_occupied']}")
        print(f"\n")
        print("= ="*30)
        print(f" THEREFORE {hostel['hostel_name'].upper()} HAS A MAXIMUM CAPACITY OF {available} FREE SPACES")
        print('= ='*30)
        


# PART B: STUDENT REGISTRATION AND ROOM ALLOCATION

# Allow a new student to be allocated to a specified room only if space remains in it.
# Reject the allocation with a clear explanation if the room is 
# already full and correctly update the room’s current occupancy when an allocation succeeds


def student_allocation(hostels, students):
    hostel_name = input("Enter Hostel Name: ").strip().lower()

    for hostel in hostels:
        if hostel_name == hostel["hostel_name"].lower():
            total_max_capacity = hostel["no_rooms"] * hostel["room_capacity"]

            if hostel["currently_occupied"] >= total_max_capacity:
                print("\n" + "=" * 45)
                print(f"REJECTED: {hostel['hostel_name'].upper()} IS FULL!")
                print(
                    f"Current Occupancy: {hostel['currently_occupied']} / {total_max_capacity}"
                )
                print("Explanation: All rooms in this hostel are occupied.")
                print("=" * 45)
                return

            student_name = input(
                "Enter student's name to be allocated: "
            ).strip()
            reg_no = input("Enter Registration Number: ").strip()

            while True:
                try:
                    total_fees = int(
                        input("Enter Total Tuition Fees (UGX): ").strip()
                    )
                    if total_fees >= 0:
                        break
                    print("Fees must be a positive amount!")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            hostel["currently_occupied"] += 1
            available_free_spaces = (
                total_max_capacity - hostel["currently_occupied"]
            )

            new_student = {
                "student_name": student_name,
                "reg_no": reg_no,
                "allocated_hostel": hostel["hostel_name"],
                "total_fees": total_fees,
                "fees_paid": 0,
                "outstanding_balance": total_fees,
            }
            students.append(new_student)

            print("\n" + "=" * 45)
            print("ALLOCATION SUCCESSFUL!")
            print(
                f"Student '{student_name}' allocated to {hostel['hostel_name']}."
            )
            print(
                f"Updated Occupancy: {hostel['currently_occupied']} / {total_max_capacity}"
            )
            print(f"Remaining Free Spaces: {available_free_spaces}")
            print("=" * 45)

            save_data(hostels, students)
            return

    print("\nInvalid hostel name! Please try again.")


# PART C: FEE PAYMENT RECORDING

# Write a function that allow full or partial fees to be recorded on student account,
#  track and correctly update the out standing balance across multiple payments made over time for students


def allow_and_track_payment(hostels, students):
    registration_number = input("Enter your Reg No: ").strip().lower()
    

    for student in students:
        if registration_number.lower() == student["reg_no"].lower():

            if student["outstanding_balance"] == 0:
                print("\n" + "-" * 31)
                print(f"Hi {student['student_name']}")
                print("Your fees are already fully cleared!")
                print(f"TOTAL AMOUNT PAID: {student['fees_paid']}")
                print("-" * 31)
                return

            try:
               amount_paid = int(input("How much do you want to pay? "))
            except ValueError:
                print("\n" + "-" * 31)
                print("Invalid input! Please enter a numeric amount.")
                print("-" * 31)
                return
            
            if amount_paid < student["outstanding_balance"] and amount_paid >0:
                student["outstanding_balance"] -= amount_paid
                student["fees_paid"] +=amount_paid
                print(f"\n")
                print('--------PAYMENT RECIEPT--------')
                print('-'*31)
                print(f"STUDENT NAME: {student['student_name']}")
                print(f"Reg No:{student['reg_no']}")
                print(f"Amount Paid: {amount_paid}")
                print(f"OUTSTANDING BALANCE: {student['outstanding_balance']}")
                print(f"TOTAL AMOUNT PAID: {student['fees_paid']}")
                print(f"\n")
                print("Partial Payment Recorded")
                print("-"*31)
                print("Thank you for paying, Goodbye!")
            elif amount_paid == student['outstanding_balance']:
                student["fees_paid"] += amount_paid
                student["outstanding_balance"] = 0
                print(f"\n")
                print("-"*31)
                print(f"STUDENT NAME: {student['student_name']}")
                print(f"Reg No:{student['reg_no']}")
                print(f"Amount Paid: {amount_paid}")
                print(f"OUTSTANDING BALANCE: {student['outstanding_balance']}")
                print(f"TOTAL AMOUNT PAID: {student['fees_paid']}")
                print("Fees cleared")
                print("-"*31)
                print("Thank you for paying, Goodbye!")
            elif amount_paid > student['outstanding_balance']:
                print(f"\n")
                print("-"*31)
                print("Amount paid should be in the range of the outstanding balance")
                print("-"*31)
                return
            else:
                print(f"\n")
                print("-"*31)
                print(f"Hi {student['student_name']}")
                print("Amount must be greater than '0'!")
                print("-"*31)

            save_data(hostels, students)

            return

    print("Invalid Reg No")


# PART D: SEARCH AND REPORTING

# Allow a student to be searched for by name or registration number. 
# Generate a full occupancy report for each hostel block and generate a list of “fee defaulters”,
#  meaning students whose outstanding balance is above a given threshold

def hostel_and_student_manager(hostels, students):
    print("\n" + "=" * 45)
    print("      HOSTEL & STUDENT MANAGEMENT SYSTEM     ")
    print("=" * 45)
    print("1. Search Student (by Name or Reg No)")
    print("2. Generate Hostel Occupancy Report")
    print("3. Generate Fee Defaulters Report")
    print("=" * 45)

    select_option = input("Select an option (1-3): ").strip()

    
    if select_option == "1":
        student_name_or_reg_no = input("\nEnter Student Name or Reg No: ").strip().lower()
        found = False

        for student in students:
            if (student_name_or_reg_no == student["student_name"].lower() or student_name_or_reg_no == student["reg_no"].lower()):
                found = True
                print("\n" + "=" * 45)
                print("STUDENT RECORD FOUND")
                print("=" * 45)
                print(f"Name                : {student['student_name']}")
                print(f"Reg No              : {student['reg_no']}")
                print(f"Total Fees          : UGX {student['total_fees']:,}")
                print(f"Fees Paid           : UGX {student['fees_paid']:,}")
                print(f"Outstanding Balance : UGX {student['outstanding_balance']:,}")

                allocated = student.get("allocated_hostel", "Not Allocated")
                print(f"Allocated Hostel    : {allocated}")
                print("=" * 45)
                break

        if not found:
            print("\nInvalid Reg No or Student Name!")

    
    elif select_option == "2":
        print("\n" + "=" * 55)
        print("           FULL HOSTEL OCCUPANCY REPORT           ")
        print("=" * 55)

        for hostel in hostels:
            total_capacity = hostel["no_rooms"] * hostel["room_capacity"]
            occupied = hostel["currently_occupied"]
            available = total_capacity - occupied
            occupancy_rate = (occupied / total_capacity) * 100

            print(f"\nHostel Block       : {hostel['hostel_name']}")
            print(f"Total Rooms        : {hostel['no_rooms']}")
            print(f"Capacity Per Room  : {hostel['room_capacity']} Students")
            print(f"Total Capacity     : {total_capacity} beds")
            print(f"Occupied Spaces    : {occupied}")
            print(f"Available Spaces   : {available}")
            print(f"Occupancy Rate     : {occupancy_rate}%")
            print("-" * 55)

    
    elif select_option == "3":
        try:
            student_balance = int(input("\nEnter outstanding balance: "))
        except ValueError:
            print("\nInvalid input! Please enter a numeric amount.")
            return

        print("\n" + "=" * 55)
        print(f"    FEE DEFAULTERS REPORT (Balance > UGX {student_balance:,})    ")
        print("=" * 55)

        defaulters_found = False
        for student in students:
            if student["outstanding_balance"] > student_balance:
                defaulters_found = True
                print(f"Student Name        : {student['student_name']}")
                print(f"Reg No              : {student['reg_no']}")
                print(f"Outstanding Balance : UGX {student['outstanding_balance']}")
                print("-" * 55)

        if not defaulters_found:
            print("No fee defaulters found.")

        

    else:
        print("\nInvalid option selected. Please enter 1, 2, or 3.")


# PART F: MENU-DRIVEN DRIVER PROGRAMME

def main():
    """Driver function uniting all system tasks behind an interactive menu loop."""
    hostels, students = load_data()

    # Print startup occupancy summary
    room_overview(hostels)

    while True:
        print("\n" + "=" * 50)
        print("  HOSTEL ROOM BOOKING & FEES MANAGEMENT SYSTEM  ")
        print("=" * 50)
        print("1. View Hostel Occupancy Overview")
        print("2. Allocate Room to Student")
        print("3. Record Fee Payment")
        print("4. Search Student & Generate Reports")
        print("5. Save and Exit")
        print("=" * 50)

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            room_overview(hostels)
        elif choice == "2":
            student_allocation(hostels, students)
        elif choice == "3":
            allow_and_track_payment(hostels, students)
        elif choice == "4":
            hostel_and_student_manager(hostels, students)
            
        elif choice == "5":
            save_data(hostels, students)
            print("\nExiting system. Have a great day!\n")
            break
        else:
            print("\n[ERROR] Invalid menu choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()