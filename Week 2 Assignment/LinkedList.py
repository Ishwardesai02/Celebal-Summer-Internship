class ListNode:
    """
    A class representing a single node in a linked list.
    Each node stores data and a reference to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next_node = None


class CustomLinkedList:
    """
    A class to manage operations on the linked list.
    It supports adding nodes, displaying the list,
    and deleting a node at a specific 1-based position.
    """
    def __init__(self):
        self.start = None  # Head of the linked list

    def append(self, value):
        """
        Adds a new node containing 'value' at the end of the list.
        """
        new_element = ListNode(value)
        if self.start is None:
            self.start = new_element
        else:
            pointer = self.start
            while pointer.next_node:
                pointer = pointer.next_node
            pointer.next_node = new_element

    def display(self):
        """
        Displays the values of all nodes in the linked list.
        """
        if self.start is None:
            print("Linked list is empty.")
            return
        current = self.start
        while current:
            print(f"[{current.value}]", end=" --> ")
            current = current.next_node
        print("None")

    def remove_by_position(self, position):
        """
        Deletes the node at the given 1-based 'position'.
        Includes exception handling for invalid operations.
        """
        try:
            if self.start is None:
                raise RuntimeError("Deletion not allowed: list is currently empty.")
            if position <= 0:
                raise ValueError("Position must be a positive integer (1 or greater).")
            
            # Special case: removing the first node
            if position == 1:
                print(f"Removing node at position {position} with value {self.start.value}")
                self.start = self.start.next_node
                return

            # Traverse to node just before the target
            current = self.start
            idx = 1
            while current and idx < position - 1:
                current = current.next_node
                idx += 1

            # If current or current.next_node is None, position is invalid
            if current is None or current.next_node is None:
                raise IndexError("Deletion failed: position exceeds list length.")

            print(f"Removing node at position {position} with value {current.next_node.value}")
            current.next_node = current.next_node.next_node

        except (RuntimeError, ValueError, IndexError) as err:
            print("Error during deletion:", err)


# ------------------ Example Testing ------------------

if __name__ == "__main__":
    # Create an instance of the linked list
    my_list = CustomLinkedList()

    # Add elements to the list
    for num in [5, 15, 25, 35, 45]:
        my_list.append(num)

    print("Original linked list:")
    my_list.display()

    # Remove the 3rd element
    my_list.remove_by_position(3)
    print("List after removing 3rd node:")
    my_list.display()

    # Attempt to remove a node beyond the list length
    my_list.remove_by_position(10)

    # Create a new empty list and try deleting
    empty_list = CustomLinkedList()
    empty_list.remove_by_position(1)
