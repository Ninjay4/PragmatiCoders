#!/usr/bin/env python
# coding: utf-8
'''
File Name: BasicCalculator
Created by: Ninjay4
Created on: 2/21/24
Modified on: 2/25/24
Description:  PractiCoders Python Challenge
Round 1 Practice Problem #3
Write a function that takes two numbers
And a mathematical operation
(add, subtract, multiply, division)
As parameters and returns the result of that operation
Hint: Use if-elif-else statements
To perform the operation based on the given string
'''

# Create 'calculator' Function
def calculator(num1, num2, operation):
    if operation == 'add':
        return (num1 + num2)
    elif operation == 'divide':
        return (num1 / num2)
    elif operation == 'multiply':
        return (num1 * num2)
    elif operation == 'subtract':
        return (num1 - num2)

# Create input parameters
num1 = int(input("Please enter the 1st number: "))
num2 = int(input("Please enter the 2nd number: "))
operation = input("Please enter the operation with only one of the following: 'add', 'divide', 'multiply', or 'substract' ")

# Run the calculator function
calculator(num1, num2, operation)

