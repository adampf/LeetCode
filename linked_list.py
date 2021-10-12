class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list

    This is a customized data structure
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    # def __repr__(self):
    #     return "<Node data: %s>" % self.data

class LinkedList:
    """
    Will define a head and this attribute models the only node that the list is going to add a reference to.

    Singly LINKED LIST
    """

    # can get rid of this because the constructor does the same thing
    # head = None

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        new_node = Node(data)
        """
        Adds a new Node containing data at the head of the list
        Takes O(1) time
        
        Not only does the Node need to be added, but we also have to point the Node to the existing 
        head of the LINKED LIST
        """
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key we input
        Return the node or 'None' if not found

        Takes O(n) for Linear Time
        :param key:
        :return:
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
            """
            If we haven't found the key, then current gets set to None, and we exit the while loop
            """
        return None

    def insert(self, data, index):
        """
        Utilize the logic from the add() function

        Inserts a new Node containing data at index position
        Insertion takes O(1) time, but finding the node at the insertion point takes O(n) time.
        Therefore takes overall O(n) time
        :param data:
        :param index:
        :return:
        """

        if index == 0:
            self.add(data)

        """Traverse the list to find the current node at that index"""
        if index > 0:
            """Create new Node containing the data we want to insert"""
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = new.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            """Now insert the new node between previous and next"""
            prev_node.next_node = new
            new.next_node = next_node

            """Everytime we call current.next_node, meaning we move to the next Node in the list, we'll decrease 
            the value of position by 1.
            When position is 0, we'll have arrived at the Node in the position we want to insert.
            """

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if the key doesn't exist
        Takes O(n) time - If we need to search the entire LL
        :param key:
        :return:
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time - Linear Time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)


l = LinkedList()
l.add(10)
print(l.size())

l.add(2)
print(l.size())

l.add(45)
print(l.size())

l.add(15)
print(l.size())

print(l)
n = l.search(45)
print(n)
print(l)
