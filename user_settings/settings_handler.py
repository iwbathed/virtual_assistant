import json
import os
from typing import NamedTuple

from main_folder.device_id import input_devices

current_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_name = "user_setting.json"
file_path = os.path.join(os.path.join(current_dir_path, "user_settings"), file_name)

input_device_info = input_devices()
input_device_names = [f"{info['name']}; Channels {info['maxInputChannels']}" for info in input_device_info]

class SettingsHandler:
    def __init__(self):
        self.input_device = input_device_names[0]

        self.stt_model_settings = {"language": "ua", "model_name": "vosk-model-small-uk-v3-small"}
        self.stt_listening_time = 15
        self.tts_model_settings = {"language": "ua", "model_id": "v4_ua", "speaker": "mykyta"}
        self.sample_rate = 48000

        self.put_accent = True
        self.put_yo = True

        self.font_family = "Arial"
        self.font_size = 14

        self.wwd_recognition_percentage = 95
        self.stt_recognition_percentage = 95

        # scripts record

        # self.ending_keys_sequence: tuple = ("Key.esc", "Key.esc")

        # scripts play
        # self.mouse_move_length_per_command = 100
        # self.keyboard_input_speed = 100


    def get_settings_dict(self) -> dict:
        return self.__dict__

    def set_settings(self, settings: dict) -> None:
        for key, value in settings.items():
            setattr(self, key, value)

    def create_json(self, data: dict, file_path:str=file_path) -> None:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def settings_json_exist(self) -> bool:
        return os.path.exists(file_path)

    def read_json(self, file_path:str=file_path)  -> dict :
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data

settings_handler = SettingsHandler()
settings_handler.set_settings(settings_handler.read_json())


if __name__ == "__main__":
    # load_scripts_info_to_json()


    # settings_handler.create_json(data=settings_handler.get_settings_dict())
    print(settings_handler.get_settings_dict())

    # for key in settings_handler.get_settings_dict().keys():
    #     print(f'setting_dict["{key}"] = ')

    # print(handler.read_json())
    # settings_handler.set_settings(settings_handler.read_json())
    # print(settings_handler.get_settings_dict())