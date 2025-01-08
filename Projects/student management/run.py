


print('++++++++++++++++++++++++=======================+++++++++++++')
print('Welcome to the Student Management system.')
print('You can add, delete, update and display students.')

studentName = input('Enter the Student Name: ')
studentAge = input('Enter the Student age: ')
studentGrade = input('Enter the Student grade: ')
studentFavSubjects = input('Enter the Student favourite subjects: ')

# students = dict()
class Student():
    def __init__(self, name, age, grade, FavSubject):
        
        self.name = name
        self.age = age
        self.grade = grade
        self.FavSubject = FavSubject

        


class studentManager() :
    def __init__(self) :
    
        self.students = []
        
    def add_student(self, name, age, grade, FavSubjects):
        
    
        student = Student(name, age, grade, FavSubjects)
        self.students.append(student)

    def viewStudents(self):
        for student in self.students :
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.FavSubjects}")

            print(student)

manager = studentManager()

manager.add_student(studentName, studentAge, studentGrade,  studentFavSubjects)

