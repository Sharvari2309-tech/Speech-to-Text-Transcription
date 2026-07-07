
import speech_recognition as sr

import os
import logging
import time
from datetime import datetime


# -----------------------------
# Configure Logger
# -----------------------------
def setup_logger():
    """
    Creates a log file inside the logs folder.
    """

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Application Started")


# -----------------------------
# List Available Audio Files
# -----------------------------
def list_audio_files(folder="audio"):
    """
    Returns all WAV audio files inside the audio folder.
    """

    if not os.path.exists(folder):
        return []

    files = [
        file for file in os.listdir(folder)
        if file.lower().endswith(".wav")
    ]

    return files


# -----------------------------
# Convert Speech to Text
# -----------------------------
def speech_to_text(audio_path):
    """
    Converts speech from an audio file into text.
    Returns transcript and processing time.
    """

    recognizer = sr.Recognizer()

    start_time = time.time()

    try:

        with sr.AudioFile(audio_path) as source:

            logging.info(f"Reading audio file: {audio_path}")

            audio = recognizer.record(source)

            logging.info("Audio successfully loaded.")

            text = recognizer.recognize_google(audio)

            end_time = time.time()

            logging.info("Speech converted successfully.")

            return text, round(end_time - start_time, 2)

    except sr.UnknownValueError:

        logging.error("Speech could not be understood.")

        return "Speech could not be understood.", 0

    except sr.RequestError:

        logging.error("Internet connection required.")

        return "Internet connection required.", 0

    except FileNotFoundError:

        logging.error("Audio file not found.")

        return "Audio file not found.", 0

    except Exception as e:

        logging.error(str(e))

        return f"Unexpected Error: {e}", 0


# -----------------------------
# Save Transcript
# -----------------------------
def save_transcript(text):
    """
    Saves transcript with current date and time.
    """

    os.makedirs("output", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"output/transcript_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write(text)

    logging.info(f"Transcript saved as {filename}")

    return filename


# -----------------------------
# Display Statistics
# -----------------------------
def display_statistics(text, processing_time):
    """
    Displays useful statistics.
    """

    words = len(text.split())

    characters = len(text)

    print("\n" + "=" * 45)

    print("TRANSCRIPTION STATISTICS")

    print("=" * 45)

    print(f"Words            : {words}")

    print(f"Characters       : {characters}")

    print(f"Processing Time  : {processing_time} seconds")

    print("=" * 45)


# -----------------------------
# Display Transcript
# -----------------------------
def display_transcript(text):
    """
    Prints transcript in a clean format.
    """

    print("\n" + "=" * 45)

    print("TRANSCRIPT")

    print("=" * 45)

    print(text)

    print("=" * 45)