# By: Jeton Sinoimeri
# Fraction.py
# Date: Oct 11, 2010

class Fraction(object):
    '''A class that models a fraction with a numerator and denominator.'''    
    def __init__(self, num, den):
        '''Create a Fraction with the given num(erator) and den(ominator).'''
        if den < 0:
            den *= -1
            num *= -1
        
        if den == 0:
            raise TypeError("Denominator cannot be zero")
        
        self.__num = num
        self.__den = den
            
    def get_num(self):
        '''F.get_num() --> int
        Returns the numerator of a fraction'''
        return self.__num
    
    def get_den(self):
        '''F.get_den() --> int
        Returns the denominator of a fraction'''
        return self.__den
    
    def set_num(self, num):
        '''F.set_num(int)
        Sets the numerator of a fraction'''
        self.__num = num
    
    def set_den(self, den):
        '''F.set_den(int)
        Sets the denominator of a fraction'''
        if den == 0:
            raise TypeError("Denominator cannot be zero")
        
        elif den < 0:
            self.__den *= -1
            self.__num *= -1
        
        else:
            self.__den = den
    
    def reduce_frac(self):
        '''F.reduce_frac() --> Fraction
        Return the simplest form of that fraction as a fraction''' 
        for x in range(1, int(self.get_den()) + 1):
            if self.get_den() % x == 0:                
                if self.get_num() % x == 0:
                    div = x    
        
        if self.get_den() / div == 1:
            return self.get_num() / div
        
        else:
            return Fraction(self.get_num() / div, self.get_den() / div)
    
    def square(self):
        '''F.square() --> Fraction
        Return the squared version of the fraction.'''        
        return Fraction(self.get_num() * self.get_num(), self.get_den() * self.get_den())
    
    def reciprocate(self):
        '''F.reciprocate() --> Fraction
        Return the fraction in a reciprocated form and if necessary the result
        will be reduced to its simpliest form.'''        
        return Fraction.reduce_frac(Fraction(self.get_den(), self.get_num()))
    
    def decimal_value(self):
        '''F.decimal_value() --> float
        Return the fraction as a float.'''        
        return self.get_num()/float(self.get_den())
    
    def mixed_form(self):
        '''F.mixed_form() --> Mixed form fraction
        Return the fraction in the form of a mixed form fraction.'''
        if self.get_num() % self.get_den() != 0:
            return "%i|%i/%i" %(self.get_num() / self.get_den(), self.get_num() % self.get_den(), self.get_den())
        
        else:
            return "%i" %(self.get_num() / self.get_den())
    
    def int_power(self, other):
        '''F.int_power(int) --> Fraction
        Return the fraction to the power of the int and the result will be
        reduced to its lowest form'''
        return Fraction.reduce_frac(Fraction(self.get_num()**abs(other), self.get_den()**abs(other)))
        
    def frac_power(self, other):
        '''F.frac_power(Fraction) --> float
        Return the decimal value of the fraction to the power of the second
        fraction'''
        return Fraction.decimal_value(Fraction((abs(self.get_num())**abs(other.get_num()))**abs(other.decimal_value()), (abs(self.get_den())**abs(other.get_num()))**abs(other.decimal_value())))
    
    def rounding(self):
        '''F.rounding() --> int
        Return the rounded version of the decimal value of the fraction to the
        whole number.'''
        return int(round(self.decimal_value()))
    
    def abs_rounding(self):
        '''F.rounding() --> int
        Return the absolute value of the rounded version of the decimal value of
        the fraction to the whole number.'''
        return abs(int(round(self.decimal_value())))
    
    def __mul__(self, other):
        '''F.__mul__(other) or F * other --> Fraction
        Return the product of the two fractions as a fraction and if necessary
        the result will be reduced to its simpliest form.'''        
        return Fraction.reduce_frac(Fraction(self.get_num() * other.get_num(), self.get_den() * other.get_den()))
    
    def __add__(self, other):
        '''F.__add__(other) or F + other --> Fraction
        Return the sum of the two fractions as a fraction and if necessary
        the result will be reduced to its simpliest form.'''        
        if self.get_den() == other.get_den():
            return Fraction.reduce_frac(Fraction(self.get_num() + other.get_num(), self.get_den())) 
        
        else:   
            return Fraction.reduce_frac(Fraction(self.get_num() * other.get_den() + other.get_num() * self.get_den(), self.get_den() * other.get_den()))
    
    def __div__(self, other):
        '''F.__div__(other) or F / other --> Fraction
        Return the divsion of the two fractions as a fraction and if necessary
        the result will be reduced to its simpliest form.'''        
        return Fraction.reduce_frac(Fraction(self.get_num() * other.get_den(), other.get_num() * self.get_den()))
    
    def __sub__(self, other):
        '''F.__sub__(other) or F - other --> Fraction
        Return the difference of the two fractions as a fraction and if necessary
        the result will be reduced to its simpliest form.'''        
        if self.get_den() == other.get_den():
            return Fraction.reduce_frac(Fraction(self.get_num() - other.get_num(), self.get_den()))    
        
        else:   
            return Fraction.reduce_frac(Fraction(self.get_num() * other.get_den()- other.get_num() * self.get_den(), self.get_den() * other.get_den()))
    
    def __eq__(self, other):
        '''F.__eq__(other) or F == other --> Boolean
        Returns whether or not the two fractions are equal. Compared by decimal
        value.'''
        return self.decimal_value() == other.decimal_value()
    
    def __lt__(self, other):
        '''F.__lt__(other) or F < other --> Boolean
        Returns whether or not the first fraction are less than the second
        fraction. Compared by decimal value.'''
        return self.decimal_value() < other.decimal_value()
    
    def __gt__(self, other):
        '''F.__gt__(other) or F > other --> Boolean
        Returns whether or not the first fraction are greater than the second
        fraction. Compared by decimal value.'''
        return self.decimal_value() > other.decimal_value()
    
    def __ge__(self, other):
        '''F.__ge__(other) or F >= other --> Boolean
        Returns whether or not the first fraction are greater than or equal to
        the second fraction. Compared by decimal value.'''
        return self.decimal_value() >= other.decimal_value()
    
    def __le__(self, other):
        '''F.__le__(other) or F <= other --> Boolean
        Returns whether or not the first fraction are less than or equal to the
        second fraction. Compared by decimal value.'''
        return self.decimal_value() <= other.decimal_value()
    
    def __str__(self):
        '''F.__str__() or str(F) --> str
        Return a str in the form "numerator/denominator".'''        
        return "%i/%i" %(self.get_num(), self.get_den())
 
def main():
    frac = Fraction(5,-2)
    frac2 = Fraction(3,-2)    
    print frac + frac2
    print frac - frac2
    print frac * frac2
    print frac / frac2
    print frac.mixed_form()
    print frac2.mixed_form()
    print frac.decimal_value()
    print frac2.decimal_value()
    print frac.square()
    print frac2.square()
    print frac > frac2
    print frac < frac2
    print frac == frac2
    print frac >= frac2
    print frac <= frac2
    print frac.int_power(3)
    print frac2.int_power(3)
    print frac.frac_power(frac2)
    print frac2.frac_power(frac)
    print frac.rounding()
    print frac2.rounding()
    print frac.abs_rounding()
    print frac2.abs_rounding()
                                  
if __name__ == "__main__":
    main()