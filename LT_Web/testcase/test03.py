def fibonacci(i):
  if i < 2:
    return 1
  else:
    return fibonacci(i-1)+fibonacci(i-2)
fib=[]
n = 5
for i in range(n):
  fib_i = fibonacci(i)
  fib.append(fib_i)
  print("{}th fibonacci number is : {}".format(i,fib[i]))

# print(fib)