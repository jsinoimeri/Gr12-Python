class ListNode(object):
    def __init__(self, data, next):
        self.__data = data
        self.__next = next
    def get_next(self):
        return self.__next
    def set_next(self, node):
        self.__next = node
    def get_data(self):
        return self.__data
    def set_data(self, data):
        self.__data = new_data
    def __str__(self):
        s = "[%s]" %(self.__data)
        if self.__next != None:
            s += "--->"
        return s

class LinkedList(object):
    def __init__(self):
        self.__first = None

    def insert(self, value):
        self.__first = ListNode(value, self.__first)

    def delete(self, value):
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

    def __str__(self):
        s = ""
        current = self.__first
        while current != None:
            s += str(current)
            current = current.get_next()
        return s

    def is_empty(self):
        return self.__first == None

    def size(self):
        count = 0
        current = self.__first
        while current != None:
            count += 1
            current = current.get_next()
        return count
    
    def contains(self, value):
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
if __name__ == "__main__":
    main()