for i in range(int(input())):
    a,b,c = [int(x) for x in input().split()]
    if (a + b == c) or (a + c == b) or (b + c == a):
        print("YES")
    else:
        print('NO')