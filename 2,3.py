def f(a,b,D):
    if D >= 0:
        return [(D**0.5) - b/2*a],[-(D**0.5) - b/2*a]
    if D < 0:
        print('error')

a = int(input())
b = int(input())
c = int(input())
#t = a*x**2 + b*x +c
D = b**2 - 4*a*c
print(f(a,b,D))
