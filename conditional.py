num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1>num2:
    print(num1,"is greater than",num2)
else:
    print(num2,"is greater than",num1)


choice = input("enter the choice (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): ")

if choice == '1':
    print (num1,"+",num2,"=",num1+num2)
elif choice == '2':
    print (num1,"-",num2,"=",num1-num2)
elif choice == '3':
    print (num1,"*",num2,"=",num1*num2)
elif choice == '4':
    print (num1,"/",num2,"=",num1/num2)
else:
    print("Invalid input")

        