import pyautogui as pa
from time import sleep

#    print(pa.KEYBOARD_KEYS)
#    cx, cy = pa.position()
#    print(cx,cy)


for i in range(5):
    # 1 Click : HandBrake
    sleep(1)
    pa.moveTo(800, 80)
    pa.click()

    # 2 Click : Open and Close Source
    sleep(1)
    pa.keyDown('alt')
    pa.typewrite('f')
    pa.keyUp('alt')
    pa.typewrite('s')
    pa.press('esc')

    # 4 Click : Open Source
    sleep(1)
    pa.keyDown('alt')
    pa.typewrite('f')
    pa.keyUp('alt')
    pa.typewrite('s')

    # 5 Enter : next file
    sleep(1)
    pa.press(['down'])
    pa.press(['down'])
    pa.press('enter')

    # 6 Click : HandBrake
    sleep(3)
    pa.moveTo(800, 80)
    pa.click()

    # 7 Click : Add To Queue
    sleep(4)
    pa.keyDown('alt')
    pa.typewrite('q')
    pa.keyUp('alt')
    sleep(1)
    pa.press(['down'])
    pa.press('enter')
