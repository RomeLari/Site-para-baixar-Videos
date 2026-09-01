from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(output_path=save_path)
        msg_label.config(text="Download concluído!\nO vídeo foi salvo em:\n" + os.path.join(save_path, video.title + ".mp4"))
    except Exception as e:
        msg_label.config(text="Ocorreu um erro durante o download:\n" + str(e))

def browse_directory():
    save_path = filedialog.askdirectory()
    save_directory_entry.delete(0, tk.END)
    save_directory_entry.insert(0, save_path)

def download_button_clicked():
    video_url = video_url_entry.get()
    save_path = save_directory_entry.get()
    download_video(video_url, save_path)

# Configuração da janela principal
root = tk.Tk()
root.title("Download de Vídeo do YouTube")

# Entrada de URL do vídeo
video_url_label = tk.Label(root, text="Digite o link do vídeo do YouTube:")
video_url_label.pack()
video_url_entry = tk.Entry(root, width=50)
video_url_entry.pack()

# Botão de busca de diretório para salvar o vídeo
browse_button = tk.Button(root, text="Buscar Diretório", command=browse_directory)
browse_button.pack()

# Entrada do diretório de salvamento do vídeo
save_directory_entry = tk.Entry(root, width=50)
save_directory_entry.pack()

# Botão de download
download_button = tk.Button(root, text="Baixar Vídeo", command=download_button_clicked)
download_button.pack()

# Label para exibir mensagens
msg_label = tk.Label(root, text="", wraplength=300, justify="left")
msg_label.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()