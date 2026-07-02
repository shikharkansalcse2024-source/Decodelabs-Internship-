# YouTube to Reels Automation

Automatically converts a long-form YouTube video into 5 short, viral-ready Reels — complete with captions, summaries, viral headlines, and B-roll suggestions.

## What this project does

1. Extracts audio from a video file
2. Transcribes the audio to text using Whisper (runs locally, free)
3. Uses an AI model (Groq - Llama 3.3) to find the 5 most "viral" segments in the transcript
4. Generates a viral headline, social media caption, summary, and B-roll suggestion for each segment
5. Cuts the original video into 5 short clips matching those segments
6. Saves everything neatly into an output folder

## Tech stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Whisper (local) | Speech-to-text transcription |
| Groq API (Llama 3.3 70B) | Finding viral segments + writing content |
| FFmpeg | Cutting video clips with audio |
| python-dotenv | Securely loading API keys |

## Folder structure

```
youtube_to_reels/
├── input/
│   └── my_video.mp4          ← put your source video here
├── output/
│   ├── reel_1/
│   │   ├── clip.mp4
│   │   └── content.txt       ← headline, caption, summary, B-roll
│   ├── reel_2/
│   ├── reel_3/
│   ├── reel_4/
│   └── reel_5/
├── temp/
│   └── audio.mp3              ← extracted audio (temporary)
├── .env                        ← API keys (never share this file)
├── main.py                     ← runs the entire pipeline
├── transcriber.py               ← Module: Whisper transcription
├── segment_picker.py            ← Module: finds viral segments
├── content_writer.py            ← Module: generates captions/headlines
└── video_clipper.py             ← Module: cuts video clips with FFmpeg
```

## Setup

### 1. Install Python
Download from [python.org](https://python.org) (3.10+).

### 2. Install FFmpeg
Make sure FFmpeg is installed. If it isn't on your system PATH, note its full
install path — you'll need it in `video_clipper.py`.

### 3. Install Python libraries
```bash
pip install openai-whisper groq python-dotenv moviepy
```

### 4. Get a Groq API key (free)
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up and create an API key

### 5. Create a `.env` file
In the project root, create a `.env` file with:
```
GROQ_API_KEY=your_groq_key_here
```

### 6. Set your FFmpeg path
Open `video_clipper.py` and update this line with your FFmpeg install path:
```python
FFMPEG_PATH = r"C:\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe"
```

## How to use

1. Place your video inside the `input/` folder and rename it `my_video.mp4`
2. Run:
```bash
python main.py
```
3. Wait for the pipeline to finish — it will print progress for each step
4. Check the `output/` folder — you'll find 5 reel folders, each containing:
   - `clip.mp4` — the short video clip (with audio)
   - `content.txt` — viral headline, caption, summary, and B-roll suggestion

## To process a new video

1. Delete the old video from `input/`
2. Add the new video and rename it `my_video.mp4`
3. Run `python main.py` again

## How each module works

**transcriber.py** — Loads a local Whisper model and converts the extracted
audio into text.

**segment_picker.py** — Sends the full transcript to an AI model and asks it
to identify the 5 most engaging/shareable moments, returning start time, end
time, and the reason each is viral.

**content_writer.py** — For each segment, asks the AI model to write a viral
headline, a social caption with hashtags, a short summary, and a B-roll
visual suggestion.

**video_clipper.py** — Uses FFmpeg directly (not MoviePy) to cut the original
video at the chosen timestamps, preserving both video and audio.

**main.py** — Orchestrates all the steps above in sequence and saves the
final output.

## Notes

- Whisper runs locally and is completely free — no API key needed for transcription.
- The AI segment-picking and content-writing steps use the Groq API (free tier).
- FFmpeg is used directly for clipping to guarantee audio is preserved in the output clips.

## Possible future improvements

- Auto-generate subtitles burned into each clip
- Integrate Runway or another tool to actually generate B-roll footage
- Add a simple UI instead of running scripts manually
- Auto-detect the video's spoken language instead of hardcoding it
