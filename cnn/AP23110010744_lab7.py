n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
src=int(input())
dist=[9999]*n
next_hop=[-1]*n
dist[src]=0
for _ in range(n-1):
    for u in range(n):
        for v in range(n):
            if graph[u][v] and dist[v]>dist[u]+graph[u][v]:
                dist[v]=dist[u]+graph[u][v]
                next_hop[v]=u
print("Destination\tNext Hop\tDistance")
for i in range(n):
    if i!=src:
        print(i,"\t\t",next_hop[i],"\t\t",dist[i])
