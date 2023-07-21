from pytube import YouTube

def VideoInfo(video):
    print("Title: " + video.title)
    print("File name: " + video.default_filename)
    print("Size (mb): " + str(video.filesize_mb))

def DownloadVideo(link):
    yt = YouTube(link)
    yt = yt.streams.get_by_resolution("720p")

    try: 
        yt.download()
    except: 
        print("There was an error downloading the video " + yt.title)

    print("Download done successfully")
    VideoInfo(yt)

url = input("Enter the YouTube video URL: ")
DownloadVideo(url)
