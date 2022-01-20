import math
def area_of_triangle(a, b, c):
    s = 1/2*(a+b+c)
    print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    
area_of_triangle(3, 4, 5)
