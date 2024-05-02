import os
import re

from audioclipextractor import AudioClipExtractor, SpecsParser
from mutagen.mp3 import MP3



def get_mp3_length(filename):
    audio = MP3(filename)
    length_in_seconds = audio.info.length
    return length_in_seconds





# path_to_save = 'D:\\programing\\my_projects\\python\\bachelor\\speech_recognition_v2\\wake_word_detection\\audio'
specs = '''
    2 17
    26 32.4
    40 58.9
'''
# ext.extract_clips(specs_file_path_or_str=specs, output_dir=path_to_save)

input_folder = "E:\\mp4-mp3\\movies_audio\\"
output_folder = "D:\\programing\my_projects\\python\\bachelor\\speech_recognition_v2\\wake_word_detection\\audio\\background_sound\\"
ffmpeg_path = 'D:\\programing\\my_projects\python\\bachelor\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'



duration_second = 2
files = [f for f in os.listdir(input_folder) if f.endswith(".mp3")]
# print(get_mp3_length())

for input_file in files:
# input_file = 'E:\\mp4-mp3\\movies_audio\\All Quiet on the Western Front (2022) WEB-DLRip-AVC [Ukr.Ger] [Sub Ukr.Eng] [Hurtom].mp3'
    file_length = get_mp3_length(input_folder + input_file)
    parts_num = int(file_length // duration_second)


    start_index = input_file.rfind('\\')
    print(start_index)
    print(input_file)

    for i in range(parts_num):
        title = f"{input_file[start_index + 1:-4]}_part_{i}"
        specs = f"{duration_second * i} {duration_second * (i+1)} {title}"

        print(specs)
        ext = AudioClipExtractor(
            audio_file_path=input_folder+input_file,
            ffmpeg_path=ffmpeg_path)



        ext.extract_clips(specs_file_path_or_str=specs,
                          output_dir=output_folder,
                            text_as_title=True)


# try:
#     while True:
#         ext.extract_clips(specs,
#                           'D:\\programing\\my_projects\\python\\bachelor\\speech_recognition_v2\\wake_word_detection\\audio',
#                           zip_output=True)
#
#
#
#
# except:
