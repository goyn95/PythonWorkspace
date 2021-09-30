def std_weight(height, gender):
    if gender == "남자":
        male_avWeight = round(height * height * 0.0022, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height, male_avWeight))
    else:
        female_avWeight = round(height * height * 0.0021, 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg입니다.".format(height, female_avWeight))

gender = "남자"
height = 175
std_weight(height, gender)