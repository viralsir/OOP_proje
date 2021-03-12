from lib_class import *

Customer_List=[]
op11=1
while op11 !=4:
    print("\t order ")
    print("\t1.Entry")
    print("\t2.View")
    print("\t3.Product Count:")
    print("\t4.Exit")

    op11=int(input("Enter Your option :"))

    if op11==1:
        op1="yes"
        while op1=="yes":
            c1=Customer()
            c1.id=int(input("Enter Customer Id:"))
            c1.name=input("Enter Customer Name :")
            c1.phno=input("Enter Customer PHno:")
            c1.address=input("Enter Customer Address:")
            c1.product_list=[]
            op="yes"
            while op.lower()=="yes":
                pr=Product()
                pr.id=int(input("Enter Product Id:"))
                pr.name=input("Enter Product Name:")
                pr.qty ,pr.rate=int(input("Enter Product Qty :")),float(input("Enter Proudct Rate :"))
                pr.price=pr.qty*pr.rate
                c1.product_list.append(pr)
                op=input("Do you want to add another product ?(yes/no):")

            total=sum([product.price for product in c1.product_list])
            if 0<total<5000:
                c1.discount=total*0.05
            elif 5000<total<10000:
                c1.discount = total * 0.10


            Customer_List.append(c1)
            op1 = input("do you want to add another bill?(yes/no):")

    elif op11==2:
        for c1 in Customer_List:
            print("Customer Id :",c1.id)
            print("Customer Name :",c1.name)
            print("Customer Address:",c1.address)
            print("Customer Phno:",c1.phno)
            print("Id \t Name \t Qty \t Rate \t Price")
            price_list=[]
            for product in c1.product_list:
                print(product.id,"\t",product.name
                      ,"\t",product.qty
                      ,"\t",product.rate
                      ,"t",product.price)
                price_list.append(product.price)

            #print("Bill Amount :",sum(price_list))
            #price_list2=[product.price for product in c1.product_list]
           # print("price_list:",price_list)
            #print("lamba list:",price_list2)
            print("Discount :",c1.discount)
            print("Gross Amount :",sum([product.price for product in c1.product_list ]))
            print("Bill Amount :",sum([product.price for product in c1.product_list])-c1.discount)


            print("======================")

    elif op11==3:
        total=0
        pname=input("enter product :")
        for c1 in Customer_List:
            for product in c1.product_list:
                if product.name==pname:
                   total=total+product.qty

        print("total Count of Product :",total)

    elif op11==4:
        print("you are exited ")
    else :
        print("wrong option selected try again !!")