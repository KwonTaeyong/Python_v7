def solution(arrows):
    # 8방향 이동
    dirs = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    
    visited_nodes = set()
    visited_edges = set()
    answer = 0
    
    x, y = 0, 0
    visited_nodes.add((x,y))
    
    for d in arrows:
        for _ in range(2):  # 대각선 교차 처리를 위해 2번 이동
            nx, ny = x + dirs[d][0], y + dirs[d][1]
            
            # 간선 (정렬된 튜플로 저장 → 방향성 없앰)
            edge = ((x,y), (nx,ny))
            redge = ((nx,ny), (x,y))
            
            # 이미 방문한 노드인데, 처음 가는 간선이라면 → 방 생성
            if (nx,ny) in visited_nodes and edge not in visited_edges:
                answer += 1
            
            visited_nodes.add((nx,ny))
            visited_edges.add(edge)
            visited_edges.add(redge)
            
            x, y = nx, ny
    
    return answer
