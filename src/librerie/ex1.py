import numpy as np
#arrays
b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum " ,b,"+",c, "= ", b+c)
b+=1
print("Autoincrement b +=1 b=", b)
print("Multiply c*3 " ,c, "* 3= ",c*3)
print("Sin (c)", np.sin(c))

#slicing
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0][0])
print(a[:,1])
print(a[0,:])
print(a[2:,1:3])