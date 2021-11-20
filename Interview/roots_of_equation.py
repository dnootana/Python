N = 2
for i in range(1,N):
    for j in range(1,N):
        for k in range(1,N):
            for l in range(1,N):
                if i**3+j**3==k**3+l**3:
                    print(i,j,k,l)