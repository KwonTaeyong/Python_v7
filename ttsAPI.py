import openai

openai.api_key = "API-KEY"

response = openai.audio.speech.create(
    model="tts-1",
    voice="alloy",  # 사용할 음성: "alloy", "echo", "fable", "onyx", "nova", "shimmer"
    input="안녕하세요, OpenAI TTS API 테스트입니다."
)

# 음성 파일 저장
with open("output.mp3", "wb") as f:
    f.write(response.content)

print("TTS 음성 파일이 생성되었습니다: output.mp3")
