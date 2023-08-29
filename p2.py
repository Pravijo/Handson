"""
a = input("enter number ")
b = input("enter number ")
c = input("enter number ")
d = input("enter number ")
e = input("enter number ")
f = input("enter number ")
g = input("enter number")
list = [a,b,c,d,e,f,g]
print(list)
l1 = list[:3]
print(l1)
l2 = list[-3:]
print(l2)
l3 = l1 + l2
print(l3)"""

l1 = [1,2,3,4,44,5,55,66,77,85,95]
last3 = []
for i in range(-1, -4, -1):
    last3.append(l1[i])
print(last3)

#listR = list(reversed(last3))  #reversed list in listR
#print(listR)