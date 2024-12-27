
print("Welcome to Rotimi's Student Grade Calculator")

print("===============================================")

student_data = {}   # dictionary for all students data


# here is the function for accpting list of subjects
def accept_subjects():
    while True:
        try:
            subjects = input("Enter the Subjects (Seperated by comma) : ")
            
            subjects = subjects.strip()  # this is to remoe the spaces in user response
            if not subjects:
                    print('Please try again, Enter a Subject')
                    continue
            student_data['subject'] = subjects.split(',')
            print("These are the list of subjects ", student_data['subject']) 
            break
        except:
            print('Wrong Input')





# let us take in the student names
def accept_student():
    students = input('Enter Student names (seperated with comma): ')
    student_data['students'] = students.split(',')
    print("These are the Students: ", student_data['students'])


# now lets accept the grades for each students 



def accept_grades(students, subjects):
    for student in students:
        grades= {}
        print(f"Enter grade for {student} :")
        print("Enter grade for {student}: ")
        for subject in subjects:
           try:
                studentGrade = int(input(f"Enter {student}'s grade for {subject} : "))
                grades[subject] = studentGrade
           except:
               print('Wrong Input')
        student_data[student] = grades


accept_subjects()
accept_student()
accept_grades(student_data['students'], student_data['subject'])
# print(student_data)