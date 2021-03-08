'''
    no=1   variable
    no=[]     list dynamic array
    dict={}   dict key value pair
    class --> object

    class :
            member variable (data)

            member defination (proccess)


'''
class student:
    rollno=0
    name=""
    maths=0
    sci=0
    eng=0
    phy=0

student_list=[]
for i in range(2):
    s1=student()
    s1.rollno=int(input("enter Roll no:"))
    s1.name=input("Enter Name :")
    s1.maths=int(input("Enter Maths marks:"))
    s1.eng=int(input("Enter English marks:"))
    s1.sci=int(input("Enter Science marks:"))
    student_list.append(s1)

for s1 in student_list:
    print("Roll No:",s1.rollno)
    print("Name :",s1.name)
    print("Maths :",s1.maths)
    print("Science:",s1.sci)
    print("Eng :",s1.eng)
    if s1.maths<35 or s1.sci<35 or s1.eng<35:
        print("you are Fail")
    else :
        print("you are passed")











