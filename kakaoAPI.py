import requests
import pandas as pd

# 카카오 API 키
access_token = "YOUR_ACCESS_TOKEN"

# 친구 목록을 가져오기 위한 API 호출
url = "https://kapi.kakao.com/v1/api/talk/friends"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)
data = response.json()

# 친구 목록을 DataFrame으로 변환
friends_list = []
for friend in data['elements']:
    friends_list.append({
        'name': friend['nickname'],
        'id': friend['uuid']
    })

df = pd.DataFrame(friends_list)

# 엑셀 파일로 저장
df.to_excel("kakao_friends.xlsx", index=False)

print("엑셀 파일로 저장되었습니다.")
