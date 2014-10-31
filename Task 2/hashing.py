def hash_code(string):
    code = 0
    for letter in str(string):
        code = 11*code + ord(letter)    
    return "%i" %(code)