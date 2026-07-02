import whisper

def transcribe_audio(audio_path):
    print("Transcribing audio...")
    model = whisper.load_model("base")           # free local model load karta hai
    result = model.transcribe(audio_path, language="hi")  # Hindi transcription
    print("Transcription complete!")
    return result
