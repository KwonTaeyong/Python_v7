from collections import Counter

def solution(weights):
    # 시소에서 사용할 각 거리의 배수
    distances = [2, 3, 4]
    
    # 각 무게에 대해 가중치 * 거리 계산
    torque_values = []
    for weight in weights:
        for distance in distances:
            torque_values.append(weight * distance)
    
    # torque_values 리스트에서 같은 값을 세는 Counter 객체 생성
    counter = Counter(torque_values)
    
    # 짝꿍 쌍을 계산하기 위해 각 값에 대해 가능한 쌍의 수를 구합니다.
    answer = 0
    for count in counter.values():
        if count > 1:
            # n개의 같은 값이 있으면 그 중 2개를 뽑는 경우의 수는 nC2 = n * (n - 1) // 2
            answer += count * (count - 1) // 2
    
    return answer
