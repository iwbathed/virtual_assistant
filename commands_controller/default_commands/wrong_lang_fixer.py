import pyperclip
import keyboard
import pyautogui
import time
import pydirectinput

# eng_ukr = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х',
#            ']': 'ї',
#            'a': 'ф', 's': 'і', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж',
#            '\'': 'є',
#            'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.',
#            'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З',
#            'A': 'Ф', 'S': 'І', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д',
#            'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь'
#            }


# input_str_eng = "ghbdsn cdsn!!!!"
# input_str_ukr = "руддщ цщкдв!"
# input_str_swap = "ghbdsn cdsn yf знерщт!"


eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
ukr = "йцукенгшщзхїфівапролджєячсмитьбю"



def eng_to_ukr(input_str):
    result = ""
    for i in input_str:
        if i in eng:
            result += ukr[eng.rfind(i)]
        else:
            result += i
    return result

def ukr_to_eng(input_str):
    result = ""
    for i in input_str:
        if i in ukr:
               result += eng[ukr.rfind(i)]
        else:
            result += i
    return result

def ukr_eng_swap(input_str):
    result = ""
    for i in input_str:
        if i in ukr:
            result += eng[ukr.rfind(i)]
        elif i in eng:
            result += ukr[eng.rfind(i)]
        else:
            result += i
    return result

def to_upper(input_str):
    return input_str.upper()


def to_lower(input_str):
    return input_str.lower()


# print(eng_to_ukr(input_str_eng))
# print(ukr_to_eng(input_str_ukr))
# print(ukr_eng_swap(input_str_swap))

# print(to_upper("qwe"))
# print(to_lower("ASDASD"))


def convert(func, all):
    time.sleep(0.3)
    pydirectinput.keyDown('ctrl')
    if all:
        pydirectinput.press('a')
    pydirectinput.press('x')
    pydirectinput.keyUp('ctrl')

    wrong_text = pyperclip.paste()


    res = func(wrong_text)
    pyperclip.copy(res)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')



# convert(eng_to_ukr, 1)


if __name__ == "__main__":
    # keyboard.add_hotkey('ctrl+win+shift', convert(ukr_eng_swap, 1))
    keyboard.add_hotkey('ctrl+win+shift', convert(eng_to_ukr, 1))
    # keyboard.add_hotkey('ctrl+win+shift', convert(ukr_to_eng, 1))
    # keyboard.add_hotkey('ctrl+win+shift', convert(to_upper, 1))
    # keyboard.add_hotkey('ctrl+win+shift', convert(to_lower, 1))

    # keyboard.add_hotkey('win+shift', convert(ukr_eng_swap, 0))
    keyboard.add_hotkey('win+shift', convert(eng_to_ukr, 0))
    # keyboard.add_hotkey('win+shift', convert(ukr_to_eng, 0))
    # keyboard.add_hotkey('win+shift', convert(to_upper, 0))
    # keyboard.add_hotkey('win+shift', convert(to_lower, 0))

    keyboard.wait()

# recorded = keyboard.record(until='esc')
# print(recorded)



# def wrong_lang_input_validate(wrong_text=None):
#     print(wrong_text)
#     time.sleep(0.4)
#     if not wrong_text:

#         # pyautogui.keyDown('ctrl')
#         # pyautogui.press('a')
#         # pyautogui.press('x')
#         # pyautogui.keyUp('ctrl')

#         pydirectinput.keyDown('ctrl')
#         pydirectinput.press('a')
#         pydirectinput.press('x')
#         pydirectinput.keyUp('ctrl')

#                                     # pyautogui.hotkey('ctrl', 'a')
#                                     # pyautogui.hotkey('ctrl', 'c')

#                                     # pyautogui.press(['ctrl', 'a'])
#                                     # pyautogui.press(['ctrl', 'c'])
#         wrong_text = pyperclip.paste()
#         print("'" + wrong_text + "'")

#     res = ""
#     for i in wrong_text:
#         if i in eng_ukr.keys():
#             res += eng_ukr[i]
#         else:
#             res += i

#     print(res)
#     pyperclip.copy(res)

#     pydirectinput.keyDown('ctrl')
#     pydirectinput.press('v')
#     pydirectinput.keyUp('ctrl')
#     # pyautogui.keyDown('ctrl')
#     # pyautogui.press('v')
#     # pyautogui.keyUp('ctrl')
#     return res

# keyboard.add_hotkey('ctrl+win+shift', wrong_lang_input_validate)

# keyboard.wait()

# # print(wrong_lang_input_validate())

# # text = input("Text : ")
# #
# # print(wrong_lang_input_validate(text))
