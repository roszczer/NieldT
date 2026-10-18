from math import exp
p = 100
r = .20
t = 2.0
#n = 12
n = 1000000
#a = p * (1 + (r/n))**(n * t)
a = (1 + (1/n))**n
print(a) # wypisuje 148.69146179463576
