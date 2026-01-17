#String methods():
#1.Indexing : Positive & Negative Indexing
#Positive Indexing: It access characters from left starts from 0.
A = "Balaji Akula"
print(A[5])

#Negative Indexing: It Access Characters from Right.starts from -1.

A = "Balaji Akula"
print(A[-5])


#2. Slicing(): Range of Values and get a part of the string.

A = "Balaji Akula"
print(A[0:6:1])


#3. Split(): It is used to convert string to list.

A = "Pyhton Is Easy"
y = A.split()
print(y)

#4. Join(): It is used to convert list to string.

Names = ['Hello',' Welcome', ' to',' my', ' world']
print(''.join(Names))

#5. Upper(): it converts Lowercase to Upper case.

x = 'hi all good morning'
print(x.upper())

#6. Lower(): It converts Uppercase to Lowercase.

x = 'ROYALSBALAJI@GMAIL.COM'
print(x.lower())

#7.title(): It is used to make every single word first letter capital.

x = 'hi all good morning'
print(x.title())

#8. Capitallize(): It is used to make first word first letter capital.

x = 'hi all good morning'
print(x.capitalize())

#9. swapcase(): It converts upper to lower and lower to uppercase letters.

x = 'Hi aLl gOOd morNing'
print(x.swapcase())


#10.Replace(): It is used to replace one string to another string.

x = "Iam Learning Java"
print(x.replace('Java','Python'))

#Count(): It is used to count the values how many times oresent in the string or list.

X = 'Hellooo World'
Y = X.count('o')
print(Y)

#Index(): find the position of the value.
#rindex(): Access characters from right to left.


X= 'welcome to python world'
Y = X.rindex('p')
print(Y)


#Center(): it is used to make center of the string remaining filll other elements.

X = 'BALAJI'
Y = X.center(20,'*')
print(Y)

#format(): used to make default template with different values.

X = 'My name is {} & iam from {}'
Y = X.format('balaji','Kadapa')
print(Y)

#format_map(): It is used to map the existing dictionary values.


X = 'My name is {Name[1]} & I am from {City[0]}'
Y = {
    'Name': ['Balaji', 'Sai'],
    'City': ['Kadapa', 'Vontimitta']
}

Z = X.format_map(Y)
print(Z)

