import os
import sys
import urllib.request
import urllib.parse

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
text = "반갑습니다 네이버"  # Python 3에서 유니코드 문자열은 기본적으로 지원됩니다.
speaker = "nara"
speed = "0"
volume = "0"
pitch = "0"
fmt = "mp3"

# 파라미터 딕셔너리
val = {
    "speaker": speaker,
    "volume": volume,
    "speed": speed,
    "pitch": pitch,
    "text": text,
    "format": fmt
}

# urllib.parse.urlencode()는 데이터를 URL 인코딩된 문자열로 변환합니다.
data = urllib.parse.urlencode(val).encode("utf-8")

# 네이버 TTS API URL
url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret
}

# Request 객체 생성
req = urllib.request.Request(url, data, headers)

# 요청을 보내고 응답 받기
try:
    with urllib.request.urlopen(req) as response:
        rescode = response.getcode()
        if rescode == 200:
            print("TTS mp3 save")
            response_body = response.read()
            # 파일로 저장
            with open('1111.mp3', 'wb') as f:
                f.write(response_body)
        else:
            print(f"Error Code: {rescode}")
except Exception as e:
    print(f"Request failed: {e}")
