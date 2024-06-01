from tkinter import messagebox
import os
from stream_downloader import download_stream

def download_audio(app, yt):
    folder = app.folder_entry.get()
    if not folder:
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите папку для сохранения.")
        return

    chosen_abr = app.audio_quality_combobox.get()
    if not chosen_abr:
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите качество аудио.")
        return

    audio_stream = next(stream for stream in app.audio_streams if stream.abr == chosen_abr)
    download_stream(app, yt, audio_stream, folder, yt.title + ".webm", audio_only=True)