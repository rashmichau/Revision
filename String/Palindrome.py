# Check if string is symmetrical or palindrome

s = input("enter any string : ")
s=s.strip()
mid=len(s)//2
if(len(s)==0):
    print("enter a valid string!!!!!")
elif s[:mid]==s[mid:]:
    print("string is symmetric")
elif s==s[ : :-1]:
    print("string is palindrome")
else:
    print("not symmetric not palindrome")