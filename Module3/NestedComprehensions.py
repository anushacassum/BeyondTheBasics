## Example of Nested Comprehension
#  matrix = [[0,1,2],[0,1,2],[0,1,2]]


matrix = []
# for y in range(3):
#     matrix.append([])
#     for x in range(3):
#         matrix[y].append(x)


matrix = [[x for x in range(3)] for y in range(3)]
print(matrix)
