

from colorama import init
from colorama import Back, Fore, Style

init()



def it_m():
    print( Back.RED + Fore.BLACK + Style.BRIGHT)
    measurement = input("Введите кол-во строк и столбов: ").split()
    n, m = measurement
    mx = []
    for y in range(int(n)):
        mx.append(input().split())
    return mx



def sum_mat():


    mtx = it_m()
    mtx_2 = it_m()
    if len(mtx) == len(mtx_2) and len(mtx[0]) == len(mtx_2[0]):
        for i in range(len(mtx)):
            for x in range(len(mtx[0])):
                print(float(mtx[i][x]) + float(mtx_2[i][x]), end=' ')
            print('')
    else:
        print("ERROR")

def multiplication():


    mtx = it_m()
    const = input("Введите константу: ")
    for i in range(len(mtx)):
        for x in range(len(mtx[0])):
            print(float(mtx[i][x]) * float(const), end=' ')
        print('')

multiplication()
