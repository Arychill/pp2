import math

def degree_to_radian(deg):
    rad = math.radians(deg)
    return rad

a = int(input("Input degree: "))
print(f"Output radian: { '%.6f' % degree_to_radian(a)} \n")

def area_trapezoid(h, a, b):
    area = (a + b) / 2 * h
    return area

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
print(f"Expected Output: {'%.1f' % area_trapezoid(h,a,b)} \n")

def area_polygon(n, l):
    p = n * l
    a = l / (2 * math.tan(math.radians(180/n)))
    area = (p * a) / 2
    return area
n = float(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
print(f"The area of the polygon is: {'%.1f' % area_polygon(n,l)} \n")

def area_parallelogram(l, h):
    area = l * h
    return area
l = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
print(f"Expected Output: {'%.1f' % area_parallelogram(l,h)}")