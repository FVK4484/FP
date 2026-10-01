from math import sqrt

def perimetro (a,b,c):
    return a + b + c

def area_por_heron (a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return None
    else:
        p = perimetro(a, b, c)
        s = p/2
        area = sqrt(s*(s-a)*(s-b)*(s-c))
        return area

