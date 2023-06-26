import yt_dlp

# Create a yt_dlp object
ydl = yt_dlp.YoutubeDL()

# Set the options for downloading audio only in MP3 format
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': r'%(title)s.%(ext)s',
}

# Specify the playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=PL4waBsMLGZzJrLloEMSAf3bqQF48QqvIk'

# Download the playlist
with ydl:
    ydl.download([playlist_url])
