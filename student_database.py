class StudentDatabase:
    student_list=[]
    def add_student(self,student):
        self.student_list.append(student)

class Student:
    def __init__(self,student_id,name,department,is_enrolled=False):
        self.student_id=student_id
        self.name=name
        self.department=department
        self.is_enrolled=is_enrolled
    
    def enroll_student(self):
        if self.is_enrolled==False:
            self.is_enrolled=True
        else:
            print('The Student is already Enrolled')
           
    def drop_student(self):
        if self.is_enrolled==True:
            self.is_enrolled=False
        else:
            print('The Student is not Enrolled')


    def view_student_info(self):
        print(f'ID: {self.student_id}, Name: {self.name}, Department: {self.department}, Enrolleed: {self.is_enrolled}')

s1 = Student('S101','Toufiq','CST')
s2=Student('S102','Talukder','EEE')
s3=Student('S103','Yousuf','ME')
sdb=StudentDatabase()
sdb.add_student(s1)
sdb.add_student(s2)
sdb.add_student(s3)
while True:
    print('1. View All Students')
    print('2. Enroll Student')
    print("3. Drop Student")
    print("4. Exit")

    choice = input('Enter your choice (1-4) : ')

    if choice == '1':
        for student in StudentDatabase.student_list:
            student.view_student_info()

    elif choice == '2':
        flag=False
        id = input('Enter student ID to enroll: ')
        for student in StudentDatabase.student_list:
            if student.student_id == id:
                student.enroll_student()
                flag=True
                break
        if flag ==False:
            print('Invalid Student ID')
               
                

    elif choice == '3':
        flag=False
        id = input('Enter student ID to drop: ')
        for student in StudentDatabase.student_list:
            if student.student_id == id:
                student.drop_student()
                flag=True
                break
        if flag==False:
            print('Invalid Student ID')
            

    elif choice == '4':
        print('Exit')
        break

    else:
        print('Invalid choice')

