def squareRoot(N: int) -> int:
  # O(N) = sqrt(N)
  i = 1
  while i*i <= N:
    if i*i == N:
      return i
    i += 1

def squareRoot1(N: int) -> int:
  #Binary Search solution O(N) = log N
  pass
