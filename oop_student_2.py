class student:
    rollno=0
    name=""
    marks={"Maths":0,"Sci":0,"Eng":0,"Phy":0}

    def entry(self):
        self.rollno=int(input("Enter Roll No:"))
        self.name=input("Enter Student Name :")
        for k in self.marks:
            #self.marks[k]=int(input("Enter "+k + "Marks:"))
            self.marks.__setitem__(k,int(input("Enter "+k+" Marks:")))

    def view(self):
        print("Roll NO:",self.rollno)
        print("Name :",self.name)
        for k,v in self.marks.items():
            print(k,v)

class Div :

    def __init__(self,name,list):
        self.divname=name
        self.studentlist=list



div_A=Div(name="A",list=[])
div_B=Div(name="B",list=[])



student_list=[]
for i in range(2):
    s1=student()
    s1.entry()
    #if "A":
    #div_A.student_list.append(s1)

for s1 in student_list:
    s1.view()



#student_list[0].view()
#student_list[1].view()