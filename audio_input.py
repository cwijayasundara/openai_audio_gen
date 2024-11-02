import base64
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

_ = load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-audio-preview",
    temperature=0,
)

with open(
    "audio/ads.wav",
    "rb",
) as f:
    # b64 encode it
    audio = f.read()
    audio_b64 = base64.b64encode(audio).decode()


output_message = llm.invoke(
    [
        (
            "human",
            [
                {"type": "text", "text": "Transcribe the following:"},
                {
                    "type": "input_audio",
                    "input_audio": {"data": audio_b64, "format": "wav"},
                },
            ],
        ),
    ]
)
print(output_message.content)