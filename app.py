from utils import (
    setup_logger,
    list_audio_files,
    speech_to_text,
    save_transcript,
    display_statistics,
    display_transcript
)
import os


def main():

    # Start logger
    setup_logger()

    print("=" * 50)
    print("       SPEECH TO TEXT TRANSCRIPTION")
    print("=" * 50)

    # Get available audio files
    audio_files = list_audio_files()

    if not audio_files:
        print("\nNo .wav files found inside the 'audio' folder.")
        return

    print("\nAvailable Audio Files:\n")

    for index, file in enumerate(audio_files, start=1):
        print(f"{index}. {file}")

    # Take user input
    while True:
        try:
            choice = int(input("\nEnter the file number: "))

            if 1 <= choice <= len(audio_files):
                break

            print("Please enter a valid number.")

        except ValueError:
            print("Please enter numbers only.")

    selected_file = audio_files[choice - 1]

    audio_path = os.path.join("audio", selected_file)

    print("\nReading Audio...")

    transcript, processing_time = speech_to_text(audio_path)

    display_transcript(transcript)

    display_statistics(transcript, processing_time)

    saved_file = save_transcript(transcript)

    print(f"\nTranscript saved successfully!")

    print(f"Location: {saved_file}")

    print("\nThank you for using Speech-to-Text Converter.")


if __name__ == "__main__":
    main()