<<<<<<< HEAD
import math
b = int(input("Enter Value of b "))
a = int(input("Enter Value of a "))
c = int(input("Enter Value of c "))
if(a<0 or b<0 or c<0):
    print ("out of range")
    exit()

bp2 = (b**2)
# ac = (29*4)
insq = ((bp2)-(4*a*c))

sqrt = math.sqrt(insq)
=======
b = -3
a = 1
c = -10
bp2 = (b**2)
ac = (29*4)
insq = ((bp2)-(4*a*c))
import math
sqrt = (math.sqrt(insq))
>>>>>>> bd5e0977437dfd8a000103bd7feb9a79112357c6
ans1 = ((-1*b)+sqrt)/(2*a)
ans2 = ((-1*b)-sqrt)/(2*a)
print(ans1, ans2)