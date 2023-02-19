def Fibonacci(min,max):
  a = 1
  b = 1
  sum = "1-1"

  for x in range(min,max):
    c = a + b
    a = b
    b = c
    sum += "-"+str(c)
  return(sum)
  """
  a = a + b
    sum += "-"+str(a)
    b = a + b
    sum += "-"+str(b)
  """
print(Fibonacci(1,10))