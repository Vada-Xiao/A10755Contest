
# Graph must be two dimensional list.

# TODO
def Prim(Graph):
    Length = len(Graph)
    Distance = [1e9 for i in range(0, Length)]
    Parent = [0 for i in range(0, Length)]
    visit = [False for i in range(0, Length)]
    