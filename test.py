from pydub import AudioSegment

# Пути к тестовому файлу и выходному файлу
input_path = "E:\\YoutubePy\\1.webm"
output_path = "E:\\YoutubePy\\1.mp3"

try:
    # Чтение и конвертация аудио
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="mp3")
    print("Конвертация завершена. Файл сохранен в:", output_path)
except Exception as e:
    print("Ошибка конвертации:", str(e))