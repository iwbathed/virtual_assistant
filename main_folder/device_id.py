import pyaudio
import sounddevice as sd


def device_info(name: str = None, to_print: bool = True) -> list:
    p = pyaudio.PyAudio()
    all_info = []
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        all_info.append(info)
    p.terminate()
    if to_print:
        if name:
            for info in all_info:
                if info['name'] != name:
                    print(f"ID: {info['index']}, {info['name']}, Input channels: {info['maxInputChannels']}")
        else:
            for info in all_info:
                print(f"ID: {info['index']}, {info['name']}, Input channels: {info['maxInputChannels']}")
    return all_info

def input_devices():
    p = pyaudio.PyAudio()
    all_info = []
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info["maxInputChannels"] > 0:
            all_info.append(info)
    p.terminate()
    return all_info

def device_info_full(name=None):
    p = pyaudio.PyAudio()
    all_info = []
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        all_info.append(info)
    p.terminate()
    if name:
        for info in all_info:
            if info['name'] == name:
                print(info)
    else:
        for info in all_info:
            print(info)

def get_device_id_by_name(name):
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info["name"] == name:
            p.terminate()
            return info["index"]
    p.terminate()

if __name__ == "__main__":
    # micro_name = "Microphone (Realtek(R) Audio)"
    # device_info_full(micro_name)
    # print(input_devices())
    for i in input_devices():
        print(i)
    # device_info()
    # print("_"*20)
    # print(sd.query_devices())