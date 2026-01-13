#Loops

#1.For Loop
#2.While loop

# forloop: It is a single line expression / One line statement.
#          It Iterate each and every value.    

for i in range(1,10,1):
    print(i)


products = {'Laptop':35000,'Mobile':2000,'TV':13000}
for i in products:
    price = products[i]
    New_price = price + 200
    print(i,'New Price is',New_price)


#While loop: It execute repeatedly until condition is false.


password = int(input('Enter password:'))
while password == 1234:
    print('Login Successful')
    break
else:
    print('Login Failed Try Again')


password = 0

while password != 1234:
    password = int(input("Enter password: "))

print("Login Successful")


#Login Attemps

attemps = 0
while attemps < 3:
    password = int(input('Enter Password:'))
    if password == 1234:
        print('Login Successufully')
        break
    else:
        print('wrong Password')
        attemps +=1
else:
    print('Account Blocked')


products = {'HP':60000,'ACER':34000,'VICTUS':64000}
for i in products:
    price = products[i]
    New_price = price + 1500
    print(i,'NewPrice is',New_price)

