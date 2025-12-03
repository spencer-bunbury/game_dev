# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# # acssesing items
# print(matrix [1][1])

# # modify
# matrix  [2][2] = 10
# print(matrix)

# # format
# for row in matrix:
#     for col in row:
#         print(col,end= " ")
#     print()

# # adding lists(2d)
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrix_2 = [[10,11,12],
          [13,14,15],
          [16,17,18]]
def add_matrix(a,b):
    matrix_3 = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        matrix_3.append(row)
    return matrix_3


result = add_matrix(matrix,matrix_2)
for row in result:
    print(row)



    

