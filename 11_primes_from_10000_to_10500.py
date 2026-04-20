# Provide a script that print every prime number in the range [10000;10050], on one line, separated by comas and spaces.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, (int(n**0.5) + 1)):
        if n % i == 0:
            return False

    return True


primes = []
for n in range(10000, 10051):
    if is_prime(n) is True:
        primes.append(str(n))

primesString = ", ".join(primes)

print(primesString)
