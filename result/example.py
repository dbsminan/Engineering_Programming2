#2019052415
#윤석현

#과제 : 주민등록번호를 입력할 때 생년월일과 성별을 출력하는 코드를 만들어보세요.
#############################################################

Num1, Num2 = input().split('-')

if int(Num1[:2]) < 24 and int(Num2[0]) in (3, 4):
    year = 2000 + int(Num1[:2])
else:
    year = 1900 + int(Num1[:2])

month = int(Num1[2:4])
day = int(Num1[4:6])

if int(Num2[0]) == 1 or int(Num2[0]) == 3:
    gen = '남자'
else:
    gen = '여자'

print('나는 {}년 {}월 {}일에 태어난 {}입니다.'.format(year, month, day, gen))

#############################################################