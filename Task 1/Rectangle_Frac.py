# By: Jeton Sinoimeri
# Rectangle_Frac.py
# Date: Oct 17, 2010

from Fraction import *

class Rectangle(object):
    '''A class that models a rectangle with the given (x,y), width and height'''
    
    def __init__(self, x, y, w, h, boolean):
        '''Creates a rectangle with the given height and width at the given (x,y)'''
        
        if Fraction.decimal_value(w) > -1.0 and Fraction.decimal_value(h) > -1.0:
            self.__height = Fraction.decimal_value(h)
            self.__width = Fraction.decimal_value(w)           
            self.__first = (x, y)
            self.__second = (x, y + self.__height)            
            self.__third = (x + self.__width, y + self.__height)
            self.__fourth = (x + self.__width, y)
            self.__filled = boolean
        
        else:
            raise TypeError("Width and height cannot be negative")
    
    def is_filled(self):
        '''R.is_filled() --> boolean
        Returns whether or not the rectangle is filled.'''        
        return self.__filled
    
    def set_filled(self, boolean):
        '''R.set_filled(boolean)
        Sets the whether or not the rectangle is filled.'''        
        self.__filled = boolean
    
    def get_height(self):
        '''R.get_height() --> int
        Returns the height of the rectangle.'''        
        return self.__height
    
    def set_height(self, h):
        '''R.set_height(int)
        Sets the rectangle's new height. An error occurs if height is negative'''        
        if Fraction.decimal_value(h) < 0:
            raise TypeError("Height cannot be negative")        
        
        else:
            self.__height = Fraction.decimal_value(h)
    
    def get_width(self):
        '''R.get_width() --> int
        Returns the width of the rectangle.'''      
        return self.__width
    
    def set_width(self, w):
        '''R.set_width(int)
        Sets the rectangle's new width. An error occurs if width is negative'''        
        if Fraction.decimal_value(w) < 0:
            raise TypeError("Width cannot be negative")        
        
        else:
            self.__width = Fraction.decimal_value(w)
   
    def get_first(self):
        '''R.get_first() --> (x, y)
        Returns the bottom left corner of the rectangle.'''        
        return self.__first
    
    def set_first(self, x, y):
        '''R.set_first(int, int)
        Sets the bottom left corner of the rectangle.'''        
        self.__first = (x, y)
   
    def get_second(self):
        '''R.get_second() --> (x, y)
        Returns the top left corner of the rectangle.'''        
        return self.__second
    
    def get_third(self):
        '''R.get_third() --> (x, y)
        Returns the top right corner of the rectangle.'''        
        return self.__third
    
    def get_fourth(self):
        '''R.get_fourth() --> (x, y)
        Returns the bottom right corner of the rectangle.'''        
        return self.__fourth
    
    def get_coordinates(self):
        '''R.get_coordinates() --> [(x, y), (x2, y2), (x3, y3), (x4, y4)]
        Returns the coordinates of the rectangle.'''        
        return [self.get_first(), self.get_second(), self.get_third(), self.get_fourth()]
    
    def show(self):
        '''R.show() --> ASCII text representation
        Returns or "shows" a picture of the rectange in ASCII text representation'''
        output = " " + "__" * int(abs(round(self.get_width(), 0)))
        v_bar = ''
        for h in range(int(abs(round(self.get_height())))):
            if h < int(abs(round(self.get_height())))-1:                                
                if self.is_filled():
                    space = "##" * int(abs(round(self.get_width())))
                
                else:
                    space = "  " * int(abs(round(self.get_width())))
                
                if int(abs(round(self.get_width()))) > 0:
                    v_bar = "|"                               
                
                output += "%s" %("\n|" + space + v_bar)
            
            else:
                if self.is_filled():
                    underscore = "##" * int(abs(round(self.get_width())))                                
                
                else:
                    underscore = "__"* int(abs(round(self.get_width())))
                
                if int(abs(round(self.get_width()))) > 0:
                    v_bar = "|" 
                
                output += "%s" %("\n|" + underscore + v_bar)
        
        return output
    
    def perimeter(self):
        '''R.perimeter() --> int
        Returns the perimeter of the rectangle'''        
        return 2*(self.get_width() + self.get_height())
    
    def area(self):
        '''R.area() --> int
        Returns the area of the rectangle'''        
        return self.get_width() * self.get_height()
    
    def diagonal_length(self):
        '''R.diagonal_length() --> float
        Returns the diagonal length of the rectangle'''        
        return (self.get_width() * self.get_width() + self.get_height() * self.get_height())**0.5
    
    def is_square(self):
        '''R.is_square() --> boolean
        Returns whether or not it is a square'''        
        return self.get_width() == self.get_height()
    
    def invert(self): # for some weird reason doesnt seem to work
        '''R.invert() --> Rectangle
        Returns the same rectangle but with height and width swapped between each other'''
        return Rectangle(self.get_first()[0], self.get_first()[1], self.get_height(), self.get_width(), self.is_filled())
    
    def translate(self, other): # for some weird reason doesnt seem to work
        '''R.translate((x, y)) --> Rectangle
        Returns the same rectangle but horizontally and vertically shifted'''            
        return Rectangle(self.get_first()[0] + other[0], self.get_first()[1] + other[1], self.get_width(), self.get_height(), self.is_filled())
    
    def contains(self, other):
        '''R.contains(other) --> Boolean
        Returns whether or not the new rectangle is fully contained within the 
        first rectangle.'''        
        boolean = True                
        for i in range(4):            
            if self.get_third()[0] < other.get_coordinates()[i][0] or self.get_first()[0] > other.get_coordinates()[i][0]:
                boolean = False
                break 
            
            elif self.get_third()[1] < other.get_coordinates()[i][1] or self.get_first()[1] > other.get_coordinates()[i][1]:                    
                boolean = False
                break 
         
        return boolean
            
    def __gt__(self, other): 
        '''R.__gt__(other) or R > other --> Boolean
        Returns whether or not the distance from the center of the first
        rectangle to the origin is greater than the distance of the second one.'''        
        center_distance = ((self.get_width() / 2.0 + self.get_first()[0]) ** 2 + (self.get_height() / 2.0 + self.get_first()[1]) ** 2)**0.5
        center_distance2 = ((other.get_width() / 2.0 + other.get_first()[0]) ** 2 + (other.get_height() / 2.0 + other.get_first()[1]) ** 2)**0.5
        
        return center_distance > center_distance2
    
    def __lt__(self, other):
        '''R.__lt__(other) or R < other --> Boolean
        Returns whether or not the distance from the center of the first
        rectangle to the origin is less than the distance of the second one.'''        
        center_distance = ((self.get_width() / 2.0 + self.get_first()[0]) ** 2 + (self.get_height() / 2.0 + self.get_first()[1]) ** 2)**0.5
        center_distance2 = ((other.get_width() / 2.0 + other.get_first()[0]) ** 2 + (other.get_height() / 2.0 + other.get_first()[1]) ** 2)**0.5
                
        return center_distance < center_distance2
    
    def __eq__(self, other):
        '''R.__eq__(other) or R == other --> Boolean
        Returns whether or not the distances from the centers of the rectangles 
        to the origin are equal by finding the difference between the two 
        distances and returning True if the difference is less than 0.0001'''        
        boolean = False        
        center_distance = ((self.get_width() / 2.0 + self.get_first()[0]) ** 2 + (self.get_height() / 2.0 + self.get_first()[1]) ** 2)**0.5
        center_distance2 = ((other.get_width() / 2.0 + other.get_first()[0]) ** 2 + (other.get_height() / 2.0 + other.get_first()[1]) ** 2)**0.5
        
        if abs(center_distance - center_distance2) < 0.0001:
            boolean = True
                
        return boolean
    
    def __str__(self):
        '''R.__str__() --> str
        Return a str in the form "x-wide by y-high, at bottom left corner(x,y) or
        if filled in the form "x-wide by y-high (filled), at bottom left corner(x,y)".'''        
        if self.is_filled():
            return "%f wide x %f high (filled), at %s" %(self.get_width(), self.get_height(), self.get_first())
        
        else:
            return "%f wide x %f high, at %s" %(self.get_width(), self.get_height(), self.get_first())

def main():
    r1 = Rectangle(0, 0, Fraction(9, 6), Fraction(1,5), False)    
    r2 = Rectangle(0, 1, Fraction(1,21), Fraction(9,5), True)   
    print r1 > r2
    print r1 < r2
    print r1 == r2
    print r1.show()
    print r2.show()
    print r1.contains(r2)
    print r2.contains(r1)
    print r1.is_square()
    print r2.is_square()
    print r1.diagonal_length()
    print r2.diagonal_length()
    print r1.area()
    print r2.area()
    print r1.perimeter()
    print r2.perimeter()
    
if __name__ == "__main__":
    main()
