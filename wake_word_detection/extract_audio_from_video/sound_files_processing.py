import math
import os

from pydub import AudioSegment


def split_mp3(input_file, output_folder, duration_ms=2000):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_file)

    # Calculate the total duration of the audio in milliseconds
    total_duration = len(audio)

    # Calculate the number of parts needed
    num_parts = total_duration // duration_ms
    input_file=input_file[:-4]
    # Split the audio into parts
    print(f"parts {num_parts}")
    for i in range(num_parts):
        start_time = i * duration_ms
        end_time = (i + 1) * duration_ms
        part = audio[start_time:end_time]

        start_index = input_file.rfind('\\')
        # Save each part to the output folder
        output_file = f"{output_folder}/{input_file[start_index:]}_part_{i + 1}.wav"
        part.export(output_file, format="wav")
        if i % 100 == 0:
            print(f"progres {i}\\{num_parts}")

#
# def split_mp3(input_file, output_folder, duration):
#     audio = AudioSegment.from_mp3(input_file)
#     total_length = len(audio)
#     num_parts = math.ceil(total_length / (duration * 1000))
#
#     for i in range(num_parts):
#         start = i * duration * 1000
#         end = (i + 1) * duration * 1000
#         split_audio = audio[start:end]
#         output_path = os.path.join(output_folder, f"part_{i + 1}.mp3")
#         split_audio.export(output_path, format="mp3")
#         print(f"Exported {output_path}")
if __name__ == "__main__":
    input_folder = "E:\\mp4-mp3\\movies_audio\\"
    output_folder = "D:\\programing\my_projects\\python\\bachelor\\speech_recognition_v2\\wake_word_detection\\audio\\background_sound\\"

    duration_ms = 2000
    files = [f for f in os.listdir(input_folder) if f.endswith(".mp3")]
    print(files)
    counter = 0
    for input_file in files:
        counter += 1
        if counter <= 3:
            continue
        print(f"'{input_folder + input_file}'")
        split_mp3(input_folder + input_file, output_folder, duration_ms)
    print(files[3])
    split_mp3(input_folder + files[3], output_folder, duration_ms)