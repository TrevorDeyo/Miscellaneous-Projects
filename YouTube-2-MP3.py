from pytube import YouTube

video_url = input("Enter the URL of the YouTube video: ")
yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()
filename = f"{yt.title}.mp4"
video.download(filename=filename)
print(f"Download complete: {filename}")

# so this is technically a mp4 with the video stripped I think?