# Check if a string contains any special character
# input : raam123@
# output : string contain special char
s= input("enter any string : ")
if s.isdigit():
    print("contain only digits :True")
elif s.isalpha():
    print("contain only char :True")

elif s.isalnum():
    print("contain both charand digits :True")
else:
    print("string contain special char also")
