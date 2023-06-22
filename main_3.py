a= int(input("enter A value: "))
b= int(input("enter B value: "))
c= int(input("enter C value: "))

if(a>b and a>c):
    print("A is maximum")
elif(b>c):
    print("B is maximum")
else:
    print("C is maximum")