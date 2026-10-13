from pytube import YouTube

# Create a YouTube object
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
yt = YouTube(url)

print(f"Title: {yt.title}")
print(f"Views: {yt.views}")

# Download the highest resolution progressive stream
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download complete!")