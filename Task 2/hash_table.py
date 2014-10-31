from linked_list import *
from hashing import *
from contacts import *

class HashTable(object):
    def __init__(self, size):
        '''H(size) creates a hash table with the desired size'''
        self.__buckets = []
        for num in range(size):
            self.__list = SortedList()
            self.__buckets.append(self.__list)

    def __str__(self):
        '''H.__str__() or H --> str
        Returns the string representations of a hash table.'''
        table = ""
        for num in range(len(self.__buckets)):
            table += "{%3i}%s\n" %(self.__buckets[num].size(), str(self.__buckets[num]))
        return table
        
    def insert(self, value):
        '''H.insert(value) --> None
        Inserts the value into the appropriate bucket postition determined by the
        hash code.'''
        code = int(hash_code(value))
        pos = int(code % len(self.__buckets))
        self.__buckets[pos].insert(value) 
    
    def is_empty(self):
        '''H.is_empty() --> Boolean
        Returns whether or not the hash table is empty.'''
        for i in range(len(self.__buckets)):
            if self.__list.is_empty():
                boolean = True
            
            else:
                boolean = False
                break
        return boolean
    
    def retrieve(self, value):
        '''H.retrieve(value) --> object
        Return a reference to the Contact from the table or None if it is not
        present.'''
        code = int(hash_code(value))
        pos = int(code % len(self.__buckets))

        current = self.__buckets[pos].get_first()
        if current != None:
            data = current.get_data()
        
        previous = current
        
        for i in range(len(str(self.__buckets[pos]))):
            if current != None:
                previous = current
                current = current.get_next()
                data = previous.get_data()
                
                if value == data:
                    return self.__buckets[pos].retrieve(value)
    
    def delete(self, value):
        '''H.delete(value) --> None:
        Deletes the Contact form the table'''
        code = int(hash_code(value))
        pos = int(code % len(self.__buckets))

        current = self.__buckets[pos].get_first()
        data = current.get_data()
        previous = current
        
        for i in range(len(str(self.__buckets[pos]))):
            if current != None:
                previous = current
                current = current.get_next()
                data = previous.get_data()
                
                if value == data:
                    self.__buckets[pos].delete(value)
                               
class SortedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
    
    def insert(self, value):
        '''S.insert(value) --> None
        Inserts the value in the correct sorted place within the list.'''
        if self.get_first() == None:
            self.set_first(ListNode(value, None))
        
        else:
            current = self.get_first()
            data = current.get_data()
            previous = current
            
            while current != None and data < value:
                previous = current
                current = current.get_next()
                if current != None:
                    data = current.get_data()
            
            if current != None and previous.get_data() < value and current.get_data() > value:                
                previous.set_next(ListNode(value, ListNode(current.get_data(), current.get_next())))               
            
            elif data < value and current == None:
                previous.set_next(ListNode(value, None))
            
            elif value < previous.get_data() and current != None:
                self.set_first(ListNode(value, ListNode(data, current.get_next())))            
    
    def delete(self, value):
        '''S.delete(value) --> None
        Deletes the value inside the sorted linked list. If the value is not
        in the position that it should be it will not go any further to look for
        it.'''
        current = self.get_first()
        data = current.get_data()
        
        if data == value and current == self.get_first():
            self.set_first(current.get_next())
        
        while current.get_next() != None:            
            previous = current
            current = current.get_next()            
                            
            if current != None and current.get_data() == value and current.get_next() == None:
                
                if current.get_data() == value:
                    previous.set_next(None)                       
            
            elif current != None and current.get_next() != None:
                data = current.get_data()
                
                if data == value:                             
                    previous.set_next(ListNode(current.get_next().get_data(), current.get_next().get_next()))
                        
    def retrieve(self, value):
        '''S.retrieve(value) --> object
        Return the first occurence of the value in the sorted linked list. If 
        the value is not in its rightful place, it will stop searching and return
        None.'''
        current = self.get_first()
        data = current.get_data()
        
        if current == self.get_first() and data == value:
                return data
            
        while current != None and data <= value:            
            previous = current
            current = current.get_next()
            
            if current != None and current.get_next() != None:
                data = current.get_data()
                
                if data == value:                             
                    return data
                    
            elif current == None:
                data = previous.get_data()
                
                if data < value and previous.get_next().get_data() == value:
                    return previous.get_next().get_data()
