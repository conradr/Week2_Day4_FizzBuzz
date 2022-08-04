# class FizzBuzz:
#     def __init__(self):
#        pass

#
def divisible_by_3_and_5(number):
    if divisible_by_3_return_fizz(number) and divisible_by_5_return_buzz(number):
        return "FizzBuzz"
    elif divisible_by_3_return_fizz(number):
        return "Fizz"
    elif divisible_by_5_return_buzz(number):
        return "Buzz"
    else:
        return str(number)


def divisible_by_3_return_fizz(number):
    if number % 3 == 0:
        return True

def divisible_by_5_return_buzz(number):
    if number % 5 == 0:
        return True