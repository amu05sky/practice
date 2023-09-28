import calendar

# Create a dictionary to store important notes
notes = {}

def add_note():
    date = input("Enter the date (YYYY-MM-DD): ")
    note = input("Enter the note: ")
    notes[date] = note

def view_notes():
    date = input("Enter the date (YYYY-MM-DD): ")
    note = notes.get(date)
    if note:
        print(f"Note for {date}: {note}")
    else:
        print(f"No note found for {date}")

while True:
    print("\nCalendar Menu:")
    print("1. View Calendar")
    print("2. Add Note")
    print("3. View Notes")
    print("4. Exit")
    
    choice = input("Select an option (1/2/3/4): ")
    
    if choice == '1':
        year = int(input("Enter year (e.g., 2023): "))
        month = int(input("Enter month (1-12): "))
        cal = calendar.month(year, month)
        print(cal)
    elif choice == '2':
        add_note()
    elif choice == '3':
        view_notes()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")

print("Exiting...")
