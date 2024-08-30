#100 pesos wii
#Exercise 1.1
amtmoney=float(input("How much money do you have ? "))
numWii=int(amtmoney/100)
needWii=100-(amtmoney%100)
print("You can only afford", numWii, "Nintendo Wiis""\nYou need",needWii ,"more pesos to afford another Nintendo Wiis")

#Exercise 1.2
factorial =int(input("Please enter a number: "))
factorialAns=1
for i in range(1, factorial+1):
    factorialAns=factorialAns*i
print("The factorial of", factorial, "is", factorialAns)

#Exersice 1.3
counter=0
factor=int(input("Enter a number dat you want to get the factors: "))
factorList=[]
for x in range(1,factor+1):
    if factor%x==0:
        #print(x, "is a factor of", factor,".")
        factorList.append(x)
        counter=counter+1
print("These are the factors of", factor, "\n",factorList)
print("Number", factor, "have", counter, "factors")