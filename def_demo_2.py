def total(no1,no2,no3=0):
    return no1+no2+no3
def sub(no1,no2):
    return no1-no2

i=int(input("Enter No1:"))
j=int(input("Enter No2:"))

print("total :",total(j,i))
print("total :",total(j,i,5))
#print("total :",total(j))
print("sub :",sub(no2=j,no1=i))