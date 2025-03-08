import os
from io import UnsupportedOperation

import yt_dlp


class YPDownloader:
    def __init__(self, url: str, format: str = "mp4"):
        self.url = url
        self.format = format
        if format == "mp3":
            ydl_format = "bestaudio/best"
            postprocessors = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        elif format == "mp4":
            ydl_format = "bestvideo+bestaudio/best"
            postprocessors = [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]

        self.ydl_opts = {
            "format": ydl_format,
            "merge_output_format": format,
            "outtmpl": "%(title)s.%(ext)s",
            "noplaylist": False,
            "quiet": False,
            "postprocessors": postprocessors,
        }

    def make_alpha_numeric(self, string: str):
        return "".join(char for char in string if char.isalnum())

    def run(self):
        format = self.format
        ydl_opts = self.ydl_opts

        if "list" in self.url: 
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                playlist_info = ydl.extract_info(self.url, download=False)
                playlist_title = self.make_alpha_numeric(playlist_info["title"])

                if not os.path.exists(playlist_title):
                    os.mkdir(playlist_title)

                totalVideoCount = len(playlist_info["entries"])
                padding_digits = len(str(totalVideoCount))  # Calculate required padding
                print("Total videos in playlist: 🎦", totalVideoCount)

                for index, video in enumerate(playlist_info["entries"], start=1):
                    # Update outtmpl for each video using the local index
                    ydl_opts["outtmpl"] = os.path.join(
                        playlist_title,
                        f"{index:0{padding_digits}d} - %(title)s.%(ext)s"
                    )
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl2:
                        try:
                            print(f"\nDownloading: {video['title']}")
                            ydl2.download([video["webpage_url"]])  # Use 'webpage_url' here
                            print(f"Downloaded: {video['title']} ✨ successfully!")
                            print("Remaining Videos:", totalVideoCount - index)
                        except Exception as e:
                            print(f"Error downloading {video['title']}: {e}")
        else:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
        print("\nAll videos downloaded successfully! 🎉")


playlist = input("Enter YouTube URL(playlist can be supported): ✨")
file_type = input("video(v) / audio(a)? ")
if file_type.startswith("v"):
    format = "mp4"
elif file_type.startswith("a"):
    format = "mp3"
else:
    raise UnsupportedOperation("only video / audio are supported")
YPDownloader(playlist, format).run()
