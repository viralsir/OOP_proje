'''
Inheritance : - is the proccess by which object of one class
can access or get the properties of objects of another class.

A   a1
B   b1
 a1  -->
 b1
1) Single Inheritance : one object access or get the properties of
only one object at a time.
        A
        |
        B

2)Multilevel Inheritance : continous chain of single inheritance

            A
            |
            B
            |
            C   c1

3) Hyrarchical Inheritance : more than one object access the properties of
same object

                  A
            |           |
            B           C

4) Multiple Inheritance : one object can access the properties of more than one
object at a time.

               A      B
                  |
                  C

5)Hybrid Inheritance : combination of more than one inheritance is hybrid inheritance

                   Personal_Info
                        |
            student         teacher
                       |
                     School


'''
class Personal_Info:
    name=""
    address=""
    phno=""

    def setPersonal_Info(self):
        self.name=input("Enter Name :")
        self.address=input("Enter Address:")
        self.phno=input("Enter Phno:")

    def getPersonal_Info(self):
        print("Name :",self.name)
        print("Address:",self.address)
        print("PhNo:",self.phno)


class Student(Personal_Info):
    rollno=""
    std=""
    div=""

    def setStudent(self):
        self.setPersonal_Info()
        self.rollno=int(input("Enter Student Roll No:"))
        self.std=int(input("Enter Std :"))
        self.div=(input("Enter Div:"))

    def getStudent(self):
        self.getPersonal_Info()
        print("Roll No:",self.rollno)
        print("STd:",self.std)
        print("Div :",self.div)


class Teacher(Personal_Info):
    subject=""
    salary=""

    def setTeacher(self):
        self.setPersonal_Info()
        self.subject=input("Enter Subject :")
        self.salary=int(input("Enter Salary :"))

    def getTeacher(self):
        self.getPersonal_Info()
        print("Teacher Subject :",self.subject)
        print("Teacher Salary :",self.salary)

class School(Student,Teacher):
    sname=""
    board=""

    def setSchool(self):

        self.sname=input("Enter School Name :")
        self.board=input("Enter School Board:")

    def getSchool(self):
        print("School Name :",self.sname)
        print("School Board:",self.board)


s1=School()
t1=Teacher()
s1.setStudent()
t1.setTeacher()
s1.setSchool()

print("output:")
s1.getStudent()
t1.getTeacher()
s1.getSchool()

