# Matrix 2.0

from colorama import Fore, Back, Style
from colorama import init
init()

print(Back.GREEN + Fore.BLACK + Style.BRIGHT)

def matrix_input(row):
    array_row = []
    for i in range(row):
        array_col = []
        for j in input().split():
            if j != " ":
                array_col.append(float(j))
        array_row.append(array_col)
    return array_row


def add_matrices(m1, m2, row, col):
    matrix_sum = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(m1[i][j] + m2[i][j])
        matrix_sum.append(temp)
    return matrix_sum


def matrix_print(result, row, col):
    for i in range(row):
        for j in range(col):
            print(result[i][j], end=' ')
        print()


def multiply_matrix_constant(m1, matrix2, row, col):
    matrix_sum = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(m1[i][j] * matrix2)
        matrix_sum.append(temp)
    return matrix_sum


def matrix_element_sum(l1, l2):
    sum = 0
    for i in range(len(l1)):
        sum += l1[i] * l2[i]
    return sum


def matrix_two_multiply(m1, m2):
    c = [[0 for row in range(len(m2[0]))] for col in range(len(m1))]
    for i in range(len(m1)):
        l1 = m1[i]
        for j in range(len(m2[0])):
            l2 = [m2[x][j] for x in range(len(m2))]
            value = matrix_element_sum(l1, l2)
            c[i][j] = value
    return c


def transpose_main(matrix):
    c = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            c[i][j] = matrix[j][i]
    return c

def transpose_side(matrix):
    c = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            c[i][j] = matrix[j][i]
    res1 = c[::-1]
    for i in range(len(matrix)):
        a = res1[i][::-1]
        result.append(a)
    return result


def transpose_vertical(matrix):
    result = []
    for i in range(len(matrix)):
        a = matrix[i][::-1]
        result.append(a)
    return result


def transpose_horizontal(matrix):
    result = matrix[::-1]
    return result




while True:
    a = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrices
5. Exit 
""")
    if a == '1':
        print(Back.CYAN + Fore.BLACK + Style.BRIGHT)
        m1row, m1col = map(int, input("Enter size of first matrix:").split())
        print('Enter first matrix:')
        matrix1 = matrix_input(m1row)
        m2row, m2col = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        matrix2 = matrix_input(m2row)
        if m1row != m2row and m1col != m2col:
            print('ERROR')
        else:
            matrix_result = add_matrices(matrix1, matrix2, m1row, m1col)
            matrix_print(matrix_result, m1row, m1col)
    elif a == '2':
        print(Back.YELLOW + Fore.BLACK + Style.BRIGHT)
        m1row, m1col = map(int, input("Enter size of matrix:").split())
        print('Enter matrix:')
        matrix1 = matrix_input(m1row)
        print("Enter constant:")
        matrix2 = float(input())
        matrix_result = multiply_matrix_constant(matrix1, matrix2, m1row, m1col)
        matrix_print(matrix_result, m1row, m1col)
    elif a == '3':
        print(Back.BLUE + Fore.BLACK + Style.BRIGHT)
        m1row, m1col = map(int, input('Enter size of first matrix:').split())
        print('Enter first matrix:')
        matrix1 = matrix_input(m1row)
        m2row, m2col = map(int, input('Enter size of second matrix:').split())
        print('Enter second matrix:')
        matrix2 = matrix_input(m2row)

        matrix_result = matrix_two_multiply(matrix1, matrix2)
        print('The result is:')
        matrix_print(matrix_result, m1row, m2col)
    elif a == '4':
        print(Back.RED + Fore.BLACK + Style.BRIGHT)
        print('''
    1. Main diagonal
    2. Side diagonal
    3. Vertical line
    4. Horizontal line''')
        transpose_choice = int(input('Your choice:'))
        if transpose_choice == 1:
            m1row, m1col = map(int, input('Enter matrix size:').split())
            print('Enter matrix:')
            matrix1 = matrix_input(m1row)
            result = transpose_main(matrix1)
            print('The result is:')
            matrix_print(result, m1row, m1col)

        elif transpose_choice == 2:
            m1row, m1col = map(int, input('Enter matrix size:').split())
            print('Enter matrix:')
            matrix1 = matrix_input(m1row)
            result = transpose_side(matrix1)
            print('The result is:')
            matrix_print(result, m1row, m1col)

        elif transpose_choice == 3:
            m1row, m1col = map(int, input('Enter matrix size:').split())
            print('Enter matrix:')
            matrix1 = matrix_input(m1row)
            result = transpose_vertical(matrix1)
            print('The result is:')
            matrix_print(result, m1row, m1col)

        elif transpose_choice == 4:
            m1row, m1col = map(int, input('Enter matrix size:').split())
            print('Enter matrix:')
            matrix1 = matrix_input(m1row)
            result = transpose_horizontal(matrix1)
            print('The result is:')
            matrix_print(result, m1row, m1col)
    elif a == '5':
        print(Style.RESET_ALL)

        break
