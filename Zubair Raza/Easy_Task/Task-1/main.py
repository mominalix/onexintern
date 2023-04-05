
# This is a function that divide tweo numbers.
def divide():
# here we gets the input fron user.
    dividend = int(input("enter the dividend :- "))
    divisor = int(input("enter the divisor :- "))
# the condition is applied.
    if divisor == 0:
        print("Error: Division by zero")
    else:
        c = dividend/divisor
    print("the divison of dividend/divisor  is = ", c) 
print(divide())
# here is the final result.


