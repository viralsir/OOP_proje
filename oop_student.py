class student:
    rollno=0
    name=""
    maths=0
    sci=0
    eng=0

    def entry(self):
        self.rollno=int(input("Enter Roll No:"))
        self.name=input("Enter Student Name :")
        self.maths=int(input("Enter Maths marks:"))
        self.sci = int(input("Enter Sci marks:"))
        self.eng = int(input("Enter Eng marks:"))

    def view(self):
        print("Roll NO:",self.rollno)
        print("Name :",self.name)
        print("Maths :",self.maths)
        print("Sci :",self.sci)
        print("Eng :",self.eng)


student_list=[]
for i in range(2):
    s1=student()
    s1.entry()
    student_list.append(s1)

for s1 in student_list:
    s1.view()

#student_list[0].view()
#student_list[1].view()