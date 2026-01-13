
#FUNCTIONS:
'''
1.It is a group of statements and block of code.
2.it will perform specific about task.
3.it is reusable.
4.we can write once and use many times.

TwoTypes:
- Built_in functions.
- User defined functions.
'''
#User defined functions: it is a customized function based on the user requirement
#user can create own function.


#student records

def name(Name,Marks):
    if Marks > 90:
        print(Name,':A Grade')
    elif Marks > 75:
        print(Name,':B Grade')
    elif Marks > 35:
        print(Name,':C Grade')
    else:
        print('Fail')
name('Balaji',37)
name('Sai',89)
name('Pranay',98)


# Login programme

def login():
    while True:
        user = input('Enter username:')
        password = int(input('Enter Password:'))
        if user=='Balaji' and password== 1234:
            print('Login successfully')
            break
        else:
            print('Login Failed')
login()
'''   
'''
def withdraw(balance):
    Amount = int(input('Enter Amount:'))
    if Amount <= balance:
        print('Cash withdraw:',Amount)
        print('Remaining Balance:',Amount-balance)
    else:
        print('Insufficient Balance')
        

withdraw(24000)


#Scopes:1.Global & Local Variables.
#1.Global Variable:
'''
- Global variable is a outside function.
- It can access anywhere inside and outside of the function.
'''
#2.Local Variable:

'''
- Local variable is a inside function.
- It can be access inside function only.
'''

a = 2
def add():
    global b
    b = 3
add()
print(a+b)

#local

def sub(a,b):
    print(a-b)
sub(3,5)


#Callback function():
#- One function passed into another function as an argument this is called callback function.
#- It automatically called once the main function completes its task.

#payment programme 

def payment(Callback):
    print('Payment Processing...')
    Callback()
def process():
    print('Payment completed Successfully')
payment(process)



def form(Callback):
    print('Form submitted')
    Callback()
def Show_message():
    print('Thanyou for submitting')
form(Show_message)


#Lambda Function():
'''
- Lambda function is a anonomous function.
- There is no function name.
- It is a single line expression.
- It is used for small & simple tasks in one line.
'''

#Lambda,paramaters:Statement
#Lambda map():
'''
- It is used to map the values.
- It applies a function to each item in a list and returns a new list.
'''
#Lambda Filter():
'''
- Selects elements from a list based on a condition.
'''
#Lambda Map():

li = [10,20,30,40]
a = list(map(lambda n:n*2,li))
print(a)

#Add Tax:using map()

Prices = [100,200,300,400]
add_tax = list(map(lambda n:n*1.18,Prices))
print(add_tax)

#Discount:using map()

prices = [100,300,400,600]
Discount = list(map(lambda n:n*0.9,prices))
print(Discount)


#Lambda Filter():

prices = [1000,2000,3000,4000,5000]
discount = list(map(lambda n:n*0.9 if n>3000 else False,prices))
print(discount)


numbers = ['8142103613','15645','2589631470']
valid = list(filter(lambda n:len(n) == 10,numbers))
print(valid)


