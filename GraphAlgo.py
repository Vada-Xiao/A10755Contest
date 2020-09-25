
# Graph must be two dimensional list.

# TODO
def Prim(Graph):
    Length = len(Graph)
    Distance = [1e9 for i in range(0, Length)]
    Parent = [0 for i in range(0, Length)]
    visit = [False for i in range(0, Length)]

    Pareent[0] = 0
    Distance[0] = 0

    for i in range(Length):
        start, end = -1, -1
        MinDis = 1e9

        for j in range(Length):
            if visit[j] == False and Distance[j] < MinDis:
                start = j
                MinDis = Distance[j]
        
        if start == -1:
            break
        visit[start] = True

        for end in range(Length):
            if visit[end] == False and Graph[start][end] < Distance[end]:
                Distance[end] = Graph[start][end]
                Parent[end] = start
    
    for i in range(Length):
        if parent[i] != i):
            print("%d --> %d : %d"%(Parent[i], i, Distance[i]))