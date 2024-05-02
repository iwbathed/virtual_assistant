import os.path
import sys
import time
import json
import pyaudio

from vosk import Model, KaldiRecognizer

from user_settings.settings_handler import settings_handler

current_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.join(current_dir, '..', 'main_folder')
if main_dir not in sys.path:
    sys.path.append(main_dir)

from device_id import get_device_id_by_name

sample_rate = 16000
channel_num = 1
frames = 8192
# micro_name = "Microphone (Realtek(R) Audio)"
micro_name = settings_handler.input_device.split(";")[0]
print(micro_name)
micro_id = get_device_id_by_name(micro_name)
micro_id=2
print(micro_id)
basic_duration = 30

# path_to_model = "../models/stt/ua_big_model_v3"
model_settings = settings_handler.stt_model_settings
print(model_settings)
# model = Model(model_name=model_settings["model_name"])

model = Model(model_name="vosk-model-small-uk-v3-small")
recognizer = KaldiRecognizer(model, sample_rate)

mic = pyaudio.PyAudio()


def va_listen(callback=None):
    stream = mic.open(format=pyaudio.paInt16, channels=channel_num,
                      rate=sample_rate, input=True, frames_per_buffer=frames,
                      input_device_index=micro_id
                       )
    stream.start_stream()
    start_time = time.time()
    time_duration = basic_duration
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        # try:
        data = stream.read(4096, exception_on_overflow=False)

        # print(recognizer.PartialResult())
        if recognizer.AcceptWaveform(data):
            rec_res = recognizer.Result()
            print(rec_res)
        else:
            print(recognizer.PartialResult())
        #     if rec_res[14:-3]:
        #         print(rec_res)
        #         callback(json.loads(rec_res)["text"])
        #         start_time = time.time()
        # if elapsed_time >= time_duration:
        #     stream.stop_stream()
        #     print("запис зупинено")
        #     break


if __name__ == "__main__":
    va_listen()
    pass









# import time
# import vosk
# import sys
# import sounddevice
# import queue
# import json
# # ua_small_model_v3 ua_small_model_v3
# model = vosk.Model("../models/ua_small_model_v3")
# sample_rate = 16000
# micro_id = 1
#
# basic_duration = 15
#
# q = queue.Queue()
#
# def q_callback(input_data, frames, the_time, status):
#
#     if status:
#         print(status, sys.stderr)
#     q.put(bytes(input_data))
#
# def va_listen(callback):
#     start_time = time.time()
#     time_duration = basic_duration
#     with sounddevice.RawInputStream(samplerate=sample_rate,
#         blocksize=8000, device=micro_id,
#         dtype="int16", channels=2, callback=q_callback):
#
#         rec = vosk.KaldiRecognizer(model, sample_rate)
#         while True:
#
#             data = q.get()
#             if rec.AcceptWaveform(data):
#                 callback(json.loads(rec.Result())["text"])
#
#
#             current_time = time.time()
#             elapsed_time = current_time - start_time
#             print(f"elapsed_time: {elapsed_time}")
#             # Якщо пройшло більше 15 секунд, зупинити цикл
#             if elapsed_time >= time_duration:
#
#                 print("запис зупинено")
#                 break
#                 # print(rec.Result())
#             # else:
#             #     print(rec.PartialResult())
#
#


