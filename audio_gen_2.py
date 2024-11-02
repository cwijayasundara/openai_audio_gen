from dotenv import load_dotenv
from openai import OpenAI
import base64

_ = load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "wav"},
    messages=[
        {
            "role": "user",
            "content": "Whats aDS/CFT?"
        }
    ]
)

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open("audio/ads.wav", "wb") as f:
    f.write(wav_bytes)