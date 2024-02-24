from pytube import YouTube
import os


def download_video(link):
    yt = YouTube(link)

    default_path = os.path.join(os.getcwd(), 'static')
    default_file = os.path.join(os.getcwd(), 'static')
    if os.path.isfile(default_file):
        pass
    else:
        try:
            video = yt.streams.filter(only_audio=False).first()
            out_file = video.download(output_path=default_path)
        except:
            print('file already exists')
    file_name = out_file.split('\\')[-1]
    return out_file, file_name
    # save the file
