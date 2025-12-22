import re
from collections import defaultdict

def solution(word, pages):
    word = word.lower()
    n = len(pages)

    urls = []              # index -> url
    basic_scores = []      # index -> 기본 점수
    out_links = []         # index -> 외부 링크 목록
    link_count = []        # index -> 외부 링크 수

    url_to_index = {}

    # 1️⃣ 페이지 파싱
    for i, page in enumerate(pages):
        # URL 추출
        url = re.search(r'<meta property="og:url" content="(https://[^"]+)"', page).group(1)
        urls.append(url)
        url_to_index[url] = i

        # 외부 링크 추출
        links = re.findall(r'<a href="(https://[^"]+)"', page)
        out_links.append(links)
        link_count.append(len(links))

        # 기본 점수 계산
        text = re.sub(r'[^a-zA-Z]', ' ', page).lower()
        words = text.split()
        basic_scores.append(words.count(word))

    # 2️⃣ 링크 점수 계산
    link_scores = [0.0] * n

    for i in range(n):
        if link_count[i] == 0:
            continue
        score = basic_scores[i] / link_count[i]
        for link in out_links[i]:
            if link in url_to_index:
                link_scores[url_to_index[link]] += score

    # 3️⃣ 매칭 점수 계산
    max_score = -1
    answer = 0

    for i in range(n):
        matching_score = basic_scores[i] + link_scores[i]
        if matching_score > max_score:
            max_score = matching_score
            answer = i

    return answer
