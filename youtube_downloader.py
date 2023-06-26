import pytube

# Inputting or manuel writing str links
link = "https://www.youtube.com/watch?v=j32RezXacYM"

# Create a Youtube object with link
yt = pytube.YouTube(link)

# Printing all streams of link and filtering some features
print(yt.streams.filter(mime_type="video/mp4", type="video", res="2160p"))
#print(yt.streams.filter(mime_type="video/mp4", type="video", progressive="True", res="720p"))

#high_quality_stream = yt.streams.filter(mime_type="video/mp4", type="video", progressive="True", res="720p")[0]
#high_quality_stream.download()

# Create a variable filtering stream some features (Returned a list and take the first index)
res_2160p_stream = yt.streams.filter(mime_type="video/mp4", type="video", res="2160p")[0]

# Download the video
res_2160p_stream.download()

#print(yt.streams.first())

#yt.streams.filter(res="1080p",mime_type="video/mp4").download()

print("Downloaded")