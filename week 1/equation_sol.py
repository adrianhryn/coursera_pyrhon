import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print("Your equation is {}x^2 {}x {}".format(a, b, c))

d = (b**2 - 4*a*c)**(1/2)

x_1 = (-b - d)/(2*a)
x_2 = (-b + d)/(2*a)

print("x1 is {} and x2 is {}".format(int(x_1), int(x_2)))