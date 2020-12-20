from collections import defaultdict

def Dfs(graph, start, visited, path):
        visited[start] = True
        #print("com")
        path.append(start)
        #print("com")
        for successor in graph[start]:
            if visited[successor] == False :
                #print("com")
                (Dfs(graph, successor, visited, path))
        return path

v, e  = map(int, input().split())
graph = defaultdict(list)
for i in range(e):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)

visited = defaultdict(bool)
path = []

print(Dfs(graph, "a", visited, path))
