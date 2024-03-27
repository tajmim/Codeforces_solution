n = input()
opinions = input().split()
hard_opinions = opinions.count('1')

if(hard_opinions > 0):
    print('HARD')
else:
    print('EASY')