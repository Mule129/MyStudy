row, column = map(int, input().split())
matrix = [[0 for _ in range(column)] for _ in range(row)]

row_cnt = column_cnt = 0
for i in range(row):    
    column_data = input()
    for j in range(column):
        
        matrix[i][j] = column_data[j]

for i in range(row):
    vital = False
    for j in range(column):
        if matrix[i][j] == "X":
            vital = True
    if vital == False:
        row_cnt += 1

for i in range(column):
    vital = False
    for j in range(row):
        if matrix[j][i] == "X":
            vital = True
    if vital == False:
        column_cnt += 1

print(max(row_cnt, column_cnt))