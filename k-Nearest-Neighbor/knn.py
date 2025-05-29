import math 

data = [
    ((1, 2), 'Red'),
    ((2, 3), 'Red'),
    ((3, 1), 'Blue'),
    ((6, 5), 'Blue'),
    ((7, 7), 'Blue'),
    ((1, 3), 'Red')
]
distances =  []
new_points = (3,3)

for points,label in data:
    x1,y1 = points
    x2,y2 = new_points
    
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    distances.append((distance,label))
    distances.sort()
    

k = 3
nearest_neighbors = distances[:k]
print(nearest_neighbors)
