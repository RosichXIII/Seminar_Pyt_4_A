# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import random
import math
number = random.randint(1, 1000)
print(number)
prime_factors = []
if number == 1:
    prime_factors.append(number)
else:
    for i in range(2, int(math.sqrt(number)) + 1):
        while (number % i == 0):
            prime_factors.append(i)
            number //= i
    if (number != 1):
        prime_factors.append(number)
print(prime_factors)