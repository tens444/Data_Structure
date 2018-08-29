graph = {
    'A':{'B':5, 'C':1},
    'B':{'A':5, 'C':2, 'D':1},
    'C':{'A':1, 'B':2, 'D':4, 'E':8},
    'D':{'B':1, 'C':4, 'E':3, 'F':6},
    'E':{'C':8, 'D':3},
    'F':{'D':6}
}

def dijkstra(graph, start):
    INF = 65535
    known = set()
    dis = dict((vertex, INF)for vertex in graph.keys())
    parent = dict((vertex, None)for vertex in graph.keys())

    minv = start
    dis[start] = 0

    for i in range(len(graph)):
        known.add(minv)
        for w in graph[minv]:
            if dis[minv] + graph[minv][w] < dis[w]:
                dis[w] = dis[minv] + graph[minv][w]
                parent[w] = minv
        
        min = INF
        for v in dis.keys():
            if v not in known and dis[v] < min:
                min = dis[v]
                minv = v
    
    for v in parent.keys():
        path = [v]
        last = parent[v]
        while last:
            path.append(last)
            last = parent[last]
        
        path.reverse()
        print(path)

dijkstra(graph, 'A')