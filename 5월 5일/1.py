import random
def make_matrix(n):
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(random.randint(1,n*n*10-1))
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            print("%12d"%matrix[i][j],end="")
        print()
def multiply_add(A,B,C):
    n=len(A)
    result=[]
    for i in range(n):
        row=[]
        for j in range(n):
            total=0
            for k in range(n):
                total+=A[i][k]*B[k][j]
            row.append(total+C[i][j])
        result.append(row)
    return result
N=int(input("N 입력: "))
A=make_matrix(N)
B=make_matrix(N)
C=make_matrix(N)
print("A")
print_matrix(A)
print("B")
print_matrix(B)
print("C")
print_matrix(C)
result=multiply_add(A,B,C)
print("A x B + C")
print_matrix(result)