def solution(numbers):
    answer = []
#     이중 for문으로 인덱스 0부터 길이만큼 배열 돌면서 answer에 넣고, set(answer)로 중복 제거하고 반환하기
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(set(answer))