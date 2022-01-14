#esercizio 3

#input parameters 1
import sys

#usage = """requires two parameters (param1, param2)
#usage: python script.py param1, param2"""

#if(len(sys.argv) < 3):
 # print('The script: ',sys.argv[0],usage)
  #sys.exit(0) # exits after help printing

# read the two input parameters
#param1 = sys.argv[1]
#param2 = sys.argv[2]

# output the read parameters
#print('''The two parameters received as input
#for the script are:\n ''',param1, param2)

#input parameters 2
#while(True):
#  print('PLEASE INSERT AN INTEGER NUMBER IN THE RANGE 0-10')
#  param1 = input()
#  if int(param1) in range(11):
#    while(True):
#      print( 'PLEASE INSERT A CHAR PARAMETER IN [A,B,C]')
#      param2 = input()
#      if param2 in ['A','B','C']:
#        print('uso I due parametri passati dall utente: ',param1,param2)
 #       sys.exit()
  #    else: print('TRY AGAIN PLEASE')
  #else: print('TRY AGAIN PLEASE')


#input parameters 3

#def f(y):
 # if y >= 0.0:
  #  return y**5*math.exp(-y)
  #else:
    # return 0.0

#infile='mydata.txt'
#outfile='myout.txt'
#indata = open( infile, 'r')
#linee=indata.readlines()
#indata.close()
#processati=[ ]
#x=[ ]
#for el in linee:
 # valori = el.split()
  #x.append(float(valori[0])); y = float(valori[1])
  #processati.append(f(y))

#outdata = open(outfile, 'w')
#i=0
#for el in processati:
 # outdata.write('%g %12.5e\n' % (x[i],el))
  #i+=1
#outdata.close()

#MATRICI
import numpy as np

with open('Input2.txt', 'r') as f:
  data = f.readlines() # read raw lines into an array
cleaned_matrix = []
for raw_line in data:
  split_line = raw_line.strip().split(",") # ["1", "0" ... ]
  nums_ls = [int(x.replace('"', '')) for x in split_line] # get rid of the
#quotation marks and convert to int
  cleaned_matrix.append(nums_ls)
print(cleaned_matrix)
