# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает 
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.


def print_operation_table(f, rows, cols):
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            print(f(i,j), end='\t')
        print()

print("Введи кол-во строк и стоблцов(два числа через пробел): ")

arg = [int(i) for i in input().split(" ")]

print_operation_table(lambda x, y: x * y, arg[0], arg[1])