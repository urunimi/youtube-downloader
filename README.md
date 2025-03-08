# Youtube Donwloader

This repository contains a Python project for downloading all the videos from a Youtube video or a YouTube playlist. The original script has been updated to use `yt_dlp` (instead of the outdated `pytube`) to handle the download and conversion process.

## Features

- **Playlist Downloads:** Downloads all videos from a given YouTube playlist URL. (Also supports downloading a Youtube video)
- **Folder Naming:** Converts the playlist title into an alphanumeric folder name to store downloaded videos.
- **High Resolution:** Downloads each video with the highest available resolution.
- **Real-Time Updates:** The GUI provides real-time download progress and error reporting.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/urunimi/youtube-downloader.git
cd youtube-downloader
```

2. Set up a virtual environment (recommended):

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface (CLI)

1. Run the CLI script:

```bash
python main.py
```

2. Follow the prompt:

   + Enter the YouTube playlist URL when prompted.
   + The script will create a folder (named by the sanitized playlist title and download all videos into it.
   + Progress updates and video size details are displayed in the terminal.

## Known Errors

### CLI

+ **Folder Already Exists**:

If a folder with the same name as the playlist already exists, the script will throw an error because it cannot recreate the folder. To resolve, delete or rename the existing folder before running the script.

## Additional Notes
+ The project now uses `yt_dlp` for improved compatibility and performance compared to the legacy `pytube` library.
+ For cross-platform builds, remember that executables are OS specific. Currently, only the Ubuntu executable is provided (built with PyInstaller on Ubuntu).

## Resources
+ [yt_dlp Documentation](https://github.com/yt-dlp/yt-dlp)
+ [PyQt5 Documentation](https://www.riverbankcomputing.com/software/pyqt/intro)
