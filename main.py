import func_stuff
from unittest.mock import patch

# DO NOT TOUCH

def grade_input_func(func, num):
	for i in range(func_stuff.func_tests[num]):
		with patch('builtins.input', side_effect=func_stuff.func_inputs[num][i]):
			result = func()
			assert result == func_stuff.func_outputs[num][i], f"Expected {func_stuff.func_outputs[num][i]}, got {result}"
	print(func_stuff.func_flags[num])

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
"""
class func_stuff():
  func_inputs = {
	  1 : [[9,8,3,6,1,-4,2,1,6,8], [1,2,3,4,5,6,7,8,9,10], [0,0,0,0,0,0,0,0,0,0]],
  }

  func_outputs = {
	  1 : [[4], [5.5], [0]],
  }

  func_tests = {
	  1 : 3,
  }

  func_flags = {
	  1 : "pcssii_robotics{avg_of_10_a268b0f5c17c123f50}",
  }
"""
