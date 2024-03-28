n,k,l,c,d,p,nl,np = [int(x) for x in input().split()]
drink_of_each_frnd = k * l / n
lime_slics_of_each_frnd = c * d /n
salt_of_each_frnd = p/n

possible_toast_from_drinks = drink_of_each_frnd //nl
possible_toast_from_lime = lime_slics_of_each_frnd//1
possible_toast_from_salt = salt_of_each_frnd//np

arr = [possible_toast_from_drinks , possible_toast_from_lime , possible_toast_from_salt ]

arr.sort()

print(int(arr[0]))
 