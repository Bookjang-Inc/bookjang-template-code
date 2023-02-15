# 반복문 시작 전에, 정수(integer)를 입력받습니다.
n = int(input('Enter an integer: '))

# 입력받은 수가 0이 아니라면, 반복하는 코드를 작성합니다.
# 1. 반복문 안에서 짝수와 홀수를 판별합니다.
# 2. 이후, 새로운 정수(integer)를 다시 입력받습니다.
while n != 0:
    if n%2 == 0:
        print('Even number.')
    else:
        print('Odd number.')
    n = int(input('Enter an integer: '))
print('End.')