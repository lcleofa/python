# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:12:40 2019

@author: 862903

short cuts:
ctl + space : code completion
snippets: ???

Ref:
http://apmonitor.com/che263/index.php/Main/PythonBasics
Debug mode
restart kernel [consoles...restart kernel]
"""

myVarF = 4.0
myVarI = 3

myVar = 2 + (5*3)

myVarB = True

myVarB2 = (myVarI > 4)

if (myVar < 15):
    print('myVar is greater')
else:
    print('myVar is smaller')


"""    
#example reserved words marked in blue
from random import *
answer = randint(0,10)
correct = False
while not(correct):
    guess = int(input("Guess a number (0-10): "))
    if guess < answer:
        print("Too low")
    elif guess > answer:
        print("Too high")
    else:
        print("Correct!")
        correct = True    

"""
    
#object
x=2            # create variable 'x'
print(x)       # print value     => 2
print(id(x))   # print id number => 1737348944
print(type(x)) # print type      => <class 'int'>

#data types
x=2             # integer
y=2.02          # float
z='3'           # string
print(str(x)+z) # 23
print(x+int(z)) # 5

a=[x,y,z]       # list
print(a[1])     # 2.02

b=(x,y)         # tuple
print(b[1])     # 2.02

c={'m':7,'n':8} # dictionary
print(c['m'])   # 7

#Math Expressions
import math
x=3.1415
print(math.sin(x)) # 9.265e-05

#Numpy math module
import numpy as np
x=np.pi
print('\nnp.pi =  ')
print(math.sin(x))  # 1.225e-16

#Strings
first = 'Tom'
last = "Smith"
name = first + ' ' + last
print(name + '\n')  # Tom Smith

#comments
hashtag = '#learnpython'
print('\n' + hashtag) # prints: #learnpython

#newline with escape sequence
flight = 'Landing at\n O\'Hare International Airport\n'
print(flight)
# prints:
# Landing at
#  O'Hare International Airport

#raw string
flight2 = r'Landing2 at\n O\'Hare International Airport'
print(flight2 + '\n')
# prints:
# Landing at\n O\'Hare International Airport


# import the number pi
import numpy as np
x = np.pi

# format pi
print(str(x))              # 3.141592653589793
print('{:.2f}'.format(x))  # 3.14
print('{:.10f}'.format(x)) # 3.1415926536
print('{:.5e}'.format(x))  # 3.14159e+00
print('{:.3%}'.format(x))  # 314.159%









