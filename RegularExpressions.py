
#REGULAR EXPRESSION:
'''
- It is used to match user and pattern.
- Regular expression is a sequence of characters that forms a search pattern.
'''
#Email:

import re
pattern =re.compile(r'^\w+\d\@\w+\.\w+$')
user = "royalsbalaji316@gmail.com"
if re.match(pattern,user):
    print('valid mail')
else:
    print("Invalid mail")


#Numbers:

import re
pattern =re.compile(r'^\w+\d\@$')
user = "balaji1223@"
if re.match(pattern,user):
    print("Valid")
else:
    print("Invalid")


import re
def Valid_aadhar(aadhar):
    pattern =r'^\d{12}$'
    return bool(re.match(pattern,str(aadhar)))
aadhars = [691804765420,225547854,332569874512,25874136945]
for a in aadhars:
    if Valid_aadhar(a):
        print(a,'is a valid aadhar number')
    else:
        print(a,'is a Invalid aadhar number')



import re
def Valid_Vehicleno(Vehicle):
    pattern =r'^\w{2}\d{2}\w{2}\d{4}$'
    return bool(re.match(pattern,Vehicle))
Vehicle = ['AP04UB1234','MP0AP323453','AP04CC2345']
for v in Vehicle:
    if Valid_Vehicleno(v):
        print(v,'is a valid Number')
    else:
        print(v,'is not Valid Number')





