'''
    no=1   variable
    no=[]     list dynamic array
    dict={}   dict key value pair
    class --> object

    class :
            member variable (data)

            member defination (proccess)
eMPLOYEE
PRODUCT
tICKET

'''
class student:
    rollno=0
    name=""
    marks=""

student_list=[]
title=["Roll No:","Name:","Maths","Sci","Eng","Phy"]
for i in range(2):
    s1=student()
    s1.rollno=int(input("enter Roll no:"))
    s1.name=input("Enter Name :")
    s1.marks=[]
    for t in title[2:]:
       s1.marks.append(int(input("Enter "+t +" Marks:")))


    student_list.append(s1)

for s1 in student_list:
    print("Roll No:",s1.rollno)
    print("Name :",s1.name)
    is_pass=True;
    for t,m in zip(title[2:],s1.marks):
        print(t,m)
        if m<35:
            is_pass=False;

    if is_pass==False:
        print("you are Fail")
    else :
        total=sum(s1.marks)
        avg=total/len(s1.marks)
        print("total :",total)
        print("Avg :",avg)
        print("you are passed")











