# 二元樹
class BStree:
    def __init__(self,value):
        self.value = value
        self.lefttree = None
        self.righttree = None
    def setLeft(self,value):
        self.lefttree = Bstree(value)
    def setRight(self,value):
        self.righttree = Bstrr(value)

def searchvalue(tmp,value):
    # 都沒有回傳新節點
    if tmp == None:
        return BStree(value)
    else:
        # 左子樹
        if tmp.value>value:
            tmp.lefttree = searchvalue(tmp.lefttree,value)
        # 右子樹
        else:
            tmp.righttree = searchvalue(tmp.righttree,value)
        return tmp
   
def postorder(root): # 後序: 左右中
    if root == None:
        return
    else:
        postorder(root.lefttree)
        postorder(root.righttree)
        print(root.value,end = " ")

def inorder(root): # 中序: 左中右
    if root == None:
        return
    else:
        inorder(root.lefttree)
        print(root.value,end = " ")
        inorder(root.righttree)

def preorder(root): # 前序:中左右
    if root == None:
        return
    else:
        print(root.value,end = " ")
        preorder(root.lefttree)
        preorder(root.righttree)

            
# 字串輸入數字
str_in = input()
num = [int(n) for n in str_in.split()]
num = list(map(int, str_in.strip().split()))
root = BStree(None)

for x in range(len(num)):
    if x == 0:
        root = BStree(num[x])
    else:
        tmp = searchvalue(root,num[x])

print("後序", end = ":")
postorder(root)
print()
print("中序", end = ":")
inorder(root)
print()
print("前序", end = ":")
preorder(root)