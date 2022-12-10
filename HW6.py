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


values = [0, 2, 10, 6]

def same_by(func, val):
    return len(set(map(func, val))) == 1 if val else True

    
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
