from pydub import AudioSegment
import os
import math

# Функция для разделения файла на части
def split_audio_file(input_path, output_dir, chunk_size_mb=99):
    try:
        # Загрузка аудио файла
        audio = AudioSegment.from_file(input_path)

        # Общая длина файла в миллисекундах и его размер в байтах
        total_length_ms = len(audio)
        total_size_bytes = audio.frame_count() * audio.frame_width  # Определить общий размер в байтах
        chunk_size_bytes = chunk_size_mb * 1024 * 1024  # Размер чанка в байтах

        # Расчет приблизительной длины чанка в миллисекундах
        chunk_length_ms = math.ceil(total_length_ms * (chunk_size_bytes / total_size_bytes))

        # Создание выходной директории, если она не существует
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Разделение и сохранение чанков
        for i in range(0, total_length_ms, chunk_length_ms):
            chunk = audio[i:i + chunk_length_ms]
            chunk_name = os.path.join(output_dir, f"chunk_{i // chunk_length_ms + 1}.webm")
            chunk.export(chunk_name, format="webm")
            print(f"Чанк сохранен: {chunk_name}")
        
        print("Разделение завершено.")
        
    except Exception as e:
        print("Произошла ошибка при разделении файла:", str(e))

# Пути к входному файлу и выходной директории
input_path = "E:\\YoutubePy\\downloads\\1.webm"
output_dir = "E:\\YoutubePy\\downloads\\chunks"

# Вызов функции для разделения файла
split_audio_file(input_path, output_dir)