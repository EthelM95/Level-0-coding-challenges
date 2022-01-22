def area_of_triangle(a, b, c):
    semiperimeter = 1/2*(a+b+c)
    print((semiperimeter*(semiperimeter-a)*(semiperimeter-b)*(semiperimeter-c)) ** 0.5)
    
area_of_triangle(3, 4, 5)
