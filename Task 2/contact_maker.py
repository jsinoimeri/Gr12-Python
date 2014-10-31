from random import *
STREETS = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf",\
           "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November",\
           "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform",\
           "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
STREET_TYPES = ["Ave.", "St.", "Rd.", "Lane", "Cres.", "Pkwy", "Ct"]
COMPANY_NAMES = ["vix", "cor", "sin", "par", "zin", "bag", "zip", "dry", "fan",\
                 "bur", "bli", "fos", "cra", "mad"]
COMPANY_ENDS = [" Ltd.", " Inc.", " Corp.", " Canada", " International", ""]

def phone_generator():
    """
    phone_generator() --> str
    Generates & returns a random phone number in North American format.
    For example: (555)987-1234"""
    phone = "(%i%i%i)" %(randint(2, 9), randint(0, 9), randint(0, 9))
    phone += "%i%i%i-" %(randint(2, 9), randint(0, 9), randint(0, 9))
    phone += "%i%i%i%i" %(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
    return phone

def address_generator():
    """
    address_generator() --> str
    Generates & returns a random street address.  Numbers are between 1 and 9999,
    and streets are randomly selected from constant lists (STREETS and 
    STREET_TYPES).  For example: 345 Foxtrot Lane"""     
    return "%i %s %s" %(randint(1, 9999), choice(STREETS), choice(STREET_TYPES))


def company_generator():
    """
    company_generator() --> str
    Generates & returns a random company name.  Names are randomly composed of
    2 - 4 letter groups (COMANY_NAMES) and a company type (COMPANY_TYPES).
    For example with 4 letter groups: Madfosfanzip Inc."""     
    name = ""
    for i in range(randint(2,4)):
        name += choice(COMPANY_NAMES)
    return "%s%s" %(name.capitalize(), choice(COMPANY_ENDS))


def contact_maker(file_name, num_contacts):
    """
    contact_maker(file_name, num_contacts) --> None
    Generates a text file of randomly generated contacts, including random
    contact types.  Argumengts are the name of the resulting file (file_name)
    and the number of contacts to be created (num_contacts)."""
    out_file = open(file_name, "w")
    for num in range(num_contacts):
        contact_type = choice("HWC")
        if contact_type == "H":
            #Home contact
            out = "H,%s,%s" %(phone_generator(), address_generator())
        elif contact_type == "W":
            #Work contact
            out = "W,%s,%s,%s" %(phone_generator(), company_generator(), address_generator())
        else:
            #Cell contact
            out = "C,%s" %(phone_generator())
        out_file.write(out + "\n")
    out_file.close()
    
if __name__ == "__main__":
    contact_maker("contacts.in", 500)
