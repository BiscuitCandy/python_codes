from plyer import notification
import time

#print(time.strftime('%a ::  %H:%M:%S :: %D', time.localtime()))

Ntfcts = {}

print("*"*100)
print("TODO LIST".center(100, "*"))
print("*"*100)

x = input("Enter Date separated by '/' in 'mm/dd/yy' format")
y = input("Enter time to be notified in 24h format\nExample: - 17:30")
z = input("Enter the heading of the Event")
a = input("Enter the message")

Ntfcts[x] = [y, z, a]