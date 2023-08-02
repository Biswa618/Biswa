a= list(input("enter a list of values: "))
b= list(input("enter a list of values2: "))
a[0], a[2] = a[2], a[0]
b[0], b[4] = b[4], b[0]
print(a)
print(b)
