PASSING_MARKS=33

def isvalid(value,subject):
    while not (0<=value<=100):
        value=int(input("Enter "+subject+":"))
    return value

def getinput(title):
    values=[]
    for t in title[:2]:
        values.append(input("Enter " + t + ":"))
    for t in title[2:]:
        mark=int(input("Enter "+t+":"))
        mark=isvalid(mark,t)
        values.append(mark)
    return values;
def is_pass(marks):
    for m in marks:
        if m<PASSING_MARKS:
            return False;
    return True;


def display(title,values):
    for t,v in zip(title,values):
        print(t,v)