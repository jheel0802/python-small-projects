import re

card = input("Enter the credit card number: ")
if re.findall('[4-6]\d{3}[-]\d{4}[-]\d{4}[-]\d{4}',card) and len(card) == 19:
    print("Valid card number")
elif re.findall('[4-6]\d{3}\d{4}\d{4}\d{4}',card) and len(card) == 16:
    print("Valid card number")
else:
    print("Invalid card number")