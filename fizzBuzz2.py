b = int(input("Enter the value: "))
def fizzbuzz(b):
    if (b % 3 == 0) and (b % 5 == 0):
        return ("FizzBuzz")   


    elif b % 3 == 0:
        return ("Fizz")

    elif b % 5 == 0:
        return ("Buzz")

    else:
        return b

if b == 0:
    print("Cannot be 0 please try again!")
else:    
    print(fizzbuzz(b))






