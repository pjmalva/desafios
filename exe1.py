import math

def solution(A, B):
    x = 0
    if A < 0:
        i = math.sqrt(A*-1)
        i *= -1    
    else:
        i = math.sqrt(A)
    
    while i**2 <= B:
        print(i, "=", i**2)
        x += 1
        i += 1
    return x

print(solution(-25, 25))