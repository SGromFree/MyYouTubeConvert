import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pytube import YouTube
from download_video import download_video, download_audio

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        self.yt = None  # Инициализация yt здесь

        # Адрес ссылки на видео
        self.url_label = ttk.Label(root, text="Видео ссылка:")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=3)

        # Контекстное меню для URL Entry 
        self.url_menu = tk.Menu(self.root, tearoff=0)
        self.url_menu.add_command(label="Вырезать", command=self.cut)
        self.url_menu.add_command(label="Копировать", command=self.copy)
        self.url_menu.add_command(label="Вставить", command=self.paste)
        self.url_entry.bind("<Button-3>", self.show_url_context_menu)

        # Выбор качества видео
        self.video_quality_label = ttk.Label(root, text="Качество видео:")
        self.video_quality_label.grid(row=1, column=0, padx=10, pady=10)
        self.video_quality_combobox = ttk.Combobox(root)
        self.video_quality_combobox.grid(row=1, column=1, padx=10, pady=10)

        # Выбор качества аудио
        self.audio_quality_label = ttk.Label(root, text="Качество аудио:")
        self.audio_quality_label.grid(row=1, column=2, padx=10, pady=10)
        self.audio_quality_combobox = ttk.Combobox(root)
        self.audio_quality_combobox.grid(row=1, column=3, padx=10, pady=10)
        
        # Кнопка для получения качества
        self.quality_button = ttk.Button(root, text="Получить качество", command=self.get_quality)
        self.quality_button.grid(row=1, column=4, padx=10, pady=10)
        
        # Выбор папки для сохранения
        self.folder_label = ttk.Label(root, text="Папка для сохранения:")
        self.folder_label.grid(row=2, column=0, padx=10, pady=10)
        self.default_folder = "E:\\YoutubePy\\downloads"
        self.folder_entry = ttk.Entry(root, width=50)
        self.folder_entry.insert(0, self.default_folder)
        self.folder_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        self.folder_button = ttk.Button(root, text="Выбрать...", command=self.choose_folder)
        self.folder_button.grid(row=2, column=3, padx=10, pady=10)

        # Прогресс бар
        self.progress = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
        self.progress.grid(row=3, column=0, columnspan=5, pady=10)

        # Кнопка для скачивания видео
        self.download_video_button = ttk.Button(root, text="Скачать видео", command=lambda: self.download_video(self.yt))
        self.download_video_button.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        # Кнопка для скачивания аудио
        self.download_audio_button = ttk.Button(root, text="Скачать аудио", command=lambda: self.download_audio(self.yt))
        self.download_audio_button.grid(row=4, column=3, padx=10, pady=10, sticky="ew")

        # Кнопка выхода
        self.exit_button = ttk.Button(root, text="Выход", command=root.quit)
        self.exit_button.grid(row=5, column=2, padx=10, pady=10)

    def cut(self):
        self.url_entry.event_generate("<<Cut>>")

    def copy(self):
        self.url_entry.event_generate("<<Copy>>")

    def paste(self):
        self.url_entry.event_generate("<<Paste>>")

    def show_url_context_menu(self, event):
        self.url_menu.post(event.x_root, event.y_root)

    def get_quality(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Предупреждение", "Пожалуйста, введите ссылку на видео.")
            return
        try:
            self.yt = YouTube(url, on_progress_callback=self.on_progress)  # Инициализация yt здесь

            # Получаем доступные качества видео
            self.video_streams = self.yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
            self.audio_streams = self.yt.streams.filter(only_audio=True).order_by('abr').desc()

            # Заполняем комбобоксы
            self.video_quality_combobox['values'] = [stream.resolution for stream in self.video_streams]
            self.audio_quality_combobox['values'] = [stream.abr for stream in self.audio_streams]

            # Выставляем максимальное качество по умолчанию
            if self.video_quality_combobox['values']:
                self.video_quality_combobox.current(0)
            if self.audio_quality_combobox['values']:
                self.audio_quality_combobox.current(0)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось получить качество видео: {e}")

    def download_video(self, yt):
        download_video(self, yt)

    def download_audio(self, yt):
        download_audio(self, yt)

    def choose_folder(self):
        folder = filedialog.askdirectory(initialdir=self.default_folder)
        if folder:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder)

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress['value'] = percentage
        self.root.update_idletasks()