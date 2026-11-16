class DLinkedList:
    # So for this question, we need both get and put to run in O(1)
    # A hashmap alone can find a key in O(1), but our biggest challenge would be that the map has no idea which key was used least recently
    # A list alone would know the order, but finding a key in it is O(n) : /
    # So we can just use both! The hashmap can find the node in O(1), and the linked list will keep the order of usage
    # The head of our list is the most recently used node and the tail is the least recently used one : )

    # And we are using a doubly linked list because when we want to pull a node out of the middle and move it to the front, we need to know who is before it and who is after it
    class Node:
        def __init__(
                self,
                value: int,
                key: int,
                prev: Optional[DLinkedList.Node] = None,
                next: Optional[DLinkedList.Node] = None
        ):
            self.value = value
            self.prev = prev
            self.next = next
            
            # We have to store the key inside the node too, because when we remove the tail from the list, we also need to know which key to remove from the hashmap
            self.key = key

    def __init__(self, node: DLinkedList.Node):
        # When we first create the list, we only have one node, so it is both the head and the tail
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, node: Node):
        # Insert at the head (most recently used)
        node.prev = None
        node.next = self.head
        self.head.prev = node

        self.head = node
        self.length += 1

    def pop(self):
        # Remove the least recently used node (tail)
        temp = self.tail

        # After removing the tail, we have to make the node before it our new tail
        # And since it is now the last node, we cut its link going forward so it doesn't still lead to the one we removed
        self.tail = self.tail.prev
        self.tail.next = None

        # Detach removed node
        temp.prev = None

        self.length -= 1
        return temp

    def promoteToHead(self, node: Node):
        # If it is already the head, then it is already the most recently used so there is nothing for us to do
        if node is self.head: return

        # Detach node from its current position
        node.prev.next = node.next

        # If we are moving the tail, we have to update our tail to be the node before it
        # If not, we have to link the node after it back to the node before it, so that the list stays connected once we pull this node out
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        # Move node to the head
        node.prev = None
        node.next = self.head

        self.head.prev = node
        self.head = node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # The hashmap maps a key to its node, so that we can get to any node in O(1)
        self.kv = {}
        # We can't create the list yet because it needs at least one node to start with
        self.linked = None

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1

        # We just used this key, so it becomes the most recently used.. which means we have to move it to the head
        node = self.kv[key]
        self.linked.promoteToHead(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        # If the key already exists, we just update its value and promote it to the head since we just used it
        if key in self.kv:
            node = self.kv[key]
            node.value = value

            self.linked.promoteToHead(node)
            return

        node = DLinkedList.Node(value, key)

        # If this is the very first node, we create the list with it.. else, we put it at the head since it is now the most recently used
        if not self.linked:
            self.linked = DLinkedList(node)
        else:
            self.linked.append(node)

        self.kv[key] = node

        # If we are now over capacity, we have to evict the least recently used one, which is the tail. So we remove it from the list
        # And we use the key we stored in the node to also remove it from the hashmap
        if self.linked.length > self.capacity:
            leastUsed = self.linked.pop()
            self.kv.pop(leastUsed.key)