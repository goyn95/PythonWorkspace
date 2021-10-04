def std_weight(height, gender):
    if gender == "남자":
        male_avWeight = round(height * height * 0.0022, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height, male_avWeight))
    else:
        female_avWeight = round(height * height * 0.0021, 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg입니다.".format(height, female_avWeight))

gender = ''
height = 0
while True:
    if gender == "남자" or gender == "여자":
        break
    gender = input("성별을 입력하세요. : (남자, 여자)")
    if gender != "남자" and gender != "여자":
        print("잘못 입력하셨습니다. 다시 입력하세요.")
        continue
    height = height + int(input("키를 입력하세요. : "))
    
    
std_weight(height, gender)