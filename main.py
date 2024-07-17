from pytube import Playlist
import os
from os import listdir

DOWNLOADS_DIR = 'e:/Downloads'

def remove_mp4_files(folder_path):
    for file_name in listdir(folder_path):
        if file_name.endswith(".mp4"):
            os.remove(folder_path + "/" + file_name)
def convert_mp4_to_mp3(file):
    base, ext = os.path.splitext(file)
    if ext == ".mp4":
        print("Converting {0} into mp3 file".format(os.path.basename(file)))
        os.system('ffmpeg -i "{mp4}" -f mp3 "{mp3}.mp3" -loglevel warning'
                  .format(mp4=file, mp3=base))



def download_playlist_as_mp3(url):
    playlist = Playlist(url)
    playlist_dir = DOWNLOADS_DIR + '/' + playlist.title
    os.makedirs(playlist_dir, exist_ok=True)
    try:
        for video in playlist.videos:
            try:
                video_to_download = video.streams.filter(only_audio=True).first()
                print('Downloading audio of ' + video_to_download.title)
                file = video_to_download.download(playlist_dir)
                convert_mp4_to_mp3(file)
            except Exception as e:
                print("Could not download audio. Reason: " + repr(e))

    # cleanup
    finally:
        remove_mp4_files(playlist_dir)


if __name__ == '__main__':
    url = str(input("Enter the URL of the playlist you want to download: \n>> "))
    download_playlist_as_mp3(url)


