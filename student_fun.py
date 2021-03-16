from student_api import *

title=["Roll No","Name","Maths","English","Science"]
data=getinput(title)

display(title,values=data)
if is_pass(marks=data[2:])==True:
    print("you are passed")
else :
    print("you are failed")



