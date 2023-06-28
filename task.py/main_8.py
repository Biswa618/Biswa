a= int(input("enter cost price: "))
b= int(input("enter selling price: "))
c= b-a
if(c>0):
    print("profit= ",c)
elif(c==0):
    print("neither profit nor loss")
else:
    print("loss= ",0-c)
    