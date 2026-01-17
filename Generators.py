
# GENERATORS:

'''
- It is a special type of function that uses yield instead of return.
- produce values once at a time.
- It does'nt store all values at a once.
#return():It will return only one value.
#iter():It iterate existing generator object.
#next(iter_value): used to generate the values.
'''

#Two Types:
'''
1.Inifinte Generator():

2.Custom Generator():
'''
#Infinite Generator(): An infinite generator produces values without ending.
#Rapido Ride programme:


import time
def Ride():
    newbooking = 1000
    while True:
        yield f'New Ride - {newbooking}'
        newbooking +=1
        time.sleep(2)
x = Ride()
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))


#Orders Programme:

def order():
    ID = 1
    while True:
        yield f'Order_ID - {ID}'
        ID +=1

x = order()
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))




import time
def otp():
    First = 1
    while True:
        yield f'Otp - {First}'
        First +=1
        time.sleep(2)
x = otp()
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

#Custom_genereators(): It generates fixed sequences of values based on user requirements.

#TicketGenerator programme:


import time
def ticket(start,end):
    while start <=end:
        yield f'Ticket:{start}'
        start +=1
        time.sleep(2)
for tickets in ticket(1,5):
    print(tickets)



import random
import time
def otp(start,end):
    while start <= end:
        yield random.randint(1000,2000)
        start +=1
        time.sleep(2)
for otps in otp(1,7):
    print(otps)



def ride(start,end):
    while start <=end:
        yield f'Ride:-{start}'
        start +=1
x = ride(1,4)
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

def Ride():
    start = 1
    while True:
        yield f'Ride:-{start}'
        start +=1
x = Ride()
y = iter(x)
print(next(y))

