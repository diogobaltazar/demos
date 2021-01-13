number = 0

for number in range(10):
    if number == 5:
        break
    print(str(number))

print('break out')

number = 0

for number in range(10):
    # the program runs exactly as it would if there were no conditional
    # statement
    if number == 5:
        pass
    print(str(number))

print('pass out')

number = 0

for number in range(10):
    # jump to the next iteration
    if number == 5:
        continue
    print(str(number))

print('continue out')