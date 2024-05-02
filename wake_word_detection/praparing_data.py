import os

import sounddevice as sd
from scipy.io.wavfile import write

micro_id = 1
def record_audio_and_save(save_path, n_start=0, n_end=100):
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    input("To start recording Wake Word press Enter: ")
    for i in range(n_start, n_end):
        fs = 44100
        seconds = 2

        myrecording = sd.rec(int(seconds * fs), device=micro_id, samplerate=fs, channels=2)
        sd.wait()
        write(save_path + str(i) + ".wav", fs, myrecording)
        input(f"Press to record next or two stop press ctrl + C ({i + 1}/{n_end}): ")

def record_background_sound(save_path, n_start=0, n_end=100):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    input("To start recording your background sounds press Enter: ")
    for i in range(n_start, n_end):
        fs = 44100
        seconds = 2

        myrecording = sd.rec(int(seconds * fs), device=micro_id, samplerate=fs, channels=2)
        sd.wait()
        write(save_path + str(i) + ".wav", fs, myrecording)
        print(f"Currently on {i+1}/{n_end}")

# Step 1: Record yourself saying the Wake Word
# print("Recording the Wake Word:\n")
# record_audio_and_save("audio/audio_data/", n_start=105, n_end=200)

# Step 2: Record your background sounds (Just let it run, it will automatically record)
print("Recording the Background sounds:\n")
record_background_sound("audio/background_sound/", n_start=21565, n_end=40000)
