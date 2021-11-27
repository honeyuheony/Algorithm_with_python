def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7, '*']
    right = [3, 6, 9, '#']
    middle = [2, 5, 8, 0]
    last_left_finger = '*'
    last_right_finger = '#'
    for n in numbers:
        # 왼쪽 버튼을 누르는 경우
        if n in left:
            answer += "L"
            last_left_finger = n
        # 오른쪽 버튼을 누르는 경우
        elif n in right:
            answer += "R"
            last_right_finger = n
        # 중앙 버튼을 누르는 경우 -> 버튼과의 거리계산
        else:
            if last_left_finger in left:
                left_length = abs(middle.index(
                    n) - left.index(last_left_finger)) + 1
            else:
                left_length = abs(middle.index(
                    n) - middle.index(last_left_finger))
            if last_right_finger in right:
                right_length = abs(middle.index(
                    n) - right.index(last_right_finger)) + 1
            else:
                right_length = abs(middle.index(
                    n) - middle.index(last_right_finger))
            if left_length < right_length:
                answer += "L"
                last_left_finger = n
            elif left_length > right_length:
                answer += "R"
                last_right_finger = n
            else:
                if hand == "left":
                    answer += "L"
                    last_left_finger = n
                else:
                    answer += "R"
                    last_right_finger = n
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand) == 'LRLLLRLLRRL')
