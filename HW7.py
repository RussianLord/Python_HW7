# Задача про планеты

# import math
# orbits = [(1, 3), (2.5, 10), (7,2), (6, 6), (4, 3)]
# def find_farthest_orbit(list_of_orbit):  
#     maxValue = 0
#     maxOrbit = ''
#     for i in range(len(orbits)):
#         a = orbits[i][0]
#         b = orbits[i][1]
#         print(a, b)
#         S = math.pi * a * b
#         print(S)
#         if maxValue < S:
#             maxValue = S
#             maxOrbit = f'{a},{b}'
        
#     print(f'Планета с орбитой {maxOrbit} является самой дальней и площадь орбиты равна {maxValue}')
# find_farthest_orbit(orbits)

# Задача про одинаковые/не одинаковые числа из списка

# values = [0, 2, 10, 6]

# def same_by(func, val):
#     return len(set(map(func, val))) == 1 if val else True

    
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# Задача про табрицу

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     for i in range(1, num_rows + 1):
#         answer = []
#         for j in range(1, num_columns + 1):
#             answer.append(str(operation(i, j)))
#         print("\t".join(answer))

# print_operation_table(lambda x, y: x * y)