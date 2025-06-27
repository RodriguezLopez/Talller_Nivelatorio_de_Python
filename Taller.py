def register_student():
    """
    Allows the user to register a new student.
    Requests name, ID, age, and at least 3 grades.
    Implements validations for each input.
    """
    print("\n--- 1. Register student ---")
    
    # --- ID validation ---
    while True:
        try:
            student_id = input("Enter the identification number (numbers only): ")
            # Validates that the ID is numeric and not empty
            if not student_id.isdigit() or len(student_id.strip()) == 0:
                print("Error: The ID must be a valid number.")
                continue
            # Checks if the student is already registered
            if student_id in students:
                print(f"Error: A student with ID '{student_id}' is already registered.")
                return  # Exit the function if already exists
            break
        except Exception:
            print("Invalid input. Please enter a number.")

    # --- Name validation ---
    while True:
        name = input("Enter the student's name: ").strip().title()  # Capitalizes the first letter of each word
        # Validates that the name is not empty and contains only letters and spaces
        if len(name) > 0 and all(c.isalpha() or c.isspace() for c in name):
            break
        else:
            print("Error: The name cannot be empty and must contain only letters.")

    # --- Age validation ---
    while True:
        try:
            age_str = input("Enter the student's age (1-99): ")
            age = int(age_str)
            # Validates that the age is within a reasonable range
            if 1 <= age <= 99:
                break
            else:
                print("Error: Age must be a number between 1 and 99.")
        except ValueError:
            print("Error: Please enter a whole number for the age.")

    # --- Grades validation ---
    grades = []
    print("Enter the student's grades (minimum 3 grades).")
    while len(grades) < 3:
        try:
            grade_str = input(f"Enter grade #{len(grades) + 1} (0.0 to 5.0): ")
            grade = float(grade_str)
            # Validates that the grade is in range
            if 0.0 <= grade <= 5.0:
                grades.append(grade)
            else:
                print("Error: Grade must be between 0.0 and 5.0.")
        except ValueError:
            print("Error: Please enter a valid decimal number for the grade.")

    # Creates the student dictionary and adds it to the global dictionary
    students[student_id] = {
        'name': name,
        'age': age,
        'grades': grades
    }
    print(f"\nStudent '{name}' successfully registered with ID: {student_id}!\n")

def calculate_average(grades):
    """Calculates the average of a list of grades."""
    # Validates that the list is not empty to avoid division by zero
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def consult_student():
    """
    Allows the user to view a student's information by ID.
    Shows name, age, grades, and average.
    """
    print("\n--- 2. Consult student ---")
    student_id = input("Enter the student's ID to consult: ")
    
    if student_id in students:
        student = students[student_id]
        avg = calculate_average(student['grades'])

        print("\n--- Student Information ---")
        print(f"Name: {student['name']}")
        print(f"ID: {student_id}")
        print(f"Age: {student['age']}")
        print(f"Grades: {student['grades']}")
        print(f"Average: {avg:.2f}")
        print("-" * 30)
    else:
        print(f"\nError: No student found with ID '{student_id}'.")

def update_grades():
    """
    Allows modifying the grades of an existing student.
    """
    print("\n--- 3. Update grades ---")
    student_id = input("Enter the student's ID to update their grades: ")
    
    if student_id in students:
        student = students[student_id]
        print(f"Student found: {student['name']}. Current grades: {student['grades']}")

        new_grades = []
        print("Enter the new grades (minimum 3 grades).")
        while True:
            try:
                grade_str = input(f"Enter grade #{len(new_grades) + 1} (or 'f' to finish): ")
                if grade_str.lower() == 'f':
                    if len(new_grades) >= 3:
                        break
                    else:
                        print("Error: You must enter at least 3 grades.")
                        continue
                grade = float(grade_str)
                if 0.0 <= grade <= 5.0:
                    new_grades.append(grade)
                else:
                    print("Error: Grade must be between 0.0 and 5.0.")
            except ValueError:
                print("Error: Invalid input. Enter a number or 'f'.")

        student['grades'] = new_grades
        new_avg = calculate_average(new_grades)
        print(f"\nGrades updated successfully for '{student['name']}'!")
        print(f"New average: {new_avg:.2f}\n")
    else:
        print(f"\nError: No student found with ID '{student_id}'.")

def delete_student():
    """
    Allows deleting a student record by ID.
    """
    print("\n--- 4. Delete student ---")
    student_id = input("Enter the student's ID to delete: ")
    
    if student_id in students:
        student_name = students[student_id]['name']
        del students[student_id]
        print(f"\nStudent record for '{student_name}' successfully deleted!\n")
    else:
        print(f"\nError: No student found with ID '{student_id}'.")

def view_all_students():
    """
    Shows a list of all registered students with their average.
    Uses a for loop to iterate over the dictionary.
    """
    print("\n--- 5. List of all students ---")

    if not students:
        print("No students registered in the system.")
        return

    for student_id, student_data in students.items():
        avg = calculate_average(student_data['grades'])
        print(f"---------------------------------------------------")
        print(f"ID: {student_id}")
        print(f"Name: {student_data['name']}")
        print(f"Age: {student_data['age']}")
        print(f"Average grade: {avg:.2f}")
    print("---------------------------------------------------\n")

def show_menu():
    """
    Prints the options menu for the user.
    """
    print("\n" + "="*40)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Register student")
    print("2. Consult student")
    print("3. Update grades")
    print("4. Delete student")
    print("5. View all students")
    print("6. Exit")
    print("="*40)

# ==============================================================================
# MAIN PROGRAM FLOW
# ==============================================================================

def main():
    """
    Main function that runs the program loop.
    """
    while True:
        show_menu()
        option = input("Select an option (1–6): ")

        if option == '1':
            register_student()
        elif option == '2':
            consult_student()
        elif option == '3':
            update_grades()
        elif option == '4':
            delete_student()
        elif option == '5':
            view_all_students()
        elif option == '6':
            print("\nThank you for using the system. Goodbye!\n")
            break
        else:
            print("\nInvalid option. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
