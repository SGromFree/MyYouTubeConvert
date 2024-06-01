from tkinter import messagebox
from pytube import YouTube

def get_quality(app):
    url = app.url_entry.get()
    if not url:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите ссылку на видео.")
        return
    try:
        global yt 
        yt = YouTube(url, on_progress_callback=app.on_progress)

        # Получаем доступные качества видео
        app.video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        app.audio_streams = yt.streams.filter(only_audio=True).order_by('abr').desc()

        # Заполняем комбобоксы
        app.video_quality_combobox['values'] = [stream.resolution for stream in app.video_streams]
        app.audio_quality_combobox['values'] = [stream.abr for stream in app.audio_streams]

        # Выставляем максимальное качество по умолчанию
        if app.video_quality_combobox['values']:
            app.video_quality_combobox.current(0)
        if app.audio_quality_combobox['values']:
            app.audio_quality_combobox.current(0)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось получить качество видео: {e}")