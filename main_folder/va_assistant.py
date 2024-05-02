import threading

import sounddevice as sd
import librosa
import numpy as np
from keras.models import load_model

import stt
import tts
from fuzzywuzzy import fuzz

from commands_controller.scripts_controller.script_runner import run_script
from commands_controller.scripts_controller.scripts_json_crud import \
    get_script_data_by_key, scripts_path, get_data_list_by_key
from commands_controller.scripts_controller.scritps_json_crud_enum import ScriptsInfo

from device_id import get_device_id_by_name

fs = 22050
seconds = 2
model = load_model("..\\wake_word_detection\\audio\\saved_model\\WWD.h5")
phrases = get_data_list_by_key(ScriptsInfo.PHRASE.value)
started = False
pause = False

def stop_listener():
    global pause
    pause = True

def play_listener():
    global started
    global pause
    if not started:
        started = True
        listener()
    pause = False


def listener():
    current_state = 0
    micro_name = "Microphone (Realtek(R) Audio)"


    micro_id = get_device_id_by_name(micro_name)
    while True:
        if pause:
            continue
        else:
            if current_state:
                print(f"current_state {current_state}")
                current_state = 0
                tts.va_speak("Слухаю")
                stt.va_listen(va_response)
            else:
                myrecording = sd.rec(int(seconds * fs), samplerate=fs,
                                     device=micro_id, channels=1)
                sd.wait()
                mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
                mfcc_processed = np.mean(mfcc.T, axis=0)

                current_state = prediction(mfcc_processed)


def prediction(y, percent=0.95):
    model_prediction = model.predict(np.expand_dims(y, axis=0))
    print(model_prediction[:, 1])
    return 1 if model_prediction[:, 1] > percent else 0

def va_response(voice: str):
    phrase = recognize_cmd(voice)
    print(f"Фраза: '{phrase}'")
    if phrase not in phrases or phrase == '':
        tts.va_speak("Команда не розпізнана")
    else:
        execute_cmd(phrase)

def recognize_cmd(cmd: str):
    print(cmd)
    rc = {"phrase": "", "percent" : 50}
    for phrase in phrases:
        vrt = fuzz.ratio(cmd, phrase)
        if vrt > rc["percent"]:
            rc["phrase"] = phrase
            rc["percent"] = vrt
    print(rc)
    return rc["phrase"]


def execute_cmd(phrase: str):
    data = get_script_data_by_key(phrase, ScriptsInfo.PHRASE.value)
    print(data)
    # run_script(
    #     path_to_script=scripts_path + "\\" + data[ScriptsInfo.NAME.value],
    #     execution_command=data[ScriptsInfo.RUN_COMMAND.value])


if __name__ == "__main__":
    # voice_thread()
    listener()
