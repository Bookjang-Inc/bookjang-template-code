import pyautogui

# 화면 크기를 가지고 옵니다.
width, height = pyautogui.size()

# 마우스 커서 위치를 화면 중앙에서 살짝 오른쪽으로 배치합니다.
pyautogui.moveTo(width // 2 + 100, height // 2)

# 소용돌이를 구성하는 선분의 길이를 준비합니다.
length = 200

# 선분의 길이가 0보다 작으면 그리는 것을 중단합니다.
while length > 0:
    # 사각형을 그립니다. 그릴 때 마다 선분의 길이를 줄입니다.
    #1. 오른쪽으로 이동합니다.
    pyautogui.drag(length, 0, duration=0.3)
    length = length - 5

    #2. 아래로 이동합니다.
    pyautogui.drag(0, length, duration=0.3)
    length = length - 5
    
    #3. 왼쪽으로 이동합니다.
    pyautogui.drag(-length, 0, duration=0.3)
    length = length - 5

    #4. 위로 이동합니다.
    pyautogui.drag(0, -length, duration=0.3)
    length = length - 5