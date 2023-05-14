def sim_int(f, a, step, n):
    pop = []
    for i in range(n + 1):
        pop.append(f(a + i * step))
    even_sum = 0
    odd_sum = 0
    for i in range(1, n, 2):
        odd_sum += pop[i]
    for i in range(2, n - 1, 2):
        even_sum += pop[i]
    sum = pop[0] + 4 * odd_sum + 2 * even_sum + pop[len(pop) - 1]

    return (step / 3) * sum


def sim_init(func, a, b, eps,n=4):
    step = (b - a) / n
    int_coarse = sim_int(func, a, step, n // 2) + sim_int(func, a + step, step, n // 2)
    int_fine = sim_int(func, a, step, n)

    while abs(int_fine - int_coarse) / 15 > eps:
        n *= 2
        step /= 2
        int_coarse = int_fine
        int_fine = sim_int(func, a, step, n)

    print("Интеграл взятый методом Симпсона = ", int_fine)
    print("Число разбиений на данном методе ", n)

