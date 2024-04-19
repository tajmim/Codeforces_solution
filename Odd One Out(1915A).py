for _ in range(int(input())):
    arr = [int(x) for x in input().split()]
    arr.sort()
    if(arr[0]==arr[1]):
        print(arr[2])
    else:
        print(arr[0])    


