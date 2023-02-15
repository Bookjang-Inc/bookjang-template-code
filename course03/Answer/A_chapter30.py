# registered_pw에 비밀번호 초기화합니다.
registered_pw = 1234

# password를 하나 입력받습니다.
entered_pw = int(input('Enter a password: '))

# registred_pw와 password가 같지 않다면, 반복하는 코드를 작성합니다.
# 1. 올바르지 않는 password라고 안내합니다.
# 2. password를 다시 입력받습니다.
while registered_pw != entered_pw:
    print('Incorrect password. Try again.')
    entered_pw = int(input('Enter a password: '))
print('Pass.')