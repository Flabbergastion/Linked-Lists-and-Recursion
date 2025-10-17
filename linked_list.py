
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a new node with the provided data.
        Args:
            data: The integer data to store in this node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node with given data at the front of the list.
        Time Complexity: O(1)
        
        Args:
            data: The integer data to store in the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node with given data at the end of the list.
        Time Complexity: O(n)
        
        Args:
            data: The integer data to store in the new node.
        """
        new_node = Node(data)
        
        # If list is empty, make new node the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the end of the list
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Set the last node's next to the new node
        current.next = new_node

    def recursive_sum(self):
        """
        Calculate the sum of all node data in the list using recursion.
        
        Returns:
            int: The sum of all node data, 0 if the list is empty.
        """
        return self._recursive_sum_helper(self.head)
    
    def _recursive_sum_helper(self, node):
        """
        Helper function for recursive sum calculation.
        
        Args:
            node: The current node being processed.
            
        Returns:
            int: The sum from this node to the end of the list.
        """
        # Base case: if node is None, return 0
        if node is None:
            return 0
        
        # Recursive case: return current node's data + sum of rest of the list
        return node.data + self._recursive_sum_helper(node.next)

    def recursive_reverse(self):
        """
        Reverse the linked list in-place using recursion.
        Updates the head to point to the new first node.
        """
        self.head = self._recursive_reverse_helper(None, self.head)
    
    def _recursive_reverse_helper(self, prev, current):
        """
        Helper function for recursive list reversal.
        
        Args:
            prev: The previous node (becomes the next node after reversal).
            current: The current node being processed.
            
        Returns:
            Node: The new head of the reversed list.
        """
        # Base case: if current is None, return prev (new head)
        if current is None:
            return prev
        
        # Store the next node before we lose the reference
        next_node = current.next
        
        # Reverse the pointer: current now points to prev
        current.next = prev
        
        # Recursive case: continue with next_node as current and current as prev
        return self._recursive_reverse_helper(current, next_node)

    def recursive_search(self, target):
        """
        Search for a target value in the list using recursion.
        
        Args:
            target: The value to search for in the list.
            
        Returns:
            bool: True if target is found, False otherwise.
        """
        return self._recursive_search_helper(self.head, target)
    
    def _recursive_search_helper(self, node, target):
        """
        Helper function for recursive search.
        
        Args:
            node: The current node being examined.
            target: The value to search for.
            
        Returns:
            bool: True if target is found, False otherwise.
        """
        # Base case: if node is None, target not found
        if node is None:
            return False
        
        # Base case: if current node's data matches target
        if node.data == target:
            return True
        
        # Recursive case: search in the rest of the list
        return self._recursive_search_helper(node.next, target)

    def display(self):
        """
        Display the contents of the list in a user-friendly format.
        Prints the list as: val -> val -> val -> None
        """
        if self.head is None:
            print("Empty list: None")
            return
        
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        
        print(" -> ".join(values) + " -> None")
