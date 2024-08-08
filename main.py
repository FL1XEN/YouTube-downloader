import yt_dlp

ydl_opts = {
    'format': 'mp4',  # Загрузка в формате MP4
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=LGFOkToQbRk'])
