import random as rd


upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '@', '#', '$', '%', '^', '?']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print('==========비밀번호 무작위 생성 프로그램==========')


while True:
   menu = input('메뉴를 선택하세요\n 1.영/숫자 구성 2.모두 구성: ')
   if menu == '1' or menu == '2':
       pwlen = int(input("패스워드 길이="))
       pwexcount = int(input("패스워드 샘플 몇개 ?"))
       break
   else:
       print('잘못된 메뉴를 선택하셨습니다. 다시 선택해주세요.')


if menu == '1':
   passList = [upper, lower, number]
elif menu == '2':
   passList = [upper, lower, symbol, number]


def rd_password(len):
   passStr = ''
   for _ in range(len):
       passStr += rd.choice(rd.choice(passList))


   return passStr


for i in range(pwexcount):
   print(f"ex{i+1}) {rd_password(pwlen)}")


