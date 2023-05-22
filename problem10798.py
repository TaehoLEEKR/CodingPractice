myList = [input() for _ in range(5)]  # 각 줄의 입력을 문자열로 받음
max_len = max(len(s) for s in myList)  # 다섯 개의 문자열 중 가장 긴 문자열의 길이를 구함
for i in range(max_len):
    for j in range(5):
        if i < len(myList[j]):  # 현재 문자열이 i번째 글자를 가지고 있다면
            print(myList[j][i], end='')  # 해당 글자를 출력함
print()
