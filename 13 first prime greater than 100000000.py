def is_prime(n):
    if n < 2:
        return False
    for i in range(2, (int(n**0.5) + 1)):
        if n % i == 0:
            return False

    return True


counter = 100000000


while True:
    if is_prime(counter):
        print(counter)
        break
    lastDigit = counter % 10
    match lastDigit:
        case 1, 7, 5, 9:
            counter += 2
        case 3:
            counter += 4
        case 0, 2, 6, 8:
            counter += 1
        case _:
            counter += 3
