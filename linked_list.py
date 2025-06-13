class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Assign the provided 'data' to an instance variable.
        Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Create a new Node with 'data'.
        Insert it at the front of the list (head).
        Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Create a new Node with 'data'.
        Traverse to the end of the list.
        Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.
        """

        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.
        """

        def helper(current, prev=None):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return helper(next_node, current)

        self.head = helper(self.head)

    def recursive_search(self, target):
        """
        Return True if 'target' is found, otherwise False, using recursion.
        """

        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)

        return helper(self.head)

    def display(self):
        """
        Print the contents of the list for debugging.
        Format output as 'val -> val -> val -> None'
        """
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(" -> ".join(result) + " -> None")
