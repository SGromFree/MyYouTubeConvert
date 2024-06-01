from pydub import AudioSegment
from tqdm import tqdm
import os
from ffmpy import FFprobe

def get_file_size(input_path):
    output = os.popen(f'ffprobe -v error -select_streams a:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 "{input_path}"').read()
    duration = float(output.strip())
    return duration * 1024 * 1024

def convert_with_progress(input_path, output_path):
    try:
        # Чтение входного файла аудио
        audio = AudioSegment.from_file(input_path)
        
        # Получение информации о файле
        total_length = len(audio)  # Длина файла в миллисекундах
        file_size = get_file_size(input_path)
        chunk_size = 1000  # Размер чанка в миллисекундах

        print("Начало конвертации...")

        # Создание пустого аудиофайла для записи конвертированных чанков
        output_audio = AudioSegment.empty()

        with tqdm(total=file_size, unit='B', unit_scale=True, desc='Конвертация аудио', ncols=100) as pbar:
            for i in range(0, total_length, chunk_size):
                chunk = audio[i:i + chunk_size]
                output_audio += chunk  # Добавление текущего чанка к итоговому аудио
                pbar.update(chunk_size)

        # Экспорт итогового аудио в MP3 формат
        output_audio.export(output_path, format="mp3")

        print("Конвертация завершена. Файл сохранен в:", output_path)
    except Exception as e:
        print("Ошибка конвертации:", str(e))

# Пути к тестовому файлу и выходному файлу
input_path = "E:\\YoutubePy\\downloads\\1.webm"
output_path = "E:\\YoutubePy\\downloads\\1.mp3"

convert_with_progress(input_path, output_path)