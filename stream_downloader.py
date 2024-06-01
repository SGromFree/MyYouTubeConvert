import os
from tkinter import Tk, ttk
from pytube import YouTube
from stream_downloader import download_stream

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        # Установим путь к папке сохранения
        self.default_folder = "E:\\YoutubePy\\downloads"

        self.download_audio_button = ttk.Button(root, text="Скачать аудио", command=self.download_audio)
        self.download_audio_button.pack()

    def download_audio(self):
        url = "https://www.youtube.com/watch?v=some_video_id"  # Пример URL видео
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()  # Получение аудиопотока
        filename = yt.title + ".webm"  # Имя файла

        download_stream(self, yt, audio_stream, self.default_folder, filename)

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()