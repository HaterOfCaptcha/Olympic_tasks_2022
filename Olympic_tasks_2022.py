# n = 9
# end_list = list()
# basic_moves = ['.', 'turn 60', '.', 'turn -120', '.', 'turn 60', '.']
# Basic_moves = ['.', 'turn 60', '.', 'turn -120', '.', 'turn 60', '.']
#
#
# def recursion(lsd, depth):
#     for i in range(len(lsd)):
#         if lsd[i] == '.' and depth > 1:
#             lsd[i] = recursion(lsd=Basic_moves, depth=depth - 1)
#         elif lsd[i] == '.' and depth == 1:
#             lsd[i] = ' '
#     return lsd
# print(recursion(basic_moves, n))
# for i in recursion(basic_moves, n):
#     if type(i) == list:
#         end_list.extend(i)
#     else:
#         end_list.append(i)
# end_list = [end_list[i] for i in range(len(end_list)) if i%2==1]
# for i in end_list:
#     print(i)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# матрица квадратная nxn заполненная по спирали числами от 1 до n^2
# import numpy as np
#
# m = int(input())
# matrix = np.zeros((m, m)).astype(int)
# current_number = 1
# depth = 0
# alarm = False
# while current_number != (m) ** 2:
#     for i in range(4):
#         matrix = np.rot90(matrix)
#         eulav = depth > 0
#         if i == 2 or i == 1:
#             deploy_matrix = [i for i in range(current_number + 1, current_number + m - depth * 2)]
#             matrix[depth][depth + 1:m - depth] = deploy_matrix
#         elif i == 3:
#             deploy_matrix = [i for i in range(current_number + 1, current_number + m - depth * 2 - 1)]
#             matrix[depth][depth + 1:m - depth - 1] = deploy_matrix
#         elif i == 0:
#             deploy_matrix = [i for i in range(current_number + eulav, current_number + m - depth * 2 + eulav)]
#             matrix[depth][depth: m - depth] = deploy_matrix
#         value = i == 3
#         current_number = matrix[depth][m - depth - value - 1]
#
#         if (m) ** 2 == current_number:
#             alarm = True
#             break
#     if alarm == True:
#         break
#     depth += 1
# if (m - 1) % 2 == 1:
#     matrix = np.rot90(np.rot90(matrix))
# for i in matrix:
#     print(*i)
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 56 57 58 59 60 61 62 63 64 65 66 67 68 69 16
# 55 104 105 106 107 108 109 110 111 112 113 114 115 70 17
# 54 103 144 145 146 147 148 149 150 151 152 153 116 71 18
# 53 102 143 176 177 178 179 180 181 182 183 154 117 72 19
# 52 101 142 175 200 201 202 203 204 205 184 155 118 73 20
# 51 100 141 174 199 216 217 218 219 206 185 156 119 74 21
# 50 99 140 173 198 215 224 225 220 207 186 157 120 75 22
# 49 98 139 172 197 214 223 222 221 208 187 158 121 76 23
# 48 97 138 171 196 213 212 211 210 209 188 159 122 77 24
# 47 96 137 170 195 194 193 192 191 190 189 160 123 78 25
# 46 95 136 169 168 167 166 165 164 163 162 161 124 79 26
# 45 94 135 134 133 132 131 130 129 128 127 126 125 80 27
# 44 93 92 91 90 89 88 87 86 85 84 83 82 81 28
# 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Game of life
# import numpy as np
#
#
# def c(n, kind_of):
#     if n == -1:
#         return -1
#     else:
#         return n % kind_of
#
#
# wide = 6
# height = 5
# # List = [[i for i in input()] for j in range(height)]
# # print(List)
# List = np.array(
#     [['.', '.', '.', 'X', 'X', '.'], ['.', 'X', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.'],
#      ['X', 'X', '.', '.', '.', '.'], ['X', '.', '.', 'X', 'X', '.']]
#
# )
#
# # print(List)
# end_list = [['_' for i in range(wide)] for j in range(height)]
# for i in range(height):
#     for j in range(wide):
#         up = List[c(i - 1, height), c(j, wide)] + List[c(i - 1, height), c(j + 1, wide)] + List[
#             c(i - 1, height), c(j - 1, wide)]
#         left_and_right = List[c(i, height), c(j - 1, wide)] + List[c(i, height), c(j + 1, wide)]
#         down = List[c(i + 1, height), c(j, wide)] + List[c(i + 1, height), c(j + 1, wide)] + List[
#             c(i + 1, height), c(j - 1, wide)]
#         all_eight = up + left_and_right + down
#         # end_list[i][j] = sum.count('X')
#         if all_eight.count('X') == 3:
#             end_list[i][j] = 'X'
#         if all_eight.count('X') == 2:
#             end_list[i][j] = List[i][j]
#         if 3 < all_eight.count('X') or all_eight.count('X') < 2:
#             end_list[i][j] = '.'
# for i in range(len(end_list)):
#     end_list[i] = [''.join(end_list[i])]
#     print(*end_list[i])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Зал Большого театра столь велик, что артистам при выступлении необходимо иметь радиомикрофоны.
#
# В начале и конце спектакля все артисты находятся за кулисами. Артисты выходят на сцену и покидают сцену через правую или левую кулису, при этом артист берет с собой один микрофон.
# Уйдя со сцены, артист оставляет микрофон за той кулисой, через которую он ушел.
#
# Имеется режиссерский план, в котором для каждого артиста указано его прихода и ухода со сцены, а также то, через какие кулисы он входит и выходит.
#
# Определите, какое наименьшее число микрофонов необходимо приготовить режиссеру за каждой кулисой до начала спектакля.
# import numpy as np
#
# left_microphones, right_microphones = 0, 0
# enters = np.array([-1, 500, -1, 600, 650, 700, 800, 900])
# a = np.array([[-1, -1, 'a', 'a'],
#               [500, 700, 'l', 'r'],
#               [-1, -1, 'a', 'a'],
#               [600, 800, 'l', 'r'],
#               [650, 750, 'r', 'l'],
#               [700, 900, 'r', 'l'],
#               [800, 1000, 'l', 'r'],
#               [900, 1100, 'l', 'r']])
#
#
#
#
# def find_next(current_index, flag, left_micro, right_micro, iteration=1):
#     if flag == 'r' and iteration == 1:
#         right_micro += 1
#     if flag == 'l' and iteration == 1:
#         left_micro += 1
#     if flag == 'r':
#         enter = int(a[current_index][1])
#         a[current_index] = [-1, -1, 'a', 'a']
#         enters[current_index] = -1
#         new_index = np.where(enters >= enter)[0]
#         if new_index.size > 0:
#             new_index = new_index[0]
#         else:
#             return (left_micro, right_micro)
#         return find_next(new_index, 'l', left_micro, right_micro, iteration + 1)
#
#     if flag == 'l':
#         enter = int(a[current_index][1])
#         a[current_index] = [-1, -1, 'a', 'a']
#         enters[current_index] = -1
#         new_index = np.where(enters >= enter)[0]
#         if new_index.size > 0:
#             new_index = new_index[0]
#         else:
#             return (left_micro, right_micro)
#         return find_next(new_index, 'r', left_micro, right_micro, iteration + 1)
#
#
# while a[a != [-1, -1, 'a', 'a']].size > 0:
#     ind = np.where(a != [-1, -1, 'a', 'a'])
#     current_index = ind[0][0]
#     current_actor = a[current_index]
#     flag = current_actor[2]
#     left_microphones, right_microphones = find_next(current_index, flag, left_microphones, right_microphones)
# print('left_microphones:',left_microphones, 'right_microphones:',right_microphones)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Лабиринт через pygame. Есть гемы, есть коллизии со стенами, есть персонаж. Не надо нажимать одновременно на 2 кнопки из 4 (WASD)
# import numpy as np
# import pygame as pg
#
# # Объявление лабиринта
# b = """1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#         1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
#         1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 1 0 0 1 1 1 0 0 1 0 1
#         1 0 1 0 1 1 0 1 1 1 1 1 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 0 1 0 1 0 0 0 0 0 1 0 1
#         1 0 1 0 1 0 0 0 0 1 1 1 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 1 0 0 0 0 0 1 0 1
#         1 0 1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1 1 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 1 0 0 1 0 1
#         1 0 1 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1 0 1 1 1 1 1 1 0 1 0 1 0 0 1 0 0 1 0 1
#         1 0 1 0 1 0 1 0 1 0 1 1 1 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 1 0 0 1 0 0 1 1 0 0 0 1 0 1
#         1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 1 0 0 1 0 0 0 0 1 1 1 0 0 1
#         1 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0 0 1
#         1 0 1 0 1 0 1 1 1 1 1 0 1 0 1 0 1 0 1 1 0 0 0 1 1 0 1 0 1 0 1 0 0 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1
#         1 0 1 0 1 0 0 1 0 0 0 0 1 0 1 0 1 0 1 1 1 0 1 1 1 0 1 0 1 0 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1
#         1 0 1 0 1 1 0 1 1 1 1 0 1 0 1 0 1 0 0 0 0 0 0 0 3 0 1 0 1 0 1 0 0 1 0 1 0 1 1 1 1 1 1 0 1 0 1 0 0 1
#         1 0 1 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 1 1 1 0 1 1 1 1 1 0 1 0 1 0 0 1 0 0 0 1 0 0 0 0 1 0 0 1 0 1 0 1
#         1 0 1 1 1 1 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 1 0 1 1 0 1 0 1 0 1 0 1 1
#         1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 0 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 1 0 1
#         1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 0 0 0 0 1 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1
#         1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1 0 1 0 1 1 1 0 1 0 1 0 1 0 0 0 0 1 1 0 1 0 0 3 0 0 0 0 0 1
#         1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 1 1 1 1 1 1 1 0 1 0 1 1 1 1 1 1 1 1
#         1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 0 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1
#         1 0 0 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#         1 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0 1 0 1 1 1 1 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
#         1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
#         1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
#         1 0 0 3 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 3 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
#         1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 0 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
#         1 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
#         1 1 1 1 0 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
#         1 0 0 0 0 0 0 0 0 1 1 1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
#         1 0 1 1 0 1 0 1 0 0 0 1 0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 1 1 1 1 0 1 0 1
#         1 0 1 1 0 1 0 1 1 1 1 1 0 1 0 1 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 0 1
#         1 0 1 1 0 1 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 1 1 1 1 0 1 0 1
#         1 0 1 1 0 1 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 0 0 1 1 1 1 0 0 1 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 0 1
#         1 0 0 0 0 1 0 1 1 1 0 1 0 1 1 1 1 0 0 0 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 0 1 0 1
#         1 0 1 1 1 1 0 1 1 1 0 1 0 0 0 1 1 0 1 1 1 1 0 0 1 1 1 1 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 1 0 1
#         1 0 1 1 0 1 0 1 0 1 0 1 1 1 1 1 1 3 1 0 0 0 0 0 0 0 0 1 0 0 1 1 1 1 1 0 0 1 0 1 0 0 1 1 0 1 0 1 0 1
#         1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 1 1 1 1 1 0 0 1 0 0 0 1 0 1 0 0 1 0 1 0 0 1 0 0 1 0 1
#         1 0 1 1 1 0 1 0 1 1 0 1 1 1 1 0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 0 1 0 1
#         1 0 0 0 1 1 1 1 1 1 0 1 0 0 0 0 1 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 0 1 0 1 0 0 1 1 0 1 1 0 1 0 1 0 1
#         1 1 1 0 1 1 1 1 1 1 0 1 1 1 1 0 1 0 1 1 1 1 0 0 1 1 1 1 0 0 1 0 1 0 1 0 0 0 0 0 3 0 0 0 0 0 0 1 0 1
#         1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
#         1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 1 1 0 1 1 0 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
#         1 0 1 0 1 0 1 0 0 0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1
#         1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 1 1 0 1 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
#         1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1
#         1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 1 1 0 1 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 0 1 0 1
#         1 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1
#         1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1 1 1 1 1 0 1 1 1 0 0 1 0 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 1
#         1 2 1 0 0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 1
#         1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1""".split()
#
# # Объявление переменных
# a = np.array([[b[i + j * 50] for i in range(50)] for j in range(50)])
# n = 0
# WIDTH = 800
# HEIGHT = 800
# FPS = 30
# dct = {}  # словарь для гемов, в котором ключ = координаты гема, значение = определенный объект гема
# tcd = {}  # словарь для препятствий, в котором ключ = координаты препятствия, значение = определенный объект препятствия
#
#
# # Объявление классов препятствий, игрока и гемов
# class Obstacles(pg.sprite.Sprite):
#     def __init__(self, name):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pg.Surface((16, 16))
#         self.image.fill((0, 0, 0))
#         self.rect = self.image.get_rect()
#         self.name = name
#
#
# class Player(pg.sprite.Sprite):
#     def __init__(self):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pg.Surface((16, 16))
#         self.image.fill((0, 150, 150))
#         self.rect = self.image.get_rect()
#
#     def right(self):
#         self.rect.x += 8
#
#     def left(self):
#         self.rect.x -= 8
#
#     def down(self):
#         self.rect.y += 8
#
#     def up(self):
#         self.rect.y -= 8
#
#
# class Gems(pg.sprite.Sprite):
#     def __init__(self, name):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pg.Surface((16, 16))
#         self.image.fill((150, 0, 150))
#         self.rect = self.image.get_rect()
#         self.name = name
#
#
# pg.init()  # старт pygame
# pg.mixer.init()
# screen = pg.display.set_mode((WIDTH, HEIGHT))  # создание окна
# pg.display.set_caption("Labirinth")  # установка названия окна
# clock = pg.time.Clock()  # ставим таймер, чтобы прорисовка шла не хаотично, а цивильно
# all_sprites = pg.sprite.Group()  # создаем массив для прорисовки
# for i in range(1, 51):
#     for j in range(1, 51):
#         if a[i - 1, j - 1] == '1':  # занесение в tcd объектов препятствий,
#                                     # чтобы можно было точно определить, с каким именно столкнулся игрок, заносим,
#                                     # ставим центр препятствиям
#                                     # в массив для прорисовки объекты препятствий
#             tcd[(i * 16, j * 16)] = Obstacles(f'a{i}')
#             tcd[(i * 16, j * 16)].rect.center = (i * 16, j * 16)
#             all_sprites.add(tcd[(i * 16, j * 16)])
#         if a[i - 1, j - 1] == '2':
#             player = Player()
#             player.rect.center = (i * 16, j * 16)
#             all_sprites.add(player)
#         if a[i - 1, j - 1] == '3':  # занесение в dct объектов гемов, заносим, ставим центр гемам
#                                     # в массив для прорисовки объекты гемов
#             dct[(i * 16, j * 16)] = Gems(f'a{i}')
#             dct[(i * 16, j * 16)].rect.center = (i * 16, j * 16)
#             all_sprites.add(dct[(i * 16, j * 16)])
#
# lst = list(dct.keys()) # список координат, на которых находятся гемы
# tls = list(tcd.keys()) # список координат, на которых находятся препятствия
# running = True
# while running:
#     clock.tick(FPS) # ставим периодичность
#     for event in pg.event.get(): # если в окне происходит вообще что угодно
#         if event.type == pg.QUIT: # если нажали на выход - выход
#             running = False
#         if pg.key.get_pressed()[pg.K_a] and (((player.rect.centerx - 16), player.rect.centery)) not in tls: # движение влево
#             player.left()
#         if pg.key.get_pressed()[pg.K_d] and (((player.rect.centerx + 16), player.rect.centery)) not in tls: # движение вправо
#             player.right()
#         if pg.key.get_pressed()[pg.K_w] and ((player.rect.centerx, (player.rect.centery - 16))) not in tls: # движение вверх
#             player.up()
#         if pg.key.get_pressed()[pg.K_s] and ((player.rect.centerx, (player.rect.centery + 16))) not in tls: # движение вниз
#             player.down()
#
#         if player.rect.center in lst: # если игрок на координатах гемов
#             n += 1
#             if n != 1:
#                 print(f'{n} gems out of 8 have been found!')
#             else:
#                 print(f'{n} gem out of 8 have been found!')
#             dct[player.rect.center].rect.center = (2 * HEIGHT, 2 * WIDTH)
#             lst[lst.index(player.rect.center)] = ()
#     # прорисовка
#     all_sprites.update()
#     screen.fill((255, 255, 255))
#     all_sprites.draw(screen)
#     pg.display.flip()
# pg.quit()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Я не хотел использовать рекурсию, потому что узнал, что она слишком затратна, и невероятно пожалел, поэтому все же сделал рекурсию
#
# Условие: Лабиринт mxn, нужно за (m+n-2) ходов дойти до выхода.
# Стартовая точка - левый нижний угол, выход - правый верхний угол.
# Найти кол-во подходящих маршрутов
#
# import numpy as np
#
# a = np.array([[0, 0, 0, 0, 0],
#               [0, 1, 0, 1, 0],
#               [0, 0, 0, 1, 0],
#               [0, 0, 0, 0, 1],
#               [0, 1, 1, 1, 1]])
# n = 5
# m = 5
# current_position = (n - 1, 0)
# temp_forks = []
#
#
# def funct(current_position, ways):
#     temp_fork = []
#     if current_position[0] > 0:
#         if a[current_position[0] - 1, current_position[1]] != 1:
#             temp_fork.append([current_position[0] - 1, current_position[1]])
#     if current_position[1] < 4:
#         if a[current_position[0], current_position[1] + 1] != 1:
#             temp_fork.append([current_position[0], current_position[1] + 1])
#     if len(temp_fork) == 1:
#         current_position = temp_fork[0]
#         ways = funct(current_position, ways)
#     if len(temp_fork) == 2:
#         ways = funct([current_position[0] - 1, current_position[1]], ways)
#         ways = funct([current_position[0], current_position[1] + 1], ways)
#     if len(temp_fork) == 0 and current_position == [0, m - 1]:
#         ways += 1
#     return ways
#
#
# ways = funct(current_position, 0)
# print(ways)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Президент одной маленькой, но очень гордой страны вдруг узнал, что на дворе двадцать первый век, и на лошадях ездить уже не модно. Однако, как выяснилось, нефти в стране нет, а без бензина автомобили ездить не умеют. Так что придется закупать нефть в других странах.
# Исследование внешнего рынка показало, что в мире есть n стран, экспортирующих нефть. При этом i-е государство продает баррель нефти либо за ai долларов, либо за bi евро.
# У президента есть a долларов и b евро. Главный бухгалтер утверждает, что если попытаться купить нефть у одного государства и за доллары, и за евро, то бюрократия может надолго отложить покупку, чего президент, разумеется, не хочет.
# Помогите президенту в таких непростых условиях узнать, сколько баррелей нефти он сможет купить.
# Формат входных данных
# На первой строке входного файла записаны три целых числа: n, a и b (1≤n≤100, 0≤a≤1000, 0≤b≤1000).
# В последующих n cтроках содержатся пары чисел ai, bi (0≤ai≤1000 , 0≤bi≤1000 ).
# Формат выходных данных
# Выведите в выходной файл максимальное количество нефти, которое может купить президент. Выведите ответ не менее чем с двумя знаками после десятичной точки.
# 4 3 2
# 1 1
# 2 2
# 3 3
# 4 4

# 3 2 5
# 6 4
# 3 5
# 8 7
# import numpy as np
#
# n, a, b = [int(i) for i in input().split()]
# data = np.array([[int(i) for i in input().split()] for j in range(n)])
# dollars = data[:, 0]
# euros = data[:, 1]
#
# dollar_course_1 = min(dollars)
# index_dollar_course_1 = np.where(dollars == dollar_course_1)[0]
# dollars[index_dollar_course_1] = 9999
# index_dollar_course_2 = np.where(dollars == min(dollars))[0]
#
# euro_course_1 = min(euros)
# index_euro_course_1 = np.where(euros == euro_course_1)[0]
# euros[index_euro_course_1] = 9999
# index_euro_course_2 = np.where(euros == min(euros))[0]
#
# if index_dollar_course_1 == index_euro_course_1 and euro_course_1 != euros[index_euro_course_2] and dollar_course_1 != dollars[index_dollar_course_2]:
#     if a / dollar_course_1 + b / euros[index_euro_course_2] >  a / dollars[index_dollar_course_2] + b / euro_course_1:
#         euro_course_1 = euros[index_euro_course_2]
#     else:
#         dollar_course_1 = dollars[index_dollar_course_2]
#
# oil = (a / dollar_course_1) + (b / euro_course_1)
# print(oil)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Быстрая сортировка
# import numpy as np
#
# a = np.array([5, 3, 2, 1, 6, 3, 8, 3, 9, 2, 9, 2])
#
#
# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     elems = array[array==array[round(len(array) / 2)]]
#     elem = array[round(len(array) / 2)]
#     before = array[array < elem]
#     after = array[array > elem]
#     z = np.append(quick_sort(before), elems)
#     z = np.append(z, quick_sort(after))
#     return z
#
#
# print(quick_sort(a))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Заяц стоит в центре большого катка и поет свою любимую песенку в игрушечный микрофон. От микрофона тянется достаточно длинный шнур, конец которого находится в руках у Волка. Волк хочет незаметно замотать Зайца этим шнуром. Для этого он катается вокруг Зайца на коньках и постепенно его заматывает. Траектория Волка — ломаная линия. При перемещении Волка микрофонный шнур всегда натянут (как будто он эластичный).
#
# Напишите программу, которая по заданной траектории Волка определяет на сколько полных оборотов Волк замотал Зайца. Учтите, что Волк во время движения может не только заматывать Зайца, но и разматывать, а также что заматывать Зайца можно в двух различных направлениях.
#
# Заяц первоначально находится в точке (0,0), Волк — в точке (1,0). Координаты представляются вещественными числами. Гарантируется, что траектория Волка не проходит через начало координат (местоположение Зайца).
# Либо ответ в задаче неправильный, либо я дебил. Но код работает верно - проверял на бумаге
#
#
# n = int(input()) # кол-во строчек входных данных
# up = 0
# down = 0
# points = [[int(i) for i in input().split()] for j in range(n)] # точки
#
# for i in range(1, n):
#     if points[i][0] * points[i - 1][0] < 0:
#         is_below = points[i][1] < ((points[i - 1][1] * points[i][0]) / points[i - 1][0])
#         # если волк находится выше графика функции, построенной из прошлой точки волка и (0,0)
#
#         if points[i][0] < 0:  # из правого в левое
#             if is_below != True:  # ребро между прошлой и новой точкой проходит через верхнюю грань
#                 up -= 1
#             else:
#                 down += 1
#
#         if points[i][0] > 0:  # из левого в правое
#             if is_below != True:  # ребро между прошлой и новой точкой проходит через верхнюю грань
#                 up += 1
#             else:
#                 down -= 1
#     if points[i - 1][0] != 0 and points[i][0] == 0:
#         if points[i - 1][0] < 0:
#             if points[i][1] > 0:
#                 up += 1
#             if points[i][1] < 0:
#                 down -= 1
#         if points[i - 1][0] > 0:
#             if points[i][1] > 0:
#                 up -= 1
#             if points[i][1] < 0:
#                 down += 1
#
#     if points[i - 1][0] == 0 and points[i][0] != 0:
#         if points[i - 2][0] * points[i][0] > 0:
#             if points[i - 2][0] < 0:
#                 if points[i - 1][1] > 0:
#                     up -= 1
#                 if points[i - 1][1] < 0:
#                     down += 1
#             if points[i - 2][0] > 0:
#                 if points[i - 1][1] > 0:
#                     up += 1
#                 if points[i - 1][1] < 0:
#                     down -= 1
# full_rounds = min(abs(up), abs(down))
# print(full_rounds)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Мансур играет в новую компьютерную стратегическую игру. Одной из самых главных задач в таких играх является добыча ресурсов. К счастью в этой игре только один необходимый для развития ресурс - это золото, и один вспомогательный - энергия.
#
# В этой игре существуют рудники, которые вырабатывают определенное количество золота и энергии. Все рудники находятся на одной прямой. Для того чтобы защитить собственные рудники можно построить силовое поле (отрезок на данной прямой покрывающий рудники, в том числе находящиеся в концах отрезка), которое потребляет энергию, равную своей длине.
#
# Мансур хочет построить одно силовое поле таким образом, чтобы энергии вырабатываемой рудниками, защищенными этим полем, было достаточно для снабжения поля энергией, а золота, добываемого этими рудниками, было как можно больше.
#
# Помогите Мансуру, напишите программу, которая будет определять, какое максимальное количество золота он может добыть с защищенных рудников.
# import numpy as np
#
# n = 6
# maximum_gold = []
# locations = np.array([-10 ** 10, -14, 1, 13, 100, 10 ** 10])
# productions = np.array([[1, 1], [100, 8], [10, 1], [17, 30], [999, 99], [1, 1]]) # в 1 ячейке голда, во второй энергия
#
#
# def search(current_gold, current_energy, left_boundary, right_boundary, max_golds):
#     left_mine = locations[locations < left_boundary][-1]
#     right_mine = locations[locations > right_boundary][0]
#     if left_boundary - left_mine <= current_energy:
#         new_current_gold = current_gold + productions[np.where(locations == left_mine)[0][0]][0]
#         new_current_energy = left_boundary - left_mine + productions[np.where(locations == left_mine)[0][0]][1]
#         max_golds = search(new_current_gold, new_current_energy, left_mine, right_boundary, max_golds)
#
#     if right_mine - right_boundary <= current_energy:
#         new_current_gold = current_gold + productions[np.where(locations == left_mine)[0][0]][0]
#         new_current_energy = right_mine - right_boundary + productions[np.where(locations == left_mine)[0][0]][1]
#         max_golds = search(new_current_gold, new_current_energy, left_boundary, right_mine, max_golds)
#
#     if left_boundary - left_mine > current_energy and right_mine - right_boundary > current_energy:
#         max_golds.append(current_gold)
#     return max_golds
#
#
# for i in range(1, n-1):
#     maximum_gold.extend(search(productions[i][0], productions[i][1], locations[i], locations[i], maximum_gold))
# maximum_gold = max(maximum_gold)
# print(maximum_gold)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# coding=utf-8
# Не так давно были достаточно популярны настольные игры на больших бумажных картах, в которых игроки передвигали фишки по определенным правилам. Недавно Вася нашел на чердаке целую кипу таких карт, но к ним, к сожалению, не прилагались правила игры. Без описаний он смог только понять, что на каждой из карт нарисовано некоторое количество кружков – возможных позиций для фишки, среди которых выделены начальная и конечная. Какие-то кружки соединены между собой отрезками, по которым разрешается перемещать фишку, при этом между некоторыми парами кружков может быть проведено сразу несколько отрезков. Перемещать фишку по отрезку разрешается в обоих направлениях.
#
# Поскольку правила игры Васе найти не удалось, он придумал свои собственные. В игре участвуют одновременно все карты. На каждой карте Вася использует ровно одну фишку. Изначально каждая фишка расположена в начальной позиции на соответствующей карте. Каждым ходом Вася перемещает фишку на каждой из карт из ее текущей позиции в некоторую другую позицию на этой карте, с которой текущая соединена отрезком. При этом даже если фишка на некоторой карте уже находится в конечной позиции, то Вася, делая очередной ход, все равно должен ее переместить.
#
# Вася заинтересовался, за какое минимальное количество ходов можно добиться того, чтобы фишки на всех картах одновременно оказались в конечных позициях. Помогите ему это выяснить.
#
# Гарантируется, что в пределах каждой карты из любой позиции можно переместить фишку в любую другую, возможно через некоторые промежуточные позиции.
#
# Формат входных данных
# Первая строка входного файла содержит число k – количество карт (1≤k≤10).
#
# Затем следуют k блоков, которые описывают карты. Первая строка каждого блока содержит два целых числа ni, и mi, (2≤ni≤20, 1≤mi≤1500), они задают количество позиций и количество отрезков на i-й карте, соответственно. Будем считать, что позиции пронумерованы числами от 1 до ni, причем начальная позиция имеет номер 1, а конечная – номер ni. В следующих mi строках находятся пары номеров позиций, соединенных соответствующим отрезком.
#
# Формат выходных данных
# В случае, если существует последовательность ходов, после которой фишки на каждой карте одновременно окажутся в конечных состояниях, выведите в выходной файл минимальную длину такой последовательности. Если такой последовательности не существует, выведите слово Impossible.
# 3
# 5 4
# 1 2
# 2 3
# 3 4
# 3 5
# 3 3
# 1 2
# 2 3
# 3 1
# 4 4
# 1 2
# 1 3
# 2 4
# 3 4
# import numpy as np
#
# dct = {}
# all = []
# maximumes_2k = []
# maximumes_2k_plus_1 = []
# is_only_2k = False
# is_only_2k_plus_1 = False
# k = int(input())
#
# temp_list = [[] for u in range(k)]
# temp_tsil = [[] for u in range(k)]
# for i in range(k):
#     dct[i] = {}
#     n, m = [int(i) for i in input().split()]
#     for j in range(m):
#         a, b = sorted([int(i) for i in input().split()])
#         dct[i][a] = []
#         temp_list[i].append(b)
#         temp_tsil[i].append(a)
#     for j in range(m):
#         dct[i][temp_tsil[i][j]].append(temp_list[i][j])
#
#
# def BFS(map_iteration, node, ends, q_operations):
#     if node == max(temp_list[map_iteration]):
#         ends.append(q_operations)
#     q_operations += 1
#     if node in temp_tsil[map_iteration]:
#         for i in range(len(dct[map_iteration][node])):
#             ends = BFS(map_iteration, dct[map_iteration][node][i], ends, q_operations)
#
#     return ends
#
#
# for i in range(k):
#     all.append(BFS(i, 1, [], 0))
# for i in range(len(all)):
#     if set(np.array(all[i]) % 2) == {0}:
#         is_only_2k = True
#     if set(np.array(all[i]) % 2) == {1}:
#         is_only_2k_plus_1 = True
#
# if is_only_2k == True and is_only_2k_plus_1 == True:
#     print('Impossible')
#
# else:
#     for i in range(len(all)):
#         if max(all[i]) % 2 == 0:
#             maximumes_2k.append(max(all[i]))
#         else:
#             maximumes_2k_plus_1.append(max(all[i]))
#     if is_only_2k == False and is_only_2k_plus_1 == False:
#         answer = [max(maximumes_2k),max(maximumes_2k_plus_1)][max(maximumes_2k) >= max(maximumes_2k_plus_1)]
#     if is_only_2k == True and is_only_2k_plus_1 == False:
#         answer = max(maximumes_2k)
#     if is_only_2k == False and is_only_2k_plus_1 == True:
#         answer = max(maximumes_2k_plus_1)
#     print(answer)
# print(all)

