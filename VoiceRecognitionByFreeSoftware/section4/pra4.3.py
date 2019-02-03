import matplotlib.pyplot as plt

data_lst = [[1, 4], [2, 1], [2, 3], [3, 2],
        [3, 3], [4, 1], [4, 3], [5, 4]]
clazz_lst = [1, 2, 1, 2, 2, 2, 1, 1]

x = [2.1, 3]

def _show_graph():
    x_lst_1 = []
    x_lst_2 = []
    y_lst_1 = []
    y_lst_2 = []

    for i in range(0, len(data_lst)):
        if clazz_lst[i] == 1:
            x_lst_1.append(data_lst[i][0])
            y_lst_1.append(data_lst[i][1])
        else:
            x_lst_2.append(data_lst[i][0])
            y_lst_2.append(data_lst[i][1])

    plt.scatter(x_lst_1, y_lst_1, c='red', label='class1')
    plt.scatter(x_lst_2, y_lst_2, c='blue', label='class2')
    plt.scatter([x[0]], [x[1]], c='green', label='input')
    plt.legend()
    plt.grid()
    plt.show()

def main():

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
        total += clazz_lst[distance[0]]

    if total <= 4:
        clazz = 1
    else:
        clazz = 2
    print('x is class', clazz)

    _show_graph()


if __name__ == '__main__':
    main()
