#stack을 이용한 풀이
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]: #인덱스랑 pop()
                        stacklist.pop()
                        stacklist.pop()
                        answer += 2     
                break

    return answer

#my solution
def solution(board, moves):
    answer = 0
    basket = []
    size = len(board[0])
    #basket 입력
    for m in moves:
        for n in range(size):
            if board[n][m-1]!=0:
                basket.append(board[n][m-1])
                board[n][m-1]=0
                break
    #basket에서 삭제
    for c in range(500):
        for i in range(1, len(basket)):
            if basket[i]==basket[i-1]:
                del basket[i]
                del basket[i-1]
                answer+=2
                break
    return answer
