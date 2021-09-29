# while
# custumer = "토르"
# index =5
# while index >=1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(custumer, index))
#     index -=1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# custumer = "아이언맨"
# index = 1
# while True:
#      print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(custumer, index))
#      index +=1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# absent = [2,5] # 결석
# no_book = [7] # 책을 깜빡함
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {}는 교무실로 따라와.".format(no_book))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환   
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# from random import *


# times = range(5, 51)
# times = list(times)
# shuffle(times)
# count = 0

# for i in range(1, 51):
#     for j in times:
#         if j >= 5 and j <=15:
#             print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, j))
#             count += 1
#         else:
#             print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, j))
#         print("총 탑승승객 : %d 분" % count)

from random import *
count = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
    time =  randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {}분".format(count))