# 1 penjumlahan dan pengurangan matriks
# penjumlahan matriks
mat1 = [
    [5, 4, 0],
    [2, 3, 6],
]
mat2 = [
[1, 2, 0],
[4, 3, 2],
]


for x in range(0, len(mat1)):
 for y in range(0, len(mat1[0])):
  print (mat1[x][y] + mat2[x][y], end=' '),
print

# pengurangan matriks
mat1 = [
    [5, 0],
    [2, 6],
]
mat2 = [
[1, 0],
[4, 2],
]


for x in range(0, len(mat1)):
 for y in range(0, len(mat1[0])):
  print (mat1[x][y] - mat2[x][y], end=' '),
print

# 2. perkalian matriks
import numpy as np

matriks1 = np.array([[2, 3], [4, 5]])
matriks2 = np.array([[6, 7], [8, 9]])

#perkalian matriks
print(np.dot(matriks1, matriks2))

# 3. transpose matriks
import numpy as np

matriks = np.array ([[2, 3], [4, 5], [6, 7]])

#transpose matriks
print(np.transpose(matriks))

# 4. inverse matriks
import numpy as np

Matriks = np.array([[1,0,0],[0,1,0],[0,0,1]])

invers_matriks = np.linalg.inv(Matriks)
print(Matriks)

# 5. matriks identitas
import numpy as np

#buat matriks identitas 3x3
matriks_identitas = np.eye(3)

print(matriks_identitas)

# 6. reshape matriks
import numpy as np

matriks = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8,],
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
]

# reshape matriks menjadi 4x4
matriks_reshape = np.reshape(matriks, (2, 8))
print(matriks_reshape)
