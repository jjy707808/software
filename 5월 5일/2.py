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
            print("%10d"%matrix[i][j],end="")
        print()
def transpose(matrix):
    n=len(matrix)
    result=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(matrix[j][i])
        result.append(row)
    return result
N=int(input())
A=make_matrix(N)
B=transpose(A)
print("원래 행렬")
print_matrix(A)
print("전치 행렬")
print_matrix(B)