Username = "Rakshana"
Password = "123"

uname = input("Enter the username: ")
pword = input("Enter the password: ")

def UnamePasswrd():
    if (uname == Username and pword == Password):
        return True
    else:
        return False
a=UnamePasswrd()
print(a)
