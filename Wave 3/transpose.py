#Transpose with Zip
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this!.


data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
matrix = zip(*data)
for data_transpose in matrix : 
    print(data_transpose)