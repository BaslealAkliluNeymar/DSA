#Binary Heap
A Binary Heap is a Data Structure that is much like a Binry Search Tree , only that the top node is bigger or smaller than its children nodes and this goes on recursively for each node except for the leaf nodes.

A Tree can be called a Heap only if :
    1.It is Complete:
        A complete Tree is one where the left most nodes are filled
        A complete Tree is one which is balanced keeping the above rule.
        A perfect tree can also be considered as a complete tree
    2. The parent node should be bigger or smaller than its children

#Types of Heap

There are two types of Heap
    1.Min Heap - where the parent node is less than its children
    2.Max Heap - where the parent node is greater than its children
        !(Capture.PNG)



In the case of Priority Queues , It is significantly hard to insert and increbly easy to delete. In priority queues the items are layed out in a specific order and just like any other queue a FIFO is applied. 

So in Deletion we can just delete the very last element 
while in insertion  , we would have to iterate to the index of the biggest item and replace that and all the others , we have to shift all over again. and this creates a O(N) time complexity. A priority queue or a queue are abstract data structures because they are made from other primitive data structures.


The heap has something called a last node. A heap’s last node is the rightmost
node in its bottom level.

#A Heap is used to implement Priority Queues

The Heap has two primary operations:
    ##Insertion
        The efficiency of inserting into a heap is O(log N).
    ##Deletion
        The first thing to know about deleting a value from a heap is that we only ever delete the root node.

        To delete it, we overwrite the root by placing the last node there instead.



Because finding the last node is so critical to the heap’s operations, and we want to make sure that finding the last node is efficient, heaps are usually implemented using arrays.

    !(Array.PNG)