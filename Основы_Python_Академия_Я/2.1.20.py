N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())
x = N * (K2 - M) / (K2 - K1)
y = N - x
print(int(x), int(y))
