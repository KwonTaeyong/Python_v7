angle1 = int(input())
angle2 = int(input())

# 두 각의 합을 구한 후 360으로 나눈 나머지를 출력
sum_angle = angle1 + angle2
result = sum_angle % 360  # 360으로 나눈 나머지를 계산
print(result)