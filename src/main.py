#esercizio 1

import math
a = 0.8
b = math.exp(a)
w = complex(a,b)
print(w)

for i in range(10):
  c = i * w
  print(c)

#print(type(w))

#esercizio 2

prv = "Oggi è s% %d %d" %("Venerdì",20,"Settembre")
print(prv)

name = "Peter"
my_string = "Hello my name is %s" %name
print(my_string)