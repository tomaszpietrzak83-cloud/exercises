def dist(points):
    close = min(points)
    far = max(points)
    return far - close


listOfPoints = [
    [1, 2, 3],
    [1, 2, 3, 2.5],
    [1, 2, 3, 2.5, 3.5],
    [1, 2, 3, 2.5, 3.5, 120],
    [1, 2, 3, 2.5, 3.5, 120, -1000],
]

for list in listOfPoints:
    print(dist(list))
