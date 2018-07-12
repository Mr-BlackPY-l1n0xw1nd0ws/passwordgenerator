import string

from random import *
#startMenu
print("---------------------------------")
startMenu = (" password generator \n " +
             "made by: Mr.BlackPY \n "+
             "Wed Jul 11 ")
print(startMenu)
print("---------------------------------")

#password generator
def passgen():
    test = string.ascii_letters + string.punctuation + string.digits + string.hexdigits
    npass = "".join(choice(test)
                    for x in range(randint(10,20)))
    return npass

#Result
print("your password is:")
print(passgen())

#t.me/Mr_BlackPY
