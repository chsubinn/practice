# 이것이 취업을 위한 코딩테스트다! -5. DFS/BFS
# 미로 탈출

# 모범 답안: BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하므로 BFS로 해결한다
from collection import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input)))

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]=graph[x][y]+1 # 거리 = 이전에 방문했던 노드 + 1
            queue.append((nx, ny))
    return graph[n-1][m-1]
print(bfs(0,0))


