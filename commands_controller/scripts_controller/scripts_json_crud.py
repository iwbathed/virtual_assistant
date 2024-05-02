import json
import os

from typing import List

from commands_controller.scripts_controller.scritps_json_crud_enum import ScriptsInfo


current_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

scripts_path = os.path.join(current_dir_path, "scripts")

file_name = "scripts_info.json"
file_path = os.path.join(os.path.join(current_dir_path, "scripts_controller"), file_name)
def load_scripts_info_to_json() -> List[dict]:
    files = os.listdir(scripts_path)
    # files = [file for file in files if file.endswith('.py')]

    if os.path.exists(file_path):
        scripts_info_json = read_json(file_path)

        scripts_names_json = [scripts_info[ScriptsInfo.NAME.value] for scripts_info in scripts_info_json]
        for name_json in scripts_names_json:
            if name_json not in files:
                scripts_info_json = delete_script_info_by_name_json(name_json)

        scripts_names_json = [scripts_info[ScriptsInfo.NAME.value] for scripts_info in scripts_info_json]
        for file in files:
            if file not in scripts_names_json:
                add_script_info_json({ScriptsInfo.NAME.value: file, ScriptsInfo.RUN_COMMAND.value: "", ScriptsInfo.PHRASE.value: ""})
        scripts_info_json = read_json(file_path)
    else:
        scripts_info_json = [{ScriptsInfo.NAME.value: file, ScriptsInfo.RUN_COMMAND.value: "",
                              ScriptsInfo.PHRASE.value: ""} for file in files]

        create_json(data=scripts_info_json, file_path=file_path)
    # print(f"2 {scripts_info_json}")
    return scripts_info_json

def get_script_data_by_key(search_by_value:str, search_by_key: ScriptsInfo) -> dict:
    data = read_json()
    for script_info in data:
        if script_info[search_by_key] == search_by_value:
            return script_info

def get_script_field_by_key(search_by_value:str, search_by_key: ScriptsInfo, get_key: ScriptsInfo) -> str:
    data = read_json()
    for script_info in data:
        if script_info[search_by_key] == search_by_value:
            return script_info[get_key]

def edit_script_field_by_script_name_json(script_name: str, key: ScriptsInfo, data_value: str) -> List[dict]:
    scripts = read_json()
    for i in range(len(scripts)):
        if scripts[i][ScriptsInfo.NAME.value] == script_name:
            scripts[i][key] = data_value
            break
    create_json(scripts)
    return scripts

def delete_script_info_by_name_json(script_name: str) -> List[dict]:
    scripts = read_json()
    for i in range(len(scripts)):
        if scripts[i][ScriptsInfo.NAME.value] == script_name:
            scripts.pop(i)
            break
    create_json(scripts)
    return scripts

# add one script info
def add_script_info_json(info: dict) -> None:
    scripts = read_json()
    scripts.append(info)
    create_json(scripts)

# get scripts info from json file
def read_json(file_path:str=file_path) -> List[dict]:
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def get_data_list_by_key(key:ScriptsInfo):
    data = read_json()
    return [script_info[key] for script_info in data]

# create (also update) json file
def create_json(data: List[dict], file_path:str=file_path) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    load_scripts_info_to_json()
    # edit_script_key_phrase_by_script_name('script3.py', 'привіт')
    print(read_json())







