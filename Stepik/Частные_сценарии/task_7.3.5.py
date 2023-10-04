# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет n!

n = int(input())
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(factorial)