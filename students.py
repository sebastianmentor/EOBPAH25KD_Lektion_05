from datetime import date

class Student:
    def __init__(self, 
                 student_id:int, 
                 name: str, 
                 ssn: str,
                 created: date = None,
                 is_active:bool = False,
                 courses: list[str] = None):
        
        self._id = student_id
        self.name = name
        self._ssn = ssn
        self.created = created or date.today() 
        self.is_active = is_active
        self._courses = courses or []

    def party(self) -> None:
        print(self.name, "Goint to a party!!!")

    def get_ssn(self) -> str:
        return self._ssn

    def get_id(self) -> int:
        return self._id
    
    def get_courses(self) -> list[str]:
        return self._courses.copy()

    def takes_course(self, course:str) -> bool:
        return course in self._courses
    
    def add_new_course(self, course:str) -> None:
        if self.takes_course(course):
            raise ValueError(f"Allready taking this course {course}")
        
        self._courses.append(course)


def load_fake_students(students:list[str]) -> None:
    students.extend([
    Student(1, "Kalle Anka", "19990101-1234", date(1999, 1, 1), courses=["Math", "Programming"]),
    Student(2, "Nisse Banan", "19890101-2342", date(2003, 1, 1), is_active=True),
    Student(3, "Göran Apa", "20100101-8888", date(1999, 1, 1)),
    Student(4, "Anna Anka", "20201101-4408", date(2023, 1, 1), is_active=False),
    Student(5, "New student", "20201101-8321", courses=["Filosofy", "Geogrofi"])
    ])




if __name__ == "__main__": 
    # vi kör bara den här if-satse om det är den här filen vi börjar med
    # Importeras den här filen så kommer inte den här koden att köras!
    print("Inside if __name__ in students.py")
    while True:
        print("Mitt andra menyprogram!")
        if "q" == input("Enter somtehing"): break

    s1 = Student(1, "Kalle Anka", "19990101-1234", date(1999, 1, 1), courses=["Math", "Programming"])
    s2 = Student(2, "Nisse Banan", "19890101-1234", date(2003, 1, 1), is_active=True)
    s3 = Student(3, "Kalle Anka", "19990101-1234", date(1999, 1, 1))
    s4 = Student(4, "Anna Anka", "20201101-1234", date(2023, 1, 1), is_active=False)
    s5 = Student(5, "New student", "20201101-1234", courses=["Filosofy", "Geogrofi"])

    print(s1._courses) # så här ska vi inte göra! Ser vi _variabelnamn så ska vi inte accessa den!
    print(s5._courses) # -- || --


    # s2.courses.append("Chemistry")
    # print(s3.courses)
    # s3.courses.append("Cooking class")
    # print(s2.courses)