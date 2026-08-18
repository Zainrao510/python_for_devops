
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input! Please enter a valid number.")


#Multiple exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


##finally block hamesha execute hota hai.    
try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Operation completed.")

#multiple exceptions ko ek hi line me handle karna
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")    



