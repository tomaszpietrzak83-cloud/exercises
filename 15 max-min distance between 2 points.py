from random import randint
from math import dist


def atGeneration(function):
    def wrapper(*args):
        tempFunction = function(*args)
        print(
            f"""Following points were generated:
            {tempFunction}
            """
        )
        return tempFunction

    return wrapper


def foundDistance(function):
    def wrapper(*args, **kwargs):
        tempFunction = function(*args, **kwargs)
        distance = tempFunction[0]
        firstPoint = tempFunction[1]
        secondPoint = tempFunction[2]

        if function.__name__ == "findMaxDistance":
            print(
                f"""Maximum distance between point: {firstPoint} and point: {secondPoint} is: {distance}
            """
            )
        elif function.__name__ == "findMinDistance":
            print(
                f"""Minimum distance between point: {firstPoint} and point: {secondPoint} is: {distance}
            """
            )
        return tempFunction

    return wrapper


@atGeneration
def generatePoints(n=None):
    if n is None:
        numberOfPoints = randint(3, 15)
    else:
        numberOfPoints = n

    listOfPoints = []
    for _ in range(numberOfPoints):
        listOfPoints.append((randint(-200, 200), randint(-200, 200)))

    return listOfPoints


@foundDistance
def findMaxDistance(pointsList):
    pointA = None
    pointB = None
    maxDistance = 0
    for i, firstPoint in enumerate(pointsList):
        for j, secondPoint in enumerate(pointsList):
            if j <= i:
                continue

            distance = dist(firstPoint, secondPoint)

            if distance > maxDistance:
                maxDistance = distance
                pointA = firstPoint
                pointB = secondPoint
    return (maxDistance, pointA, pointB)


@foundDistance
def findMinDistance(pointsList):
    pointA = None
    pointB = None
    minDistance = 10e355
    for i, firstPoint in enumerate(pointsList):
        for j, secondPoint in enumerate(pointsList):
            if j <= i:
                continue

            distance = dist(firstPoint, secondPoint)

            if distance < minDistance:
                minDistance = distance
                pointA = firstPoint
                pointB = secondPoint
    return (minDistance, pointA, pointB)
