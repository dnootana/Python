# Enter your code here. Read input from STDIN. Print output to STDOUT
def evenlist():
    list = input("Enter numbers : ")
    L = list.split()
    E = []
    for i in range(len(L)):
        num = int(L[i],10)
        if(num%2==0):
            E.append(L[i])
    print("Even numbers are : ",E)
