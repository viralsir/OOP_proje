def introduction():
    print("this is a simple program")

def getInputs(principle,rate,time):
    principle = input("Enter the original principle: ")
    rate = input("Enter the yearly interest rate %")
    rate = float(rate) / 100.0
    time = input("Enter the number of years that money will be invested: ")
    return principle, rate, time

def calculate (principle, rate, time, interest, amount):

    interest = float(principle) * float(rate) * float(time)
    amount = float(principle) + interest
    return interest, amount

def display (principle, rate, time, interest, amount):
    temp = rate * 100
    print ("")
    print ("With an investment of $", principle, " at a rate of", temp, "%")
    print (" over", time, " years...")
    print ("Interest accrued $", interest)
    print ("Amount in your account $", amount)


principle = 0
rate = 0
time = 0
interest = 0
amount = 0
introduction()
principle, rate, time = getInputs (principle, rate, time)
interest, amount = calculate (principle, rate, time, interest, amount)
display (principle, rate, time, interest, amount)