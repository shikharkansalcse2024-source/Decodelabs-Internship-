import os
import subprocess
import shutil

FFMPEG_PATH = shutil.which("ffmpeg") or r"C:\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe"

def clip_video(video_path, start_time, end_time, output_path):
    try:
        print(f"Clipping {start_time}s to {end_time}s...")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        duration = end_time - start_time

        command = [
            FFMPEG_PATH, "-y",
            "-i", video_path,
            "-ss", str(start_time),
            "-t", str(duration),
            "-vcodec", "libx264",
            "-acodec", "aac",
            output_path
        ]

        subprocess.run(command, check=True)
        print(f"Saved: {output_path}")

    except Exception as e:
        print(f"Error: {e}")
