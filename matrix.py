import random

def matrix(l, c):
	return [[random.randint(1,99) for j in range(c)] for i in range(l)]

def smaller_line(matrix):
	s = []
	for line in matrix:
		s.append(min(line))
	return s

def smaller_matrix(matrix):
	return min(smaller_line(matrix))	

m = matrix(5, 5)
print(m)
print(smaller_line(m))
print(smaller_matrix(m))
