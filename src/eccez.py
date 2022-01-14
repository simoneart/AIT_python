#prova di eccezione

def divide(x,y):
  try:
    result = x/y
  except ZeroDivisionError:
    print("division by zero!")
  else: 
    print("ther result is:", result)
  finally:
    print("Executing finally clause")

divide("12","0")



