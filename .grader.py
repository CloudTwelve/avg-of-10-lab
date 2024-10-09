from unittest.mock import patch

# if you found this file, submit the flag as well as pcssii_robotics{I_DID_IT}
# nice job!

def grade_input_func(func, num):
	for i in range(func_tests[num]):
		with patch('builtins.input', side_effect=func_inputs[num][i]):
			result = func()
			assert result == func_outputs[num][i], f"Expected {func_outputs[num][i]}, got {result}"
	print(func_flags[num])


func_inputs = { 
	1 : [[9,8,3,6,1,-4,2,1,6,8], [1,2,3,4,5,6,7,8,9,10], [0,0,0,0,0,0,0,0,0,0]],
  }

func_outputs = {
	1 : [4, 5.5, 0],
  }

func_tests = {
	1 : 3,
  }

func_flags = {
	1 : "flag_robotics{avg_of_10_a268b0f5c17c123f50}",
  }
