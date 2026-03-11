name = input("enter a string")
palindromic = name[::-1]
if name == palindromic:
    print("palindromic")
else:
    print("not palindromic")