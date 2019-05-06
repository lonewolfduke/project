print("Enter the value you are converting and leave the other column as 0 ")
cur1 = float(input("Dollar Enter here "))
cur = float(input("Naira Enter here "))
g = (cur1 * 358)
g2 = (cur / 358)
if cur1 > 0 and cur == 0:
 print ("N", g)
elif cur > 0 and cur1 == 0:
 print("$", g2)
elif cur1 > 0 and cur > 0:
 print("ERROR!!! You can only Compute one result at a time")