def solution(n, info):
    info = info[::-1]  # 0점 -> 10점

    def evaluate(path):
        apeach = 0
        ryan = 0

        for i in range(11):
            if info[i] == 0 and path[i] == 0:
                continue

            if path[i] > info[i]:
                ryan += i
            else:
                apeach += i

        diff = ryan - apeach
        return diff, tuple(path), path

    def P(depth, remain, path):
        """
        1점~10점에 대한 선택을 DFS로 탐색하고,
        (최대 점수차, tie-break key, 최적 path)를 반환한다.

        depth  : 현재 점수 index (1~10)
        remain : 남은 화살 수
        path   : 현재 화살 분배 상태 (0점~10점)
        """
        if depth == 11:
            final_path = path[:]
            final_path[0] += remain  # 남은 화살은 0점에 몰기
            return evaluate(final_path)

        best = (-1, (), [])

        need = info[depth] + 1

        # 이 점수를 이기는 경우
        if remain >= need:
            new_path = path[:]
            new_path[depth] = need
            best = max(best, P(depth + 1, remain - need, new_path))

        # 포기하는 경우
        best = max(best, P(depth + 1, remain, path[:]))

        return best

    diff, _, best_path = P(1, n, [0] * 11)

    if diff <= 0:
        return [-1]

    return best_path[::-1]  # 다시 10점 -> 0점