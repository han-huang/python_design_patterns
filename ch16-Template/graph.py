# coding: utf-8

# 演算法中的path不是最優的路徑，
# 而是搜索過程中的遍歷路徑
def bfs(graph, start, end): # 廣度優先圖搜索
    path = [] #　訪問路徑鏈
    visited = [start] # 訪問起始城市加入要訪問的列表
    while visited: # 訪問城市不為空
        current = visited.pop(0) # 彈出當前的城市
        if current not in path: # 如果當前的城市沒有在訪問路徑中
            path.append(current) # 將當前的城市添加到訪問路徑中
            if current == end: # 如果當前的城市是目標城市
                print()
                print(path) # 輸出訪問路徑
                print()
                return (True, path)
            if current not in graph: # 如果當前城市不在圖的起點城市中，
                continue # 則不能作為訪問的起點，跳過去
        # 將當前城市的可訪問城市添加到要訪問的目標城市清單中
        print("bfs: visited {} + graph[current] {}".format(visited, graph[current]))
        visited = visited + graph[current] # Queue - FIFO, visited.pop(0)
    return (False, path)


def dfs(graph, start, end): # 深度優先圖搜索
    path = [] #　訪問路徑鏈
    visited = [start] # 訪問起始城市加入要訪問的列表
    while visited: # 訪問城市不為空
        current = visited.pop(0) # 彈出當前的城市
        if current not in path: # 如果當前的城市沒有在訪問路徑中
            path.append(current) # 將當前的城市添加到訪問路徑中
            if current == end: # 如果當前的城市是目標城市
                print()
                print(path) # 輸出訪問路徑
                print()
                return (True, path)
            if current not in graph: # 如果當前城市不在圖的起點城市中，
                continue # 則不能作為訪問的起點，跳過去
        # 將當前城市的可訪問城市添加到要訪問的目標城市清單中
        print("dfs: graph[current] {} + visited {}".format(graph[current], visited))
        visited = graph[current] + visited # Stack - LIFO, visited.pop(0)
    return (False, path)


def main():
    graph = {
        'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
        'Mannheim': ['Karlsruhe'],
        'Karlsruhe': ['Augsburg'],
        'Augsburg': ['Munchen'],
        'Wurzburg': ['Erfurt', 'Nurnberg'],
        'Nurnberg': ['Stuttgart', 'Munchen'],
        'Kassel': ['Munchen'],
        'Erfurt': [],
        'Stuttgart': [],
        'Munchen': []
    }

    bfs_path = bfs(graph, 'Frankfurt', 'Nurnberg')
    dfs_path = dfs(graph, 'Frankfurt', 'Nurnberg')
    print('bfs Frankfurt-Nurnberg: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found'))
    print('dfs Frankfurt-Nurnberg: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found'))
    print()
    bfs_nopath = bfs(graph, 'Wurzburg', 'Kassel')
    print()
    print('bfs Wurzburg-Kassel: {}'.format(bfs_nopath[1] if bfs_nopath[0] else 'Not found'))
    print()
    dfs_nopath = dfs(graph, 'Wurzburg', 'Kassel')
    print()
    print('dfs Wurzburg-Kassel: {}'.format(dfs_nopath[1] if dfs_nopath[0] else 'Not found'))

if __name__ == '__main__':
    main()
