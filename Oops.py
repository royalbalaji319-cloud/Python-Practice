())
'''


#OOPS :
'''
- Object Oriented Programming System
- It allows to structure of the code using class and object for better organization.
'''
#1.Class & Object



class Student:
    def __init__(self, marks, grade):
        self.marks = marks
        self.grade = grade

    def show_marks(self):
        print(f"Marks: {self.marks}")

    def show_grade(self):
        print(f"Grade: {self.grade}")

obj = Student(30, 'D')

obj.show_marks()
obj.show_grade()

obj1 = Student(90, 'A')

obj1.show_marks()
obj1.show_grade()

# Inheritance:

'''
- One class derived from another class.
'''
# single Inheritance: Parent Class derived inside child class.

class vehicle:
    def start(self):
        print('Vehicle is starting....')
    def car(vehicle):
        print('Car is going....')
obj = vehicle()
obj.start()
obj.car()


#MultiLevel Inheritance: Parent class derived inside child class like a chain.


class person:
    def speak(self):
        print('Person speak the team...')
class Employe(person):
    def work(self):
        print('Employe works the team...')
class Manager(Employe):
    def manage(self):
        print('manager manges the team...')

obj = Manager()
obj.speak()
obj.work()
obj.manage()


#Multiple Inheritance: Multiple parent class single child class.

#  classA -> classB -> classC(B)


class vehicle:
    def vehicletype(self):
        print('Car')
class payment:
    def paymentMode(self):
        print('UPI')
class Ride(vehicle,payment):
    def ridestatus(self):
        print('Ride Confirm..')

obj=Ride()
obj.vehicletype()
obj.paymentMode()
obj.ridestatus()


#Hirachical Inheritance: Single Parent class and Multiple child class.

class animal:
    def sound(self):
        print('Animal Sound..')
class dog(animal):
    def bark(self):
        print('dog Barking..')
class cat(animal):
    def mewo(self):
        print('Cat meow...')
obj=cat()
obj.sound()
obj.mewo()

obj=dog()
obj.sound()
obj.bark()
