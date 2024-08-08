import yt_dlp  # type: ignore

ydl_opts = {

    'format': 'mp4',  # format
    # 'merge_output_format': 'mp4',  # Merge into MP4
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Convert in MP4
    }],
    'outtmpl': '%(title)s.%(ext)s',  # FILE_NAME === TITLE_NAME
    # Download status
    'progress_hooks': [lambda d: print(f"Progress: {d.get('status', 'Unknown')}")],
    'noplaylist': True,  # Download one video if URL is playlist
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=LGFOkToQbRk'])
