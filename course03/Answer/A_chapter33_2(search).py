# pyautogui 모듈을 불러옵니다.
import pyautogui

# 마우스 커서의 위치를 Google 검색창 위로 옮기고, 클릭합니다.
pyautogui.moveTo(2552, -1392)
pyautogui.click()

# 검색하고 싶은 키워드(예: Bookjang)을 작성하고, interval을 0.25로 설정합니다.
pyautogui.write('Bookjang', interval=0.25)

# 키워드 작성 이후, 'enter'키를 누릅니다.
pyautogui.press('enter')