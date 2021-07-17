# Enter your code here. Read input from STDIN. Print output to STDOUT
r = input("Enter no of matrix row")
#c = input("Enter no of matrix column")
A = []
for i in range(int(r)):
    row_list = input("Enter row "+str(i+1)+" columns : ")
    A.append(row_list.split())
    max = len(A[i])

print(A)
for i in range(int(r)):
    D = [0 for i in range(max)]
    D[0:len(A(i))] = A[i]
    A[i] = D
print(A)
