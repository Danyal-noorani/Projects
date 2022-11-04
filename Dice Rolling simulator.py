import  random


sides = int(input("Enter Number of sides: "))
rolls = int(input("Enter number of rolls: "))

numbers = []
times = {}

for i in range(rolls):
    number = random.randint(1,sides)
    number =str(number)
    numbers.append(number)

for i in numbers:
    times[i] = numbers.count(i)

print(times)
