##### CONSTANTS ################
import threading
import sounddevice as sd
import librosa
import numpy as np
from keras.models import load_model


fs = 22050
seconds = 2

model = load_model("../wake_word_detection/audio\saved_model\WWD.h5")


##### LISTENING THREAD #########
def listener():
    while True:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
        mfcc_processed = np.mean(mfcc.T, axis=0)
        prediction_thread(mfcc_processed)






##### PREDICTION THREAD #############
def prediction(y, percent=0.95, wake_word_status=[]):
    prediction = model.predict(np.expand_dims(y, axis=0))
    print(f"prediction: {prediction[:, 1]}")
    # return prediction[:, 1] > 0.95
    # result_storage = prediction[:, 1] > percent
    if prediction[:, 1] > percent:
        print("Слухаю")
        wake_word_status.append(1)
    #   for i in range(100000):
    #         print("Hello")
        # speak("Hello")
    # else:
    #     print("0")

def voice_thread():
    # listen_thread_event = threading.Event()
    listen_thread = threading.Thread(target=listener, name="ListeningFunction")
    listen_thread.start()

def prediction_thread(y):
    pred_thread = threading.Thread(target=prediction, name="PredictFunction", args=(y,))
    pred_thread.start()

if __name__ == "__main__":
    voice_thread()

    # threading.Thread.getName()