# Linked List

## Properties

- Atomic unit of linked list is called a `Node`

- `Node` contains a value and a pointer which connect the next `Node` in the chain

```cs
class Node {
    int data;
    Node next;
    Node(int data) {
        this.data = data;
    }
}
```
- head: first node in the list 

- tail: last node in the list (does not have next pointer)

## Pro and Cons

pros:

    - adding (insert) new items, 
    - deleting items

    *Notes*: can easily change where the next pointer is

cons:

    - retrieval (accessing)
    - searching

    *Notes*: because each node is only aware of node next to it

## Examples

- To Declare a linked list in this sequence 6 -> 3 -> 4 -> 2 -> 1

```cs
// Declare 5 nodes
Node nodeA = new Node(6);
Node nodeB = new Node(3);
Node nodeC = new Node(4);
Node nodeD = new Node(2);
Node nodeE = new Node(1);

// connect node with its next node
nodeA.next = nodeB;
nodeB.next = nodeC;
nodeC.next = nodeD;
nodeD.next = nodeE;
```

## Variations

### Doubly Linked List

- have two pointer `next` and `prev` which connect next `node ` and also previous `Node`

```cs
class Node {
    int data;
    Node next;
    Node prev;
    Node(int data) {
        this.data = data;
    }
}
```

### Circular Linked List

- the last node connect to the first node