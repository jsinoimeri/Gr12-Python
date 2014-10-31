from contact_maker import *
from hashing import *

class Contact(object):
    '''The general way to refer to a phone contact'''    
    def __init__(self, phone):
        '''Constructs the contact's phone number and gets the hash code for it.'''        
        self.__num = phone
        self.__hash = hash_code(self.__num)
    
    def get_phone_num(self):
        '''C.get_phone_num() --> str
        Returns the contact's phone number.'''
        return self.__num
    
    def get_hash_code(self):
        '''C.get_hash_code() --> int
        Returns the hash code of the contacts phone number.'''
        return self.__hash
    
    def __gt__(self, other):
        '''C.__gt__(other) or C > other --> bool
        Returns whether or not the first phone number is greater than the second
        phone number.'''
        return self.get_phone_num() > other.get_phone_num()
    
    def __lt__(self, other):
        '''C.__lt__(other) or C < other --> bool
        Returns whether or not the first phone number is less than the second
        phone number.'''
        return self.get_phone_num() < other.get_phone_num()
    
    def __eq__(self, other):
        '''C.__eq__(other) or C == other --> bool
        Returns whether or not the first phone number is equal to the second
        phone number.'''
        return self.get_phone_num() == other.get_phone_num()
    
    def __ne__(self, other):
        '''C.__ne__(other) or C != other --> bool
        Returns whether or not the first phone number is not equal to the second
        phone number.'''
        return self.get_phone_num() != other.get_phone_num()
    
    def __le__(self, other):
        '''C.__le__(other) or C <= other --> bool
        Returns whether or not the first phone number is less than or equal to
        the second phone number.'''
        return self.get_phone_num() <= other.get_phone_num()
    
    def __ge__(self, other):
        '''C.__ge__(other) or C >= other --> bool
        Returns whether or not the first phone number is greater than or equal to
        the second phone number.'''
        return self.get_phone_num() >= other.get_phone_num()
    
    def __str__(self):
        '''C.__str__() or str(C) --> str
        Returns the string representations of the contact's number.'''
        return "%s" %(self.get_phone_num())

class CellContact(Contact):
    def __init__(self, phone):
        '''Constructs the contact's cell number.'''
        Contact.__init__(self, phone)
        self.__phone = phone
    
    def __str__(self):
        '''C.__str__() or str(C) --> str
        Returns the string representations of the contact's cell number.'''
        return "%s (c)" %(self.get_phone_num())

class HomeContact(Contact):
    def __init__(self, phone, address):
        '''Constructs the contact's home number and address.'''
        Contact.__init__(self, phone)
        self.__address = address
        
    def __str__(self):
        '''C.__str__() or str(C) --> str
        Returns the string representations of the contact's home number and
        address.'''
        return "%s@%s" %(self.get_phone_num(), self.__address)
    
class WorkContact(Contact):
    def __init__(self, phone, address, work):
        '''Constructs the contact's work number, company name and address.'''
        Contact.__init__(self, phone)
        self.__address = address
        self.__work = work
        
    def __str__(self):
        '''C.__str__() or str(C) --> str
        Returns the string representations of the contact's work number, company
        name and address.'''
        return "%s@%s(%s)" %(self.get_phone_num(), self.__work, self.__address)