k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

lambs = ['1'] * d
for i in range(1, d+1):
    if i % k == 0 or i % m == 0 or i % l == 0 or i % n == 0:
        lambs[i-1] = '0'
print(lambs.count('0'))