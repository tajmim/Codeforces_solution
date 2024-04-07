n = int(input())
t =0
for i in range(n):
    s = [int(x) for x in input().split()]
    if s.count(1) >= 2:
        t+=1
print(t)