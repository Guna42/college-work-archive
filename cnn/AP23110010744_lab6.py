n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
src=int(input())
visited=[0]*n
dist=[9999]*n
dist[src]=0
for _ in range(n):
    u=-1
    for i in range(n):
        if not visited[i] and (u==-1 or dist[i]<dist[u]):
            u=i
    visited[u]=1
    for v in range(n):
        if graph[u][v] and dist[v]>dist[u]+graph[u][v]:
            dist[v]=dist[u]+graph[u][v]
print("Vertex\tDistance from Source")
for i in range(n):
    print(i,"\t",dist[i])
