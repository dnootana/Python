def isPrime(n):
  count = 0
  for i in range(1, int(math.sqrt(n))+1):
    if n%i == 0:
      count += 1 if i*i==n else 2
      if count > 2:
        return False
    return count == 2

def isPrime1(n):
  import math
  if n <2:
    return False
  for i in range(2, int(math.sqrt(n)+1):
    if n%i == 0:
      return False
  return True
