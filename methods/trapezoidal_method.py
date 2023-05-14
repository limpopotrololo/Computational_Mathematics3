def trap_int(f, a, step, n):
    pop = []
    for i in range(n + 1):
        pop.append(f(a + i * step))
    sum = 0
    for i in range(1, len(pop)):
        sum += pop[i]
    sum += pop[0] + pop[len(pop) - 1]

    return sum * step


def trap_init(f, a, b, eps, n=4):
    step = (b - a) / n
    int_coarse = trap_int(f, a, step, n // 2) + trap_int(f, a + step, step, n // 2)
    int_fine = trap_int(f, a, step, n)

    while abs(int_fine - int_coarse) / 3 > eps:
        n *= 2
        step /= 2
        int_coarse = int_fine
        int_fine = trap_int(f, a, step, n)

    print("Интеграл взятый методом трапеций = ", int_fine)
    print("Число разбиений на данном методе ", n)
