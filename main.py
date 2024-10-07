import grader 
from unittest.mock import patch

"""

Welcome! Today's challenge is to write a program that asks a person for 10
numbers and takes the average of them, returning it.

A successful program prints a flag in the form of:

pcssii_robotics{code_clash_name_384e67a7c83b2b}
  code_clash_name will be the challenge name
  the numbers will be random (obviously)

Get coding!

"""

def avg_of_10():
  # code goes here
  sum = 0
  for i in range(10):
    sum += int(input("Enter a number: "))
  avg = sum / 10
  return avg


# Nothing under here, DO NOT EDIT
grade_input_func(avg_of_10,1)
