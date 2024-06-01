from tkinter import messagebox
from stream_downloader import download_stream

def download_video(app, yt):
    folder = app.folder_entry.get()
    if not folder:
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите папку для сохранения.")
        return
    
    chosen_resolution = app.video_quality_combobox.get()
    if not chosen_resolution:
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите качество видео.")
        return

    video_stream = next(stream for stream in app.video_streams if stream.resolution == chosen_resolution)
    download_stream(app, yt, video_stream, folder, yt.title + ".mp4")

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