from pytube import Search, YouTube
import os
import shutil

def get_video_id(name: str):
  s = Search(f"{name}")
  yt_id = s.results
  video_ids = [video.video_id for video in yt_id]

  return str(video_ids[0])

def give_link(name: str):
  video_id = get_video_id(name)
  base_url = f"https://www.youtube.com/watch?v={video_id}"
  return base_url

def download_vid(name: str):
  video_id = get_video_id(name)
  base_url = f"https://www.youtube.com/watch?v={video_id}"
  yt = YouTube(base_url)
  audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first() #downloading the first Result and only mp4
  audio_stream.download(output_path='music')

def delete_audio():
  shutil.rmtree('music')

def find_music_name():
  return os.listdir("music")[0]

def remove_all_files(dir):
  for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))