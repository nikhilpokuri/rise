"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:

Input Format:
    - The first line contains a single integer n,
       the number of rows and columns in the square matrix arr.
    - next n lines contains n-space separated integers  

Output Format:
    - Return the absolute diff b/w the sums of matrix's two diagonals as a single integer.

Sample Input
3
1 2 3
4 5 6
9 8 9 

Sample Output
2

Explanation:
The left-to-right diagonal (1+5+9= 15). The right to left diagonal (3+5+9 = 17). 
Their absolute difference is |15-17|=2.

"""
# # input
# n = int(input("n:"))
# matrix = []

# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

n = int(input("n:"))
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrix)
for i in matrix:
    print(i)
# logic
left_digonal = 0
right_digonal = 0

for row in range(n):
    for col in range(n):
        if row == col:
            left_digonal += matrix[row][col]

        if row + col == n - 1:
            right_digonal += matrix[row][col]
        
#output
print(abs(left_digonal - right_digonal))