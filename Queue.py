class node:
    def __init__(self, nodeData, nodePriority):
        self.nodeData = nodeData
        self.nodePriority = nodePriority
        self.next = None
        return

class Queue:
    # constructor
    def __init__(self):
        self.head = None

    # Add an element with a priority to queue
    def add(self, data, priority):
        # 確保 priority 範圍介於[1,10]
        if priority > 10 or priority < 1:
            print("invalid")
        else:
            NewNode = node(data, priority)
            if self.head == None: # Queue是空的時候
                self.head = NewNode
            else: # Queue不是空的話，放最後
                HeadPtr = self.head
                while True:
                    if(HeadPtr.next == None):
                        HeadPtr.next = NewNode
                        break
                    HeadPtr = HeadPtr.next
                
    # Remove the element that has highest priority from Queue 
    def remove(self):
        # 呼叫checkHightest()找到priority最高的data
        highest = self.checkHightest()
        if highest != None:
            HeadPtr = self.head
            # First data's priority is the highest -> remove first node
            if HeadPtr.nodeData == highest:
                self.head = self.head.next
            else:
                PreviousPtr = self.head # 紀錄priority最高的前一個node 
                HeadPtr = self.head.next
                while HeadPtr != None:
                    if(HeadPtr.nodeData == highest):
                        PreviousPtr.next = HeadPtr.next
                        break
                    PreviousPtr = PreviousPtr.next
                    HeadPtr = HeadPtr.next
        else:
            print("No node can remove")
    
    # Return the data with highest priorty
    def checkHightest(self):
        if self.head != None:
            maxNode = self.head # 用來找priority最高的node
            HeadPtr = self.head
            while HeadPtr != None:
                if(HeadPtr.nodePriority > maxNode.nodePriority):
                    maxNode = HeadPtr
                HeadPtr = HeadPtr.next
            return maxNode.nodeData
        else:
            return None

    # Print datas of all nodes.
    # 跟于恩借ㄉ，print出來測試用ouo
    def traversal(self):
        HeadPtr = self.head
        while HeadPtr != None:
            print(HeadPtr.nodeData, end = " -> ")
            HeadPtr = HeadPtr.next
        print("None")

# Test
hiQueue = Queue()
hiQueue.add("one",1)
hiQueue.add("three",3)
hiQueue.add("two",2)
hiQueue.traversal() # one -> three -> two -> None

highestData = hiQueue.checkHightest() 
print("The element with highest data:", highestData) # three
hiQueue.remove()
hiQueue.traversal() # one -> two -> None

highestData = hiQueue.checkHightest()
print("The element with highest data:", highestData) # two