import os
import pyaudio
import json
from vosk import Model, KaldiRecognizer

# ✅ Set the correct model path (update if needed)
MODEL_PATH = "C:/vosk_model/vosk-model-small-en-us-0.15"

# Check if the model exists
if not os.path.exists(MODEL_PATH):
    print("❌ Model not found! Make sure you downloaded and extracted it correctly.")
    exit(1)

# ✅ Load the Vosk speech model
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# ✅ Initialize microphone
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
stream.start_stream()

print("🎤 Listening... Speak now!")

# ✅ Convert speech to text
while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        print("📝 You said:", result["text"])  # Display recognized text
