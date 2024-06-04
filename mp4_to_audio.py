from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import os


# 1. Converting video to audio


class VideoAud:
    @staticmethod
    def extract_audio_from_video_with_pydub(video_filepath, output_audio_filepath):
        video_clip = VideoFileClip(video_filepath)
        temp_audio_filepath = "temp_audio.mp3"
        video_clip.audio.write_audiofile(temp_audio_filepath)

        audio = AudioSegment.from_file(temp_audio_filepath)
        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)

        audio.export(output_audio_filepath, format="wav", parameters=["-acodec", "pcm_s16le"])
        os.remove(temp_audio_filepath)

    def launch(self):
        video_filepath = 'files/video2.mp4'  # transfer your downloaded videos to the 'files' directory
        output_audio_filepath = 'files/output_audio.wav'  # the resulting audio file will be in the same directory
        self.extract_audio_from_video_with_pydub(video_filepath, output_audio_filepath)
