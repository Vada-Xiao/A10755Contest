# A10755Contest
Preparation for NCPC contest

Data Structure + Algorithms


# Everybody's work
* TiLing
    * Implement **BinarySearchTree** by OOP -> Create *BSTree.py* file.
        * Every tree node has one data, left pointer and right pointer.
        * operations 
            * constructor -> you can define it by youerself.
            * insert an element to binary search tree.
            * delete an element from binary search tree (optional, this method is a little difficult).
            * inorder traversal (print the elements).
            * preorder traversal.
            * postorder traversal.
    * InsertionSort -> Add it into *Sort.py*.

* AddG
    * Implement **Queue** by OOP -> Create *Queue.py* file.
        * You can choice array or linked list to implement queue. (In my point, linked list implementation is relatively easy.)
        * Every element has a data and the data's priority (and a pointer to next node if you using linked list).
            * The interval of priority is [1, 10], so the input priority should be invalid if it is out of the interval.
        * operations (methods) : 
            * constructor -> you can define it by yourself.
            * add an element with a priority to queue.
            * remove the element that has highest prioriry from queue.
            * check the element with highest priority. (this method should returns the data.)
    * SelectionSort -> Add it into *Sort.py*.

* Dr.Xiao
    * Implement **LinkedList** by OOP ->Create *LinkedList.py*.
    * QuickSort -> Add it into *Sort.py*.
    * Graph Algorithms
        * DFS
        * BFS
        * Minimum Cost Spanning Tree (Kruskal method)
        * Shortest Path problem (Dijkstra method)
    * Other special algorithms (Finding...)

* Hou
    * Implement **Stack** by OOP -> Create *Stack.py*.
        * You can choice array or linked list to implement. (Generally, it is relatively easy using array implementation rather than linked list.)
        * Every element has a data. (and a pointer if using linked list implementaion.)
        * operations (methods) : 
            * constructor -> you can define it by youerself.
            * push an element to stack.
            * pop an element from stack.
            * check the top element. (return the top data.)
    * HeapSort -> Add it into *Sort.py*.
    * Backtracking with DFS function
        * two parameters : given an **array** and an integer called **depth**
        * print all combinations when the depth of DFS is up to **depth**.
