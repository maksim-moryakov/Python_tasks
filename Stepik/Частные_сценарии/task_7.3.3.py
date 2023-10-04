"""
На вход программе подается натуральное число n.
Напишите программу, которая вычисляет значение выражения
"""
from math import log

n = int(input())
sm = 1
for i in range(2, n + 1):
    sm += (1 / i)
print(sm - log(n))