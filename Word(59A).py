s = input()
u , l = 0 ,0
for i in s:
    if i.islower() == True:
        l +=1
    else:
        u +=1
if l >= u:
    print(s.lower())
else:
    print(s.upper())