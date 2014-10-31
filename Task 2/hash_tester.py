import random
import time
from contact_maker import *
from hash_table import *
from contacts import *
 
TEST_SIZE = 5000

def main():
    h = HashTable(600) #create the HashTable with a specified size
    contacts = open("contacts.in")
    for contact in contacts:
        contact = contact.strip().split(",")
        if contact[0] == "C":
            h.insert(CellContact(contact[1]))
        elif contact[0] == "H":
            h.insert(HomeContact(contact[1], contact[2]))
        elif contact[0] == "W":
            h.insert(WorkContact(contact[1], contact[3], contact[2]))
    print h #view the hashtable --> should be nicely formatted!

    start = time.time()
    for i in range(TEST_SIZE):
        #generate a random generic contact and attempt to retrieve it
        x = Contact(phone_generator())
        y = h.retrieve(x)
    end = time.time()
    print "It took %.2f seconds to retrieve %i contacts." %(end-start, TEST_SIZE)

if __name__ == "__main__":
    main()