# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

import os

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

history_file = "history.txt"

def load_history():
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = file.readlines()
        return [entry.strip() for entry in history]
    return []

def save_history(num1, sign, num2, result):
    with open(history_file, "a") as file:
        file.write(f"{num1} {sign} {num2} = {result}\n")

def show_history():
    history = load_history()
    print("\nИстория операций:")
    if history:
        for entry in history:
            print(entry)
    else:
        print("Empty")

def get_matrix_input():
    rows = int(input("Количество строк: "))
    cols = int(input("Количество столбцов: "))
    matrix = []
    print("Введите элементы матрицы (по строкам):")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error")
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error")
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Error")
        return None

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')

history = load_history()

while True:
    print("\nВыберите тип операции:")
    print("1. Обычные")
    print("2. Матрицы")
    print("3. История операций")
    print("4. Exit")

    choice = input("Номер операции: ")

    if choice == '1':
        num1 = int(input('Please choose your first number: '))

        if num1 == -1:
            break

        sign = input('What do you want to do? +, -, /, or *: ')
        num2 = int(input('Please choose your second number: '))

        if sign == '+':
            result = num1 + num2
        elif sign == '-':
            result = num1 - num2
        elif sign == '*':
            result = num1 * num2
        elif sign == '/':
            if num2 == 0:
                print("Error")
                continue
            result = num1 / num2
        else:
            print("Error")
            continue

        print(f"Result: {result}")

        save_history(num1, sign, num2, result)

    elif choice == '2':
        print("\nОперация:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")

        matrix_choice = input("->: ")

        if matrix_choice == '1':
            print("First matrix:")
            matrix1 = get_matrix_input()
            print("Second matrix:")
            matrix2 = get_matrix_input()

            result = add_matrices(matrix1, matrix2)
            if result:
                print("Result:")
                print_matrix(result)
                save_history(f"Сложение матриц:\n{matrix1}\n+\n{matrix2}\n=\n{result}")

        elif matrix_choice == '2':
            print("First matrix:")
            matrix1 = get_matrix_input()
            print("Second matrix:")
            matrix2 = get_matrix_input()

            result = subtract_matrices(matrix1, matrix2)
            if result:
                print("Result:")
                print_matrix(result)
                save_history(f"Вычитание матриц:\n{matrix1}\n-\n{matrix2}\n=\n{result}")

        elif matrix_choice == '3':
            print("First matrix:")
            matrix1 = get_matrix_input()
            print("Second matrix:")
            matrix2 = get_matrix_input()

            result = multiply_matrices(matrix1, matrix2)
            if result:
                print("Result:")
                print_matrix(result)
                save_history(f"Умножение матриц:\n{matrix1}\n*\n{matrix2}\n=\n{result}")


    elif choice == '3':
        show_history()

    elif choice == '4':
        print("Thanks for using this calculator, goodbye :)")
        break