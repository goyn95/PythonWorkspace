# # 자료구조의 변경
# menu = {"커피", "우유","주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# from random import *

# student = range(1, 21)
# student = list(student)
# shuffle(student)
# winners = sample(student, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다. --")

from random import *

users = range(1, 21)
users = list(users)
shuffle(users)
winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print(' -- 축하합니다. -- ')