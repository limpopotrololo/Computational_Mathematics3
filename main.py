from methods.rectangle_method import rec_init
from methods.trapezoidal_method import trap_init
from methods.simpson_method import sim_init

int_1 = lambda x: 4 * (x ** 3) - 5 * (x ** 2) + 6 * x - 7
int_2 = lambda x: -2 * x ** 3 - 5 * x ** 2 + 7 * x - 13
int_3 = lambda x: x ** 3 - 2 * x ** 2 + 3 * x + 23


def start():
    print("program is starting")
    print("1)")
    print("4 * x ** 3 - 5 * x ** 2 + 6 * x - 7")
    print("----------------------------------------------")
    print("2)")
    print(" -2 * x ** 3 - 5 * x ** 2 + 7 * x - 13")
    print("----------------------------------------------")
    print("3)")
    print("x ** 3 - 2 * x ** 2 + 3 * x + 23")
    var = int(input("Выбирите номер фукнкции интеграл от которой вы хотите взять\n"))
    if var == 1:
        func = int_1
    elif var == 2:
        func = int_2
    elif var == 3:
        func = int_3
    else:
        print("Вы что то сделали не так, надо повторить\n")
        exit()
    a = int(input("Введите левую границу интегрирования\n"))
    b = int(input("Введите правую границу интегрирования\n"))

    print()
    print("1)")
    print("Метод прямоугольников")
    print("----------------------------------------------")
    print("2)")
    print("Метод трапеции")
    print("----------------------------------------------")
    print("3)")
    print("Метод Симпсона")

    var = int(input("Определите метод взятия интеграла\n"))
    print("----------------------------------------------")
    acc = float(input("Введите погрешность\n"))
    print("----------------------------------------------")
    if var == 1:
        rec_init(func, a, b, acc)
    elif var == 2:
        trap_init(func, a, b, acc)
    elif var == 3:
        sim_init(func, a, b, acc)
    else:
        print("Вы что то сделали не так, надо повторить")


start()
