def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, (int(n**0.5) + 1)):
        if n % i == 0:
            return False

    return True


def sumOfPrimes(maximumNumber):
    sum = 0
    for number in range(1, maximumNumber + 1):
        if is_prime(number):
            sum += number
    print(sum)
    return sum


sumOfPrimes(4)
sumOfPrimes(7)
sumOfPrimes(11)
sumOfPrimes(25)
sumOfPrimes(100)
sumOfPrimes(125)
