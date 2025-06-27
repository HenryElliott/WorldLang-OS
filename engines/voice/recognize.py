import whisper, sounddevice as sd, numpy as np, scipy.io.wavfile as wav

def record(filename="voice.wav", duration=5, rate=16000):
    print("🎙️ Recording...")
    audio = sd.rec(int(duration * rate), samplerate=rate, channels=1)
    sd.wait()
    wav.write(filename, rate, audio)
    return filename

def transcribe(file="voice.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(file)
    return result['text']

if __name__ == "__main__":
    print(transcribe(record()))
