def log(N):
  count = 0
  while N > 1:
    N = N //2
    count += 1
  return count
