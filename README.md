# 🎤 Voice-to-Text Python Script  

This is a simple **Voice-to-Text converter** using **Vosk & Python**. It listens to audio from the microphone and converts speech into text in real-time.  

## 🚀 Features  
✅ Converts **live speech to text**  
✅ Works **offline** (no internet required)  
✅ Supports **multiple languages** (by changing the Vosk model)  
✅ Lightweight and **fast processing**  

---

## 🛠️ Installation  

### **1️⃣ Install Dependencies**  
Make sure you have **Python 3.8+** installed. Then, run:  
```sh
pip install vosk pyaudio

### **2️⃣ Download Vosk Model**
Visit 👉 Vosk Models
Download "vosk-model-small-en-us-0.15.zip" (for English)
Extract the folder and place it in C:\vosk-model\

---
## 🚀 Usage  

### Run the Script  
Once everything is set up, run the following command in your terminal:  

```sh
python speech_to_text.py

---
📌 Example Output

🎤 Listening... Speak now!
📝 You said: hello how are you
📝 You said: I need to buy groceries tomorrow

## 📌 How It Works
1️⃣ Captures voice input using pyaudio
2️⃣ Uses vosk for speech recognition
3️⃣ Converts spoken words into text
4️⃣ Displays the transcribed text in real-time

🎯 Supported Languages
Vosk supports multiple languages. You can change the model to Spanish, French, Hindi, or others by downloading the corresponding model.


 ## 👨‍💻 Author
🚀 Developed by Jaideep Yadav
📧 Contact: jaideepyadav611@gmail.com
🌍 GitHub: https://github.com/JaideepYadav
