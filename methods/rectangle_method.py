import math


def central_int(f, a, step, n=4):
    pop = []
    intsum = 0
    h = step / 2
    x = a
    for i in range(n):
        intsum += f(x + h)
        pop.append(f(x + h))
        x += step
    ans = intsum * step
    return ans


def left_int(f, a, step, n=4):
    pop = []
    intsum = 0
    for i in range(0, n):
        intsum += f(a + i * step)

        pop.append(f(a + i * step))
    return intsum * step


def right_int(f, a, step, n=4):
    intsum = 0
    for i in range(1, n + 1):
        intsum += f(a + i * step)
    return intsum * step


def rec_init(func, a, b, eps, n=4):
    int_coarse = central_int(func, a, (b - a) / n, n)
    int_fine = central_int(func, a, (b - a) / (2 * n), 2 * n)

    while (abs(int_fine - int_coarse) / 3) > eps:
        n *= 2
        int_coarse = central_int(func, a, (b - a) / n, n)
        int_fine = central_int(func, a, (b - a) / (2 * n), 2 * n)

    print("Интеграл методом средних = ", round(int_fine, 4))
    print("Количество итераций на данном методе = ",n)
    print("------------------------------------------------")
    n = 4
    int_coarse = left_int(func, a, (b - a) / n, n)
    int_fine = left_int(func, a, (b - a) / (2 * n), 2 * n)
    while (abs(int_fine - int_coarse) / 3) > eps:
        n *= 2
        int_coarse = left_int(func, a, (b - a) / n, n)
        int_fine = left_int(func, a, (b - a) / (2 * n), 2 * n)
    print("Интеграл методом левых прямоугольников = ", round(int_fine, 4))
    print("Количество итераций на данном методе = ", n)
    print("------------------------------------------------")

    n = 4
    int_coarse = right_int(func, a, (b - a) / n, n)
    int_fine = right_int(func, a, (b - a) / (2 * n), 2 * n)
    while (abs(int_fine - int_coarse) / 3) > eps:
        n *= 2
        int_coarse = right_int(func, a, (b - a) / n, n)
        int_fine = right_int(func, a, (b - a) / (2 * n), 2 * n)
    print("Интеграл методом правых прямоугольников = ", round(int_fine, 4))
    print("Количество итераций на данном методе = ", n)
    print("------------------------------------------------")



