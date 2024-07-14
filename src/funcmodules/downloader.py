import re
import os
from pathlib import Path
import subprocess
from time import sleep
from pytube import YouTube

from __main__ import display_menu

yt_available = False
in_available = True
tt_available = True

def get_download_folder():
    if os.name == 'nt':  # Windows
        download_folder = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
    else:  # macOS, Linux
        download_folder = os.path.join(os.getenv('HOME'), 'Downloads')
    return download_folder

def identify_platform(url):
    youtube_pattern = r'(https?://)?(www\.)?(youtube|youtu\.be)(\.com)?/.*'
    instagram_pattern = r'(https?://)?(www\.)?instagram\.com/.*'
    tiktok_pattern = r'(https?://)?(www\.)?tiktok\.com/.*'

    if re.match(youtube_pattern, url):
        return 'YouTube'
    elif re.match(instagram_pattern, url):
        return 'Instagram'
    elif re.match(tiktok_pattern, url):
        return 'TikTok'
    else:
        return 'Unknown'

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'Download fortschritt: {percentage_of_completion:.2f}%')

def download_video(url):
    platform = identify_platform(url)
    download_folder = get_download_folder()

    if platform == 'YouTube':
        if not yt_available: 
            print('YouTube not available')
            sleep(3)
            display_menu()
        yt = YouTube(url)
        print(f'Titel: {yt.title}')
        yt.register_on_progress_callback(on_progress)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path='Pfad_zum_Download-Ordner')
        print(f'Download abgeschlossen: {yt.title}')
    elif platform == 'Instagram':
        if not in_available: 
            print('Instagram not available')
            sleep(3)
            display_menu()
        import instaloader
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
        L.download_post(post, target=download_folder)
        print('Download abgeschlossen!')
    elif platform == 'TikTok':
        if not tt_available: 
            print('TikTok not available')
            sleep(3)
            display_menu()
        from TikTokApi import TikTokApi
        api = TikTokApi()
        video_data = api.video(url=url).bytes()
        with open(os.path.join(download_folder, "tiktok_video.mp4"), "wb") as file:
            file.write(video_data)
        print('Download abgeschlossen!')
    else:
        print('Unbekannte Plattform oder ungültige URL.')

def download():
    url = input("Insert the URL of the Video: ")
    download_video(url)
    