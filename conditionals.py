# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:48:00 2019

@author: 862903
"""

from random import *
answer = randint(0,100)
correct = False
while not(correct):
    guess = int(input("Guess a number: "))
    if guess < answer:
        print("Too low")
    elif guess > answer:
        print("Too high")
    else:
        print("Correct!")
        correct = True
