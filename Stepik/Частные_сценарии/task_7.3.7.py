# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет сумму всех его делителей.

number = int(input())
sum_of_divisors = 0

for i in range(1, number + 1):
    if number % i == 0:
        sum_of_divisors += i

print(sum_of_divisors)