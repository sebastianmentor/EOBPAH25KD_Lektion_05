from students import Student, load_fake_students

def main():
    students:list[Student] = []
    load_fake_students(students)

    while True:
        print("1. Create student")
        print("2. List all students")
        print("3. Add course to student")
        print("0. Quit")

        choice = input("Enter choice:")

        if choice == "0": 
            break

        elif choice == "1":
            ...

        elif choice == "2":
            for student in students:
                print(f"Student id: {student.get_id()}")
                print(f"\tName:       {student.name}")
                print(f"\tSSN:        {student.get_ssn()}")
                print(f"\tStudent is: {'Active' if student.is_active else 'Inactive'}")
                print(f"\tCreated:    {student.created}")
                print(f"\tTakes course:")
                for course in student.get_courses():
                    print(f"\t\t{course}")

        elif choice == "3":
            ...

        else:
            print("Invalid choice! Try again NOOB!")


if __name__ == "__main__":
    main()