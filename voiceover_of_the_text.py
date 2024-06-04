from gtts import gTTS  # You will also have to download 'ffmpeg' from the Internet to your computer
from audio_to_text import AudioText


# 3. Voiceover of text from a neural network

class Voiceover(AudioText):
    def __init__(self, file_name, language):
        self.file_name = file_name
        self.language = language

    def speak(self):
        try:
            with open(f"{self.file_name}.txt", "r", encoding="utf-8") as file:
                result = ' '.join(word.strip() for word in file.readlines())
        except Exception as Ex:
            return f"An error occurred while working with a text file: {Ex}"

        try:
            aud = gTTS(result, lang=self.language, slow=False)
            aud.save(f'{self.file_name}.mp3')  # You need to wait here too
            return "Recording completed successfully"
        except Exception as Ex:
            return f"An error occurred while working with audio: {Ex}"
