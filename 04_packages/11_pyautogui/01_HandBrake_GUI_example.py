import pyautogui as pa
from time import sleep

#print(pa.KEYBOARD_KEYS)

cx, cy = pa.position()
print(cx,cy)

for i in range(38):
    # step 1
    pa.moveTo(527,80)
    pa.click()
    sleep(0.1)
    # step 2
    pa.keyDown('alt')
    pa.typewrite('f')
    pa.keyUp('alt')
    pa.typewrite('s')
    pa.press('esc')
    # step 3 
    sleep(0.4)
    pa.keyDown('alt')
    pa.typewrite('f')
    pa.keyUp('alt')
    pa.typewrite('s')
    sleep(0.3)
    pa.press(['down'])
    pa.press(['down'])
    pa.press('enter')
    # step 4
    sleep(8)
    pa.keyDown('alt')
    pa.typewrite('q')
    pa.keyUp('alt')
    sleep(0.3)
    pa.press(['down'])
    pa.press('enter')

