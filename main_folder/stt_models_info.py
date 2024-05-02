import os
from re import match
from pathlib import Path
import requests


MODEL_PRE_URL = "https://alphacephei.com/vosk/models/"
MODEL_LIST_URL = MODEL_PRE_URL + "model-list.json"
MODEL_DIRS = [os.getenv("VOSK_MODEL_PATH"), Path("/usr/share/vosk"),
        Path.home() / "AppData/Local/vosk", Path.home() / ".cache/vosk"]

def add_path_for_models(path: str) -> None:
    if os.path.exists(path):
        MODEL_DIRS.insert(0, path)

def get_all_paths_for_models() -> list:
    return MODEL_DIRS

def get_models() -> list:
    response = requests.get(MODEL_LIST_URL, timeout=10)
    models = {stt_model["name"] for stt_model in response.json()}
    return sorted(list(models))


def get_languages() -> list:
    response = requests.get(MODEL_LIST_URL, timeout=10)
    languages = {m["lang"] for m in response.json()}
    return sorted(list(languages))


def get_models_by_lang(lang):
    dirs = []
    models_in_dirs = []
    for directory in MODEL_DIRS:
        if directory is not None and os.path.exists(directory):
            dirs.append(directory)
    for d in dirs:
        model_file_list = os.listdir(d)
        model_file = [model for model in model_file_list if
                match(r"vosk-model(-small)?-{}".format(lang), model)]
        if model_file != []:
            models_in_dirs.extend(model_file)
    if models_in_dirs != []:
        return models_in_dirs
    else:
        response = requests.get(MODEL_LIST_URL, timeout=10)
        result_models = [model["name"] for model in response.json() if
                        model["lang"] == lang and model["obsolete"] == "false"]
        return result_models








