from vosk import Model, KaldiRecognizer
from mp4_to_audio import VideoAud
import wave

# 2. converting audio to text


model_path = 'model/vosk-model-ru'  # download vosk model that you need from Internet and transfer it to the 'model' directory

model = Model(model_path)


class AudioText(VideoAud):
    @staticmethod
    def transcribe_audio(file_path):
        wf = wave.open(file_path, "rb")
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                print("Proccesing...")  # If you saw red lines agt the beginning, then everything is fine
                # Remember that this is a slow process, just wait
        result = rec.FinalResult()
        return result

    def text_to_file(self):
        audio_file_path = 'files/output_audio.wav'
        text = self.transcribe_audio(audio_file_path)

        with open("transcribed_text.txt", "w") as text_file:
            text_file.write(text)
            print("The text was successfully saved to file 'transcribed_text.txt'.")
        # You will need to extract all the text from the file after the "text:" and transfer it to a new text file,
        # which you put in the same space as the project
