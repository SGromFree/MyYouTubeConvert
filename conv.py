import subprocess
import os

def convert(in_file, out_file):
    # Формирование команды для конвертации
    cmd = f"ffmpeg -i \"{in_file}\" -vn -ab 128k -ar 44100 -y \"{out_file}\""
    
    # Вызов команды через subprocess.run()
    subprocess.run(cmd, shell=True)

# Пути к входному и выходному файлам
input_path = "E:\\YoutubePy\\downloads\\1.webm"
output_path = "E:\\YoutubePy\\downloads\\1.mp3"

# Выполнение конвертации
convert(input_path, output_path)

print(f"Конвертация завершена. Файл сохранен в: {output_path}")