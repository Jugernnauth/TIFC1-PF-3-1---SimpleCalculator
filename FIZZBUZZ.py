
#Presentar ejercicio FizzBuzz

for Num in range(1, 1001):
    if (Num % 3 == 0) and (Num % 5 == 0):
        print("Fizzbuzz")
    elif Num % 3 == 0:
        print("Fizz")
    elif (Num % 5 == 0):
        print("Buzz")
    else:
        print(Num)
