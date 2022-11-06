def exp(a, b):
  if b==0:
    return 1
  return a * exp(a, b-1)

print(exp(10,2))