from tkinter import messagebox
import os
import re

def clean_filename(filename):
    # Удаляем нелегальные символы
    return re.sub(r'[\/:*?"<>|]', '_', filename)

def download_stream(app, yt, stream, folder, filename, audio_only=False):
    try:
        # Очищаем имя файла
        filename = clean_filename(filename)
        
        # Скачиваем поток
        stream.download(output_path=folder, filename=filename)
        messagebox.showinfo("Успех", f"Загрузка завершена: {filename}")

        if audio_only:
            convert_to_audio(os.path.join(folder, filename))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

def convert_to_audio(file_path):
    # Пример функции конвертации видео в аудио (если требуется)
    pass