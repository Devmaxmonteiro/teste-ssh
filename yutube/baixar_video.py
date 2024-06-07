from pytube import YouTube

# Função para baixar vídeo do YouTube
def baixar_video(url, caminho_destino='.'):
    try:
        yt = YouTube(url)
        print(f"Baixando: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=caminho_destino)
        print(f"Download concluído! Vídeo salvo em: {caminho_destino}/{yt.title}.mp4")
    except Exception as e:
        print(f"Erro ao baixar vídeo: {e}")

# URL do vídeo que você deseja baixar
url_video = 'https://www.youtube.com/watch?v=0_kpZV_Ss7E&t=3177s'  # Substitua pela URL do vídeo desejado
caminho_destino = '.'  # Diretório onde o vídeo será salvo

# Chamando a função para baixar o vídeo
baixar_video(url_video, caminho_destino)
