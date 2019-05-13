import math
a = int(input("Enter Value of a "))
b = int(input("Enter value of b "))
c = int(input("Enter value of c "))
if (a<0 or b<0 or c<0):
 print("Error!!! ")
bp2 = (b*2)
inp = ((bp2)-(4*a*c))
rt = math.sqrt(inp)
ans = ((-1*b)+(rt)/(2*a))
ans2 = ((-1*b)-(rt)/(2*a))
print (ans)