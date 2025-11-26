"""
Reads points from a CSV-like file and finds the closest pair.
Expected file format (one point per line):
x,y
Example:
1,2
3,4
"""

import math


def read_points(filename):
    points = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                x_str, y_str = line.split(",")
                x = float(x_str)
                y = float(y_str)
                points.append((x, y))
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid line in file. Expected format x,y")
    return points


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def find_closest(points):
    if len(points) < 2:
        return None, None, None
    min_d = float("inf")
    best_pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_d:
                min_d = d
                best_pair = (points[i], points[j])
    return best_pair[0], best_pair[1], min_d


filename = input("Enter file name containing points (e.g., points.csv): ")
pts = read_points(filename)
if len(pts) >= 2:
    p1, p2, d = find_closest(pts)
    print(f"Closest points are {p1} and {p2} with distance {d:.2f}")
else:
    print("Not enough points to compare.")
