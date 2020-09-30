tree=["A","B","C","D","E"]
  
def preorder(t,root=0):
    if root<len(t):
        print(t[root])
        preorder(t,2*root+1)
        preorder(t,2*root+2)


preorder(tree)
