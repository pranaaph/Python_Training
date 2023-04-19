import re
passwrd=input("Enter a password: ")
length = len(passwrd)
if not (length>=8 and length<=16):
     flag=0
elif not re.search("[a-z]",passwrd):
     flag=0
elif not re.search("[A-Z]",passwrd):
     flag=0
elif not re.search("[0-9]",passwrd):
     flag=0
elif not re.search("[$#@]",passwrd):
     flag=0
else:
    flag=1

if(flag==1):
    print("Its Valid")
else:
    print("Its not Valid")