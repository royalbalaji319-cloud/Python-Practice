#Exceptional handling:
'''
- It is used to handles the errors.
- Run time errors it will handle.
- Try,Except,else,finally by using these blocks we can handle the errors.

try: Block of code we can pass n number of statements.
Except: We can handles the error.
else:if try any error except will be executed.
      if try no error else will be execute.
finally:it is a common operation we r using finally.
'''

#ValueError: - It Occurs when we enter text instead of numbers.
#ZeroDivisionError: -It occurs divide a number by zero.
#TypeError: -try to use two different datatypes together in wrong way.
#IndexError: -try to access something does'nt existing in a list.
#NameError: -NameError Occurs when we use variable or function that is not defined.


#ZeroDivisionError:It occurs divide a number by zero
try:
    x=10
    y=0
    print(x/y)
except ZeroDivisionError:
    print('0 Not divisible 10')

#ValueError:when we enter text instead of numbers.

try:
    age = int('twenty')
except ValueError:
    print('Age defined only numbers')



#TypeError:try to use two different datatypes together in wrong way.

try:
    x = 'twenty'
    y = 30
    print(x+y)
except TypeError:
    print('Not use string and int in same function')


#IndexError:try to access something does'nt existing in the list.

try:
    Names =['Balu','Sai']
    print(Names[2])
except IndexError:
    print('Data Not Found')


#NameError:When we use variables or functions that is not defined.
try:
    print(x)
except NameError:
    print("Name not defined")

try:
    Names=['Balaji','Sai']                              #IndexError
    index=int(input('Enter Index_Name:'))   #ValueError
    print(Names[index])
    
    count=int(input('Enter Team count:'))#ZeroDivisionError
    print(1000/count)

    bouns='300'
    print(bonus+2000)                     #TypeError

    #print(manager)                         #NameError
except ValueError:
    print("Please enter numbers only")

except IndexError:
    print("Employee record not found")

except ZeroDivisionError:
    print("Team count cannot be zero")

except TypeError:
    print("Input format mismatch")

except NameError:
    print("Variable not defined")

finally:
    print("Process completed")

