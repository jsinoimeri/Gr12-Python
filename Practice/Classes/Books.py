
# The Parent class
class Book(object):
    def __init__(self, pages=0, title="No Title"):
        self.pages = pages
        self.title = title

    def print_pages(self):
        print "Number of pages = %i" %(self.pages)
    
    def __str__(self):
        return "Book: %s" %(self.title)
        
# the child class
class Dictionary(Book):
    def __init__(self, p=0, d=0, t="Untitled"):
        Book.__init__(self, p, t) #construct the parent part
        self.definitions = d
    
    def print_definitions(self):
        #use the variable 'pages' in the parent class as if it was local
        print "%i definitions (%.1f per page)" %(self.definitions, 1.0*self.definitions/self.pages)
        
    def print_both(self):
        #call a method 'inherited' from the parent
        self.print_pages()
        self.print_definitions()

    def __str__(self):
        #override the method inherited form the parent
        #return "Dictionary: %s" %(self.title)
        return Book.__str__(self) + "\n" + "Dictionary: %s" %(self.title)
    
def main():
    webster = Dictionary(p=1000, d=15000, t="Websters")
    # call an inherited method:
    webster.print_pages()
    # call a method local to Dictionary:
    webster.print_definitions()
    print "---------------------------"
    # call a method in the child that uses a method in the parent
    webster.print_both()
    print "---------------------------"
    # call a method that is defined in both the parent and the child:
    print webster
    

if __name__ == "__main__":
    main()
