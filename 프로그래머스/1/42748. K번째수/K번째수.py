def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k=command
        cutted_array=array[i-1:j]
        cutted_array.sort()
        answer.append(cutted_array[k-1])
    return answer