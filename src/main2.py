#esercizio 2

import math
import time

#LISTE

a = [0,3,5,12,54,78]
#print(a[0:2],a[2:],a[0::2], a[6:0:-2])

b = list(range(50))
#print(b[5])
b = list(range(0,50,7))
#for i in b:
  #print(i)

a = range(10)
b = [el*2 for el in a]

#for i in b:
  #print(i)

l = [1,2]
l2 = ['a','b']
l3 = [4,5]

f = [(e1,e2,e3) for e1 in l for e2 in l2 for e3 in l3]

#for i in f:
  #print(i)

my_list = []
for i in range(0,10):
  my_list.append(2**i)

my_list.insert(10,2**10)
#print(my_list)
my_list.extend(l3)
#print(my_list)
my_list.pop(len(my_list)-1)
#print(my_list)
my_list.pop(len(my_list)-2) #elimina l'oggetto all'indice dato
#print(my_list)
my_list.remove(64) #rimuove l'oggetto dato
#print(my_list)

#efficiency
#l = list(range(10000000))
#v = list(range(10000))
#T1 = time.perf_counter()
#s=l+v
#T2 = time.perf_counter()
#print(T2-T1)
#T3 = time.perf_counter()
#l.extend(v)
#T4 = time.perf_counter()
#print(T4-T3)

stack = [1,2,3,4]
print('Initial stack: ', stack)
for i in range(5,7):
  stack.append(i)
print('Append: ', stack)
stack.pop()
print('Pop: ', stack)

queue = ['a','b','c','d']
print('initial queue: ', queue)
queue.append('e')
queue.append('f')
print('Append: ', queue)
queue.pop(0)
print('pop: ', queue)

#TUPLE
tup1 = 'a','b','c'
tup2 = (1,2,3,4,5)
tup3 = ('a', 3)

del(tup1)
print(tup2[2])
print(('de','Pefforza')*15)

print(('bella')+('ciao'))

#DIZIONARI

my_dict = dict({'key1': 9, 'key2':7, 'key3':98})
my_dict = dict([('key1','znego'),('key2', [0,1,2])])
print(my_dict['key1'])
print(my_dict.get('key2'))
my_dict['key3'] = (1,2,3)
my_dict.pop('key2')
del(my_dict['key1'])
my_dict.clear()
print(my_dict)

#controlo flow

x = 45.
y = 0.5
while (x > 3):
  y = y + x*y
  print('x: ', x, 'y: ', y)
  x = x/3.
  if (y>x):
    break

else: y = 0.

print('x: ', x, 'y: ', y) #the else clause is not executed

a = {1:'a',2:'b'}
for el in a.keys(): #by key
  print(el)

for el in a.values(): #by value
  print(el)

for el1,el2 in a.items(): #by item
  print(el1,el2)