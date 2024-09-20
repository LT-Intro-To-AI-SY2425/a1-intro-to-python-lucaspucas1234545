# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

def temp(input_temp, input_type):
    if input_type == "F":
        val = (input_temp - 32) * (5 / 9)
    else:
        val = (input_temp * (9 / 5)) + 32

    print(val)
    return val

assert temp(32, "F") == 0, "temp 32 degrees F"
assert temp(100, "C") == 212, "temp 0 degrees C"

def wordCounter(input_string):
    i = 0
    numWords = 1
    for char in input_string:
        i += 1
        if char == " ":
            numWords +=1
    
    return numWords

assert wordCounter("sho fidda bruh moment") == 4, "4 word string"
assert wordCounter("crazy") == 1, "1 word string"

def numGuesser(correct_num):
    guess = int(input("Enter your guess "))
    if guess == correct_num:
        return True
    else:
        return False
    