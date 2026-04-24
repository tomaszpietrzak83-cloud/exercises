from time import sleep

# first version
for second in sorted(range(1, 4), reverse=True):
    print(second)
    sleep(1)
print("Start!")


# second better
for second in range(3, 0, -1):
    print(second)
    sleep(1)
print("Start!")
