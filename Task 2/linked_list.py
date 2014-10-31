class ListNode(object):
    """Models a node in a linked list, containing a data value and a link
    to the next node."""

    def __init__(self, data, next=None):
        """ListNode(data, next)
        Construct a ListNode which contains the given data and links to the
        specified next node."""
        self.__data = data
        self.__next = next

    def get_next(self):
        """L.get_next() --> ListNode
        Returns the ListNode that this node links to."""
        return self.__next

    def set_next(self, node):
        """L.set_next(node) --> None
        Sets the ListNode that this node links to."""
        self.__next = node

    def get_data(self):
        """L.get_data() --> object
        Returns the data object that this node contains."""
        return self.__data

    def set_data(self, data):
        """L.set_data(data) --> None
        Sets the data object that this node contains."""
        self.__data = new_data

    def __str__(self):
        """L.__str__() or str(L) --> str
        Returns a string representation of this ListNode in the format
        [data_value]-->  or just   [data_value] if the next node is None."""
        s = "[%s]" %(self.__data)
        if self.__next != None:
            s += "-->"
        return s

    
    
class LinkedList(object):
    """Models a classic linked list data structure."""

    def __init__(self):
        """LinkedList()
        Construct an empty linked list."""
        self.__first = None

    def get_first(self):
        """L.get_first() --> ListNode
        Return a reference to the first node in this list."""
        return self.__first

    def set_first(self, first_node):
        """L.set_first() --> None
        Set the first node in this list to be first_node."""
        self.__first = first_node

    def insert(self, value):
        """L.insert(value) --> None
        Insert the value at the front of this linked list."""
        self.__first = ListNode(value, self.__first)

    def delete(self, value):
        """L.delete(value) --> None
        Remove the first occurence of the value from this linked list, if present."""
        current = self.__first
        if current == None:
            return
        elif current.get_data() == value:
            self.__first = current.get_next()
        else:
            while current.get_next() != None and current.get_next().get_data() != value:
                current = current.get_next()
        if current.get_next() == None:
            return
        else:
            current.set_next(current.get_next().get_next())

    def retrieve(self, value):
        """L.retrieve(value) --> object
        Return the first occurence of the value in this linked list,
        or None of the value is not in the linked list."""
        current = self.__first
        while current != None and current.get_data() != value:
            current = current.get_next()
        if current != None:
            return current.get_data()
        return None

    def __str__(self):
        """L.__str__() or str(L) --> str
        Return a string representation of the list.  The format will be:
        |:[Node1]-->[Node2]-->...-->[LastNode]"""
        s = "|:"
        current = self.__first
        while current != None:
            s += str(current)
            current = current.get_next()
        return s

    def is_empty(self):
        """L.is_empty() --> bool
        Return True if this list is empty, or False otherwise."""
        return self.__first == None

    def size(self):
        """L.size() --> int
        Return the number of items in this list."""
        count = 0
        current = self.__first
        while current != None:
            count += 1
            current = current.get_next()
        return count
    
    def contains(self, value):
        """L.contains(value) --> bool
        Return True if the value is present in this list, or False otherwise."""
        current = self.__first
        contains = False
        while current != None:
            if current.get_data() == value:
                contains = True
            current = current.get_next()
        return contains
    

def main():
    l = LinkedList()
    print "contains a?", l.contains("a")
    print "insert a"
    l.insert("a")
    print "contains a?", l.contains("a")
    print "insert b"
    l.insert("b")
    print "insert c"
    l.insert("c")
    print "insert d"
    l.insert("d")
    print "insert e"
    l.insert("e")
    print "contains a?", l.contains("a")
    print "contains c?", l.contains("c")
    print "contains x?", l.contains("x")
    print l
    l.delete("a")
    print l
if __name__ == "__main__":
    main()