
import ctypes
import win32con
import win32api
import py_win_keyboard_layout

def get_keyboard_layout_name():
    # layout_name = ctypes.create_string_buffer(8)
    # user32 = ctypes.WinDLL('user32', use_last_error=True)
    # user32.GetKeyboardLayoutNameA(layout_name)
    # return layout_name.value.decode()
    return py_win_keyboard_layout.get_foreground_window_keyboard_layout()

def set_keyboard_layout_name(layout_name):
    if type(layout_name) == str:
        layout_name = int(layout_name, 16)
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(layout_name)
    # user32 = ctypes.WinDLL('user32', use_last_error=True)
    # user32.LoadKeyboardLayoutW(layout_name, 1)

def get_layout_list():
    return py_win_keyboard_layout.get_keyboard_layout_list()

# def set_key_status(virtual_key, state):
#     if state:
#         win32api.keybd_event(virtual_key, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
#     else:
#         win32api.keybd_event(virtual_key, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)

def get_key_status(virtual_key):
    return win32api.GetKeyState(virtual_key) & 0x01 == 1



def set_key_status(key, status:bool):
    if not status == get_key_status(key):
        ctypes.windll.user32.keybd_event(key, 0, 0, 0)
        ctypes.windll.user32.keybd_event(key, 0, 0x0002, 0)

# def toggle_caps_lock():
#     """Simulates a Caps Lock toggle by sending key presses."""
#     # Send Caps Lock down event
#     win32api.SendInput([
#         (win32con.VK_CAPITAL, win32con.KEYEVENTF_KEYDOWN),
#         (win32con.VK_CAPITAL, win32con.KEYEVENTF_KEYUP),
#     ])
#

if __name__ == "__main__":
    # Отримання стану клавіш Caps Lock, Scroll Lock та Num Lock
    # caps_lock_state = get_key_status(win32con.VK_CAPITAL)
    # scroll_lock_state = get_key_status(win32con.VK_SCROLL)
    # num_lock_state = get_key_status(win32con.VK_NUMLOCK)

    set_key_status(win32con.VK_CAPITAL, False)




    # current_layout = get_keyboard_layout_name()
    # print(f"Поточний розклад клавіатури: {type(current_layout)} {current_layout}")
    # eng = 67699721
    # ukr = -257424350
    #
    # set_keyboard_layout_name(eng)
    #
    #
    # current_layout = get_keyboard_layout_name()
    # print(f"Поточний розклад клавіатури: {current_layout}\n")


    # # Вивід стану клавіш Caps Lock, Scroll Lock та Num Lock
    # print(f"Стан Caps Lock: {'Увімкнено' if caps_lock_state else 'Вимкнено'}")
    # print(f"Стан Scroll Lock: {'Увімкнено' if scroll_lock_state else 'Вимкнено'}")
    # print(f"Стан Num Lock: {'Увімкнено' if num_lock_state else 'Вимкнено'}")



