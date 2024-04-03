t = int(input())
for _ in range(t):
    n =input()
    s = [x for x in input()]
    if sorted(s) == sorted(['T','i','m','u','r']):
        print('YES')
    else:
        print('NO')