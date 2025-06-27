import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile

def record_audio(filename="input.wav", duration=5, samplerate=16000):
    print("🎙️ Recording... Speak now.")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
    sd.wait()
    scipy.io.wavfile.write(filename, samplerate, audio)
    print("✅ Saved to", filename)

def transcribe_audio(filename="input.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    print("🧠 Transcribed Text:", result["text"])
    return result["text"]

if __name__ == "__main__":
    record_audio()
    transcribe_audio()
