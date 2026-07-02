from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
from transcriber import transcribe_audio
from segment_picker import pick_viral_segments
from content_writer import generate_content
from video_clipper import clip_video
import os

load_dotenv()

VIDEO_PATH = "youtube_to_reels/input/my_video.mp4"
AUDIO_PATH = "youtube_to_reels/temp/audio.mp3"
OUTPUT_DIR = "youtube_to_reels/output"

# Step 1: Audio extract
print("=== Step 1: Extracting Audio ===")
video = VideoFileClip(VIDEO_PATH)
video.audio.write_audiofile(AUDIO_PATH)
video.close()

# Step 2: Transcribe
print("=== Step 2: Transcribing ===")
transcript = transcribe_audio(AUDIO_PATH)

# Step 3: Find viral segments
print("=== Step 3: Finding Viral Segments ===")
segments = pick_viral_segments(transcript["text"])

# Step 4: Generate content + clip video for each segment
for i, segment in enumerate(segments):
    print(f"\n=== Reel {i+1} ===")

    # Content generate karo
    content = generate_content(segment)

    # Folder banao
    reel_folder = f"{OUTPUT_DIR}/reel_{i+1}"
    os.makedirs(reel_folder, exist_ok=True)

    # Video clip karo
    clip_video(VIDEO_PATH, segment["start_time"], segment["end_time"], f"{reel_folder}/clip.mp4")

    # Content file save karo
    with open(f"{reel_folder}/content.txt", "w", encoding="utf-8") as f:
        f.write(f"HEADLINE: {content['viral_headline']}\n\n")
        f.write(f"CAPTION: {content['caption']}\n\n")
        f.write(f"SUMMARY: {content['summary']}\n\n")
        f.write(f"B-ROLL: {content['broll']}\n")

    print(f"Reel {i+1} complete!")

print("\n✅ All 5 Reels Generated Successfully!")
