from pytube import YouTube

def download_video(link):
    try:
        # Create a YouTube object with the video URL
        video = YouTube(link)
        
        # Get the highest resolution stream
        highest_resolution_stream = video.streams.get_highest_resolution()
        
        # Download the video
        highest_resolution_stream.download()
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")
download_video(video_url)