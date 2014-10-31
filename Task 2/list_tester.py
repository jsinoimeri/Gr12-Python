import time
from contact_maker import*
from contacts import *

TEST_SIZE = 5000

def main():
    h = [] #the list to store the Contacts
    contacts = open("contacts.in")
    for contact in contacts:
        contact = contact.strip().split(",")
        if contact[0] == "C":
            h.append(CellContact(contact[1]))
        elif contact[0] == "H":
            h.append(HomeContact(contact[1], contact[2]))
        elif contact[0] == "W":
            h.append(WorkContact(contact[1], contact[3], contact[2]))

    print h
    start = time.time()
    for i in range(TEST_SIZE):
        #generate a random generic contact based on just a phone number
        x=Contact(phone_generator())
        pos = 0
        #perform a retrieval, stopping once found or past end of list
        while pos < len(h) and h[pos] != x:
            pos += 1
    end = time.time()
    print "It took %.2f seconds to retrieve %i contacts." %(end-start, TEST_SIZE)
if __name__ == "__main__":
    main()
