# -*- coding: utf-8 -*-
import torch
import sounddevice
import time

from user_settings.settings_handler import settings_handler

model_settings = settings_handler.tts_model_settings

sample_rate = 48000
put_accent = True
put_yo = True
# cpu, cuda, ipu, xpu, mkldnn, opengl, opencl, ideep, hip, ve, fpga, ort, xla, lazy, vulkan, mps, meta, hpu, mtia
device = torch.device("cpu")
model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=model_settings["language"],
                                     speaker=model_settings["model_id"])
model.to(device)  # gpu or cpu
def va_speak(text, speaker=model_settings["speaker"], sample_rate=sample_rate):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo
                            )
    sounddevice.play(audio, samplerate=sample_rate)
    time.sleep(len(audio)/sample_rate)
    # sounddevice.wait()
    sounddevice.stop()

if __name__ == "__main__":
    # text = "Зараз " + number_to_words(10) + " " + number_to_words(25)
    # va_speak(text)
    # text = "hello how are u"
    # va_speak(text)
    # print('\xd0')
    text = '''Фундаментальне значення проблеми буття для філософії. Людські виміри проблеми буття. Проблема буття є однією з найдавніших тем філософських роздумів і досліджень. «Чому взагалі є сутнє, а не навпаки — ніщо?» — це запитання М. Хайдеггер, один із найавторитетніших філософів XX ст., слідом за Ф.Шеллінгом вважав основним питанням метафізики як науки про фундаментальні основи всього сутнього. З часів давньогрецької філософії розділ філософського знання, пов'язаний із дослідженням буття, отримав назву "онтологія" (від давньогрецького "онтос"— буття, сутнє).'''
    va_speak(text)
