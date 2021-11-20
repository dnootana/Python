# Enter your code here. Read input from STDIN. Print output to STDOUT
r = int(input("Enter no of matrix rows : "))
#c = input("Enter no of matrix column")
A = []
max = 0
for i in range(r):
    a = []
    row_list = input("Enter row "+str(i+1)+" columns : ")
    a=list(map(int,row_list.split()))
    A.append(a)
    if len(A[i])>max:
        max = len(A[i])

print('Original Matrix : ',A)
print('Maximum columns : ',max)
for i in range(r):
    D = [0 for k in range(max)]
    D[0:len(A[i])] = A[i]
    A[i] = D
print('Final Matrix : ',A)
