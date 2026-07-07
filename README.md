#  Speech-to-Text Transcription

A Python application that converts spoken audio into text using the SpeechRecognition library.

---

##  Features

- Convert `.wav` audio files to text
- Automatic audio file detection
- Timestamped transcript files
- Word count
- Character count
- Processing time
- Logging support
- Clean modular code

---

##  Project Structure

```
Speech-to-Text/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
│
├── audio/
│
├── output/
│
├── logs/
│
└── screenshots/
```

---

##  Libraries Used

- SpeechRecognition
- os
- logging
- datetime
- time

---

##  Installation

Clone the repository.

Install dependencies.

```bash
pip install -r requirements.txt
```

---

##  Run the Project

```bash
python app.py
```

---

##  Output

The program will

- Detect audio files
- Convert speech to text
- Display the transcript
- Save it inside the output folder
- Show transcription statistics

---

##  Output Files

Transcript files are automatically saved inside

```
output/
```

Example

```
transcript_20260706_151520.txt
```

---

##  Log File

Application logs are stored inside

```
logs/app.log
```

---

##  Screenshots
<img width="1920" height="1080" alt="Screenshot (230)" src="https://github.com/user-attachments/assets/39d07aa7-a4d9-4474-a260-829ef0f1bbad" />


---

##  Future Improvements

- Microphone support
- GUI using Streamlit or Tkinter
- Support for MP3 files
- Multiple language recognition
- Speaker identification

---

##  Author

Sharvari Marathe
