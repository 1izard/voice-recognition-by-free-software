import numpy as np

data_lst = [[1, 4], [2, 1], [2, 3], [3, 2],
        [3, 3], [4, 1], [4, 3], [5, 4]]
clazz = [1, 2, 1, 2, 2, 2, 1, 1]

def main():
    x = [3, 4]

    distance_lst = []
    i = 0
    for data in data_lst:
        distance_lst.append([i, (x[0]-data[0])**2 + (x[1]-data[1])**2])
        i += 1
    print(distance_lst)

    distance_lst = sorted(distance_lst, key=lambda d: d[1])
    print(distance_lst)
    least_3_distance_lst = distance_lst[:3]
    print(least_3_distance_lst)

    total = 0
    for distance in least_3_distance_lst:
        total += clazz[distance[0]]
    if total <= 4:
        print("x is clazz 1")
    else:
        print("x is clazz 2")


if __name__ == "__main__":
    main()
