import numpy
import random

n = int(input("Гранична межа: "))
tochki = []
for i in range(n):
    x = random.randint(-n, n)
    y = random.randint(- n, n )
    tochki.append([i, x, y])

triangles = []

for i in range(len(tochki)):
    for j in range(i+1, len(tochki)):
        for k in range(j+1, len(tochki)):
            triangles.append([
                tochki[i],
                tochki[j],
                tochki[k]
            ])

triangles = numpy.array(triangles)

def get_calculate_area(triangle):
    _, x1, y1 = triangle[0]
    _, x2, y2 = triangle[1]
    _, x3, y3 = triangle[2]
    return abs((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))/2

get_calculate_area_vectorized = numpy.vectorize(get_calculate_area, signature='(m,n)->()')

Sq = get_calculate_area_vectorized(triangles)

max_koord = max(Sq)
max_index = numpy.where(Sq == max_koord)[0][0]
print('Максимальне значення: ', max_koord)
print('Визначені точки: ')
for i, x, y in triangles[max_index]:
    print('Індекс:', i, f', значення: ({x},{y})')