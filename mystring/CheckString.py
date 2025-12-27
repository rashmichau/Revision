# Check if string has a letter and number
# input : rashu123
# output :True
s  =input("Enterany string :")
has_letter = any(c.isalpha() for c in s)
has_number = any(c.isdigit() for c in s)

print(has_letter and has_number)


