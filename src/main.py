#esercizio 1

import math
a = 0.8
b = math.exp(a)
w = complex(a,b)
#print(w)

for i in range(10):
  c = i * w
  #print(c)

#print(type(w))

#esercizio 2

nome = "Peter"
my_string = "Hello my name is %s" %nome
#print(my_string)
my_string = "Hello %s , how are you? %s" %(nome, 'ok')
#print(my_string)

person = {"name": "John", "age": 19}
print(f"{person['name']} is {person['age']} years old")

my_string2 = "the rest is empty \n with no brain \n but the clever nerd \n the best MC with no chain \n that you evere heard"
print(my_string2)
print(my_string2[0:10])
