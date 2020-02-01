def solution(l):
	versionsList = sorted(l, key=lambda v: list(map(int, v.split('.'))))
	return ",".join(versionsList)