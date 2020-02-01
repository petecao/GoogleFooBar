def solution(l):
	memory = [0] * len(l)
	count = 0
	for i in range(len(l)-1):
		for j in range(i+1,len(l)):
			if l[j]%l[i] == 0:
				memory[j] += 1
				count += memory[i]
	return count