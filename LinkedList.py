# Definition of linked list

class node:
    def __init__(self, nodeData, next = None):
        self.nodeData = nodeData
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    #   Push an element to first position. 
    def push(self, data):
        NewNode = node(data, self.head)
        self.head = NewNode
    #   Pop an element from first position.
    def pop(self):
        if self.head != None:
            self.head = self.head.next
    #   Print datas of all nodes.
    def traversal(self):
        HeadPtr = self.head
        while HeadPtr != None:
            print(HeadPtr.nodeData, end = " -> ")
            HeadPtr = HeadPtr.next
        print("None")
    
    #   Insert and Delete methods. If these operations come across fail conditions, returning False.
    def insert(self, pos, data):
        if pos < 0:
            return False
        elif pos == 0:
            NewNode = node(data, self.head)
            self.head = NewNode
            return True
        else:
            HeadPtr = self.head
            for i in range(pos - 1):
                if HeadPtr == None:
                    return False
                HeadPtr = HeadPtr.next
            if HeadPtr == None:
                return False
            NewNode = node(data, HeadPtr.next)
            HeadPtr.next = NewNode
            return True
    def delete(self, pos):
        if pos < 0:
            return False
        elif pos == 0:
            if self.head != None:
                self.head = self.head.next
                return True
            return False
        else:
            HeadPtr = self.head
            for i in range(pos - 1):
                if HeadPtr == None or HeadPtr.next == None:
                    return False
                HeadPtr = HeadPtr.next
            if HeadPtr == None or HeadPtr.next == None:
                return False
            HeadPtr.next = HeadPtr.next.next
            return False



myList = LinkedList()
myList.push(10)
myList.push(20)
CheckInsertSuccess = myList.insert(2,30)
CheckDeleteSuccess = myList.delete(0)
myList.traversal()

# Insert and Delete are successful
print(CheckInsertSuccess, CheckInsertSuccess)