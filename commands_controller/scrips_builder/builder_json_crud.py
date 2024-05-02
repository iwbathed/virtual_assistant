import json
import os.path
from typing import List

from project_settings import base_dir


scripts_path = os.path.join(base_dir, "commands_controller", "scripts")


def read_json(file_name:str) -> List[dict]:
    if not file_name.endswith(".json"):
        file_name += ".json"
    file_path = os.path.join(scripts_path, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


def create_json(data: List[dict], file_name: str) -> bool:

    if not file_name.endswith(".json"):
        file_name += ".json"
    file_path = os.path.join(scripts_path, file_name)
    if os.path.exists(file_path):
        return False
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        return True



