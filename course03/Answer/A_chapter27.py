# pyautogui 모듈을 불러옵니다.
import pyautogui

# 화면 크기를 가지고 옵니다.
width, height = pyautogui.size()

# 마우스 커서 위치를 화면 중앙에서 살짝 오른쪽으로 배치합니다.
pyautogui.moveTo(width // 2 + 100, height // 2)

# 사각형을 그립니다.
#1. 오른쪽으로 이동합니다.
pyautogui.drag(200, 0, duration=0.5)

#2. 아래로 이동합니다.
pyautogui.drag(0, 200, duration=0.5)

#3. 왼쪽으로 이동합니다.
pyautogui.drag(-200, 0, duration=0.5)

#4. 위로 이동합니다.
pyautogui.drag(0, -200, duration=0.5)