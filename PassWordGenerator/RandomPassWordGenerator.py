# import Random module for sampling and length
import random

# define the requirements of the password
small = 'abcdefghijklmnopqrstuvwxyz'
capital = small.upper()
numbers = '1234567890'
symbols = '_!@#$%^&*+-><'

# Create a rondom password from above data
password = "".join(random.sample("".join([small, capital, numbers, symbols]), random.randrange(8,16)))

#print the password
print("The Random password Generated is : {0}".format(password))

#Store the password in a file 'passwords.txt'
with open(r"C:\Users\VIVEK VR\Documents\Python\PassWordGenerator\passwords.txt", 'a') as f:
    f.write('\n')
    f.write(password)

#Program completed