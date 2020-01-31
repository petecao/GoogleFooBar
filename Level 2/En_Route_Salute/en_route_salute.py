def solution(s):
	right_employees = 0
	salutes = 0
	for employee in s:
		if employee == ">":
			right_employees+=1
		elif employee == "<":
			salutes+= (right_employees*2)
		else:
			pass
	return salutes