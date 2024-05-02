import time

import sounddevice
from vosk import Model, KaldiRecognizer
import queue


sample_rate = 16000
device = 2
channel_num = 1
blocksize = 8000


# sample_rate = 8000
# device = 2
# channel_num = 1
# blocksize = 4000



# model = Model(model_name="vosk-model-small-uk-v3-small")
# model = Model(model_name="vosk-model-uk-v3-lgraph")
model = Model(model_name="vosk-model-en-us-0.42-gigaspeech")



basic_duration = 30


q=queue.Queue()

def callback(data, frames, time, status):
    # if status:
    #     print(status)
    #
    q.put(bytes(data))
    pass



def listen(callback):
    print("start")
    with sounddevice.RawInputStream(samplerate=sample_rate, blocksize=blocksize, device = device,
                                    dtype= "int16", channels=channel_num, callback=callback):
        recognizer = KaldiRecognizer(model, sample_rate)
        # start_time = time.time()
        # time_duration = basic_duration
        while True:
            # current_time = time.time()
            # elapsed_time = current_time - start_time


            data = q.get()
            if recognizer.AcceptWaveform(data):
                # calback(recognizer.Result())
                print(recognizer.Result())
            else:
                print(recognizer.PartialResult())

            # if elapsed_time >= time_duration:
            #
            #     print("запис зупинено")
            #     break

listen(callback)