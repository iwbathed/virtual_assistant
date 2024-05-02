import pyautogui
import pydirectinput
import pyperclip
import pyscreeze


# monitor_size = pyautogui.size()
# print(monitor_size)


def locate_on_screen(path_to_img: str):
    # lication = pyautogui.locateOnScreen(path_to_img)
    # point = pyautogui.center(lication)
    point = pyautogui.locateCenterOnScreen(path_to_img, confidence=0.9)
    # print(point)
    return point


def mouse_move_to_point(point_to_move: pyscreeze.Point):
    pyautogui.moveTo(point_to_move)

def keyboard_write(text: str = ""):
    pyautogui.write(text)
    # pyautogui.hotkey("enter")

def keyboard_insert(text: str = ""):
    pyperclip.copy(text)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')

def keyboard_copy():
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('c')
    pydirectinput.keyUp('ctrl')

def keyboard_paste():
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')



def mouse_left_click():
    pyautogui.leftClick()


def mouse_right_click():
    pyautogui.rightClick()


def mouse_middle_click():
    pyautogui.middleClick()


def mouse_left_doubleclick():
    pyautogui.doubleClick(button="left")


def mouse_left_down():
    pyautogui.mouseDown()


def mouse_left_up():
    pyautogui.mouseUp()


def mouse_move_down(distance=100, duration=0.3):
    pyautogui.move(0, distance, duration)


def mouse_move_up(distance=100, duration=0.3):
    pyautogui.move(0, -distance, duration)


def mouse_move_left(distance=100, duration=0.3):
    pyautogui.move(-distance, 0, duration)


def mouse_move_right(distance=100, duration=0.3):
    pyautogui.move(distance, 0, duration)


if __name__ == "__main__":



    # img_path = "../screenshots/aim.png"
    #
    # while(1):
    #     try:
    #         point = locate_on_screen(img_path)
    #         mouse_move_to_point(point)
    #         mouse_left_click()
    #     except Exception as e:
    #         break
    #         continue

    #
    # point = locate_on_screen(img_path)
    # # print(type(point))
    # move_to(point)

    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.keyUp("ctrl")

    # mouse_left_click()
    # mouse_right_click()
    # mouse_left_doubleclick()

    # mouse_left_down()

    # mouse_move_down()
    # mouse_move_right()




#
