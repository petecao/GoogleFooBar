def solution(n):
	number = int(n)
	count = 0
	while number != 1:
		if number % 2 == 0:
			count += 1
			number /= 2
		elif number % 4 == 1 or number == 3:
			count += 2
			number -= 1
			number /= 2
		else:
			count +=2
			number += 1
			number /= 2
	return count