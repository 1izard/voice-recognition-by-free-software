import numpy as np

rho = 0.4
w_arr = np.array([[0.2, 0.3]])
x_arrs = np.array([[1.0, -1.3], [1.0, -0.2], [1.0, 0.5], [1.0, 1.0]])
clazz = [1, 1, 2, 2]

def _tuning(i, w_arr, x_arr):
    gs = np.dot(w_arr, x_arr)
    gs_before = gs
    if clazz[i] == 1 and gs > 0:
        w_arr -= rho * x_arr
    elif clazz[i] == 2 and gs < 0:
        w_arr += rho * x_arr
    gs = np.dot(w_arr, x_arr)
    print(i, ": ", gs)
    return gs_before - gs

def main():
    print(x_arrs)
    print(w_arr)

    while True:
        diff = 0
        print()
        for i in range(0, x_arrs.shape[0]):
            diff += abs(_tuning(i, w_arr, x_arrs[i]))
        print(w_arr)
        if abs(diff) == 0:
            break

    print(w_arr)


if __name__ == "__main__":
    main()