import json

import threading
import mouse
import keyboard
# import time
#
# def record_events(escape_key: str = "esc") -> [list, list]:
#     mouse_events = []
#     keyboard_events = []
#     start_time = time.time()
#
#     def record_mouse(event):
#         relative_time = time.time() - start_time
#         mouse_events.append((relative_time, event))
#
#     def record_keyboard(event):
#         relative_time = time.time() - start_time
#         keyboard_events.append((relative_time, event))
#
#     mouse.hook(record_mouse)
#     keyboard.hook(record_keyboard)
#     keyboard.wait(escape_key)
#     mouse.unhook(record_mouse)
#     keyboard.unhook(record_keyboard)
#
#     return mouse_events, keyboard_events
#
# def play_events(mouse_events: list, keyboard_events: list):
#     start_time = time.time()
#
#     for event_time, mouse_event in mouse_events:
#         time_to_wait = event_time - (time.time() - start_time)
#         if time_to_wait > 0:
#             time.sleep(time_to_wait)
#         mouse.play([mouse_event])
#
#     for event_time, keyboard_event in keyboard_events:
#         time_to_wait = event_time - (time.time() - start_time)
#         if time_to_wait > 0:
#             time.sleep(time_to_wait)
#         keyboard.play([keyboard_event])
#
# mouse_events, keyboard_events = record_events()
# time.sleep(10)
# play_events(mouse_events, keyboard_events)

import os
import pickle
import threading
import time
import mouse
import keyboard
import win32con
from typing import List, Tuple, Any

from commands_controller.action_recorder.keyboard_state_controller import get_keyboard_layout_name, \
    get_key_status, set_keyboard_layout_name, set_key_status
from commands_controller.scripts_controller.scripts_json_crud import create_json

mouse_events = []
keyboard_events = []

keyboard_start_time = 0
mouse_start_time = 0
time_diff = None
recording_stopped = False

current_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scripts_path = os.path.join(current_dir_path, "scripts")


# def record_events(escape_key: str = "esc") -> [list, list]:
#
#     mouse.hook(mouse_events.append)
#
#     keyboard.start_recording()
#     keyboard.wait(escape_key)
#
#     mouse.unhook(mouse_events.append)
#     keyboard_events = keyboard.stop_recording()
#
#     return mouse_events, keyboard_events

def pickle_file_exist(file_name:str) -> bool:
    if not file_name.endswith(".pickle"):
        file_name += ".pickle"
    return os.path.exists(os.path.join(scripts_path, file_name))

def watcher():
    print("start watch func")
    global time_diff, recording_stopped
    while True:
        print(recording_stopped)
        if recording_stopped:
            return
        if not mouse_events:
            mouse_start_time = time.time()
        if not keyboard_events:
            keyboard_start_time = time.time()
        if (mouse_events and keyboard_events):
            break

    time_diff = mouse_start_time - keyboard_start_time
    # return time_diff


def _record_events(escape_key: str = "esc") -> [list, list]:
    print("start record func")
    global mouse_events, keyboard_events, recording_stopped

    mouse.hook(mouse_events.append)
    keyboard.hook(keyboard_events.append)

    keyboard.wait(escape_key)
    recording_stopped = True
    mouse.unhook(mouse_events.append)
    keyboard.unhook(keyboard_events.append)
    print("end record func")
    # return mouse_events, keyboard_events

def record_events(escape_key: str = "esc") -> Tuple[List[Any], List[Any]]:
    watcher_thread = threading.Thread(target = lambda : watcher())
    watcher_thread.start()

    record_thread = threading.Thread(target = lambda : _record_events(escape_key))
    record_thread.start()

    watcher_thread.join()
    record_thread.join()

    print("recording ended")
    return keyboard_events, mouse_events


# def play_events(mouse_events: list, keyboard_events: list, time_differance: int):
#     k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
#     k_thread.start()
#     print("k_thread.start()")
#     #Mouse threadings:
#
#     m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
#     m_thread.start()
#     print("m_thread.start()")
#     #waiting for both threadings to be completed
#
#     k_thread.join()
#     m_thread.join()

def play_events(keyboard_events, mouse_events, time_diff):
    print(f"time_diff {time_diff}")
    if time_diff is not None:
        if time_diff>0:
            k_thread = threading.Thread(target=lambda: keyboard.play(keyboard_events))
            k_thread.start()

            time.sleep(time_diff)
            m_thread = threading.Thread(target=lambda: mouse.play(mouse_events))
            m_thread.start()

            k_thread.join()
            m_thread.join()

        elif time_diff<=0:
            m_thread = threading.Thread(target=lambda: mouse.play(mouse_events))
            m_thread.start()

            time.sleep(-time_diff)
            k_thread = threading.Thread(target=lambda: keyboard.play(keyboard_events))
            k_thread.start()


            k_thread.join()
            m_thread.join()
    else:
        m_thread = threading.Thread(target=lambda: mouse.play(mouse_events))
        m_thread.start()

        k_thread = threading.Thread(target=lambda: keyboard.play(keyboard_events))
        k_thread.start()

        k_thread.join()
        m_thread.join()


def record_keyboard_state() -> dict:
    state = {
        "layout_code": get_keyboard_layout_name(),
        "caps_lock": {"key":win32con.VK_CAPITAL,
                        "status":get_key_status(win32con.VK_CAPITAL)},
        "num_lock": {"key":win32con.VK_NUMLOCK,
                        "status":get_key_status(win32con.VK_NUMLOCK)},
        "scroll_lock": {"key":win32con.VK_SCROLL,
                        "status":get_key_status(win32con.VK_SCROLL)},
    }
    return state

def set_keyboard_state(state: dict):
    print(state)
    for key, val in state.items():
        # print(key, val)
        try:

            # print(key["key"], key["status"])
            set_key_status(val["key"], val["status"])

        except TypeError as e:
            print(e)
            continue
    set_keyboard_layout_name(state["layout_code"])


def save_events(file_name:str, data: dict):
    if not os.path.exists(scripts_path):
        os.mkdir(scripts_path)
    if not file_name.endswith(".pickle"):
        file_name += ".pickle"
    file_path = os.path.join(os.path.join(current_dir_path, "scripts"), file_name)

    with open(file_path, 'wb') as file:
        pickle.dump(data, file)
    # if not os.path.exists(file_path):
    #     with open(file_path, 'wb') as file:
    #         pickle.dump(data, file)
    # else:
    #     print("file with that name already exist!")

def read_events(file_name) -> dict:
    if not file_name.endswith(".pickle"):
        file_name += ".pickle"
    file_path = os.path.join(os.path.join(current_dir_path, "scripts"), file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            return data

def record(file_name:str, escape_key: str = "esc"):
    keyboard_state = record_keyboard_state()
    keyboard_events, mouse_events = record_events(escape_key)

    data = {"keyboard_state": keyboard_state,
            "keyboard_events": keyboard_events,
            "mouse_events": mouse_events,
            "time_diff": time_diff}
    save_events(file_name, data)

def play(file_name):
    info = read_events(file_name)
    keyboard_state, keyboard_events, mouse_events, time_diff = info["keyboard_state"], info["keyboard_events"], info[
        "mouse_events"], info["time_diff"]
    set_keyboard_state(keyboard_state)
    play_events(keyboard_events=keyboard_events, mouse_events=mouse_events, time_diff=time_diff)

if __name__ == "__main__":
    file_name = "file1"

    # record(file_name)
    # time.sleep(5)
    play(file_name)
    # keyboard_state = record_keyboard_state()
    # keyboard_events, mouse_events = record_events()
    # data = {"keyboard_state": keyboard_state,
    #        "keyboard_events": keyboard_events,
    #        "mouse_events": mouse_events}
    # save_events(file_name, data)
    # info = read_events(file_name)
    # keyboard_state, keyboard_events, mouse_events = info["keyboard_state"], info["keyboard_events"], info["mouse_events"]
    # set_keyboard_state(keyboard_state)
    # play_events(keyboard_events=keyboard_events, mouse_events=mouse_events)











    # time.sleep(10)
    #
    # play_events(keyboard_events, mouse_events)

    # mouse_events, keyboard_events = record_events()
    # print(mouse_events)
    # print(keyboard_events)
    # time.sleep(10)
    # play_events(mouse_events, keyboard_events)



