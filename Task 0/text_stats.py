# Author: Jeton Sinoimeri
# Text_stats.py
# Date: Sept 26, 2010

words = []
in_file = open("sample.txt")

for lines in in_file:
    words += [lines.split("\n")]
in_file.close()

ind_word = []
counter = 0

for i in range(len(words)):
    counter += len(words[i][0])
    ind_word += words[i][0].split()
output = "Total number of all characters is %i\n" %(counter)

str_word = ' '.join(ind_word).lower().replace('.', '').replace(',', '')
ind_word = str_word.split()

counter2 = 0
letter_1 = []
letter_2 = []
letter_3 = []
letter_4 = []
letter_5 = []
letter_6 = []
letter_7 = []
more_than_7 = []

for word in ind_word:
    w_count = ind_word.count(word)            
    if w_count > counter2:
        counter2 = w_count
        frequent_word = word
 
    if len(word) == 1:
        letter_1 += [word]
        if letter_1.count(word) > 1:
            letter_1.remove(word)
    
    elif len(word) == 2:
        letter_2 += [word]
        if letter_2.count(word) > 1:
            letter_2.remove(word)
    
    elif len(word) == 3:
        letter_3 += [word]
        if letter_3.count(word) > 1:
            letter_3.remove(word)
    
    elif len(word) == 4:
        letter_4 += [word]
        if letter_4.count(word) > 1:
            letter_4.remove(word)
    
    elif len(word) == 5:
        letter_5 += [word]
        if letter_5.count(word) > 1:
            letter_5.remove(word)
    
    elif len(word) == 6:
        letter_6 += [word]
        if letter_6.count(word) > 1:
            letter_6.remove(word)
    
    elif len(word) == 7:
        letter_7 += [word]
        if letter_7.count(word) > 1:
            letter_7.remove(word)
            
    else:
        more_than_7 += [word]
        if more_than_7.count(word) > 1:
            more_than_7.remove(word)

output += "1-letter words are: %s\n2-letter words are: %s\n3-letter words are: %s\n" %(', '.join(letter_1), ', '.join(letter_2), ', '.join(letter_3))
output += "4-letter words are: %s\n5-letter words are: %s\n6-letter words are: %s\n7-letter words are %s\n" %(', '.join(letter_4), ', '.join(letter_5), ', '.join(letter_6), ', '.join(letter_7))

if len(more_than_7) > 0:
    output += "rest of the words are: %s\n" %(', '.join(more_than_7))

output += "The most frequent word is '%s'\n\nBar-Graph of Letter Frequency:\n" %(frequent_word)

str_word = ''.join(ind_word)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for alpha in alphabet:
    counter = str_word.count(alpha)
    bars = '='*counter        
    
    if len(bars) > 15:
        bars = '='*15 + ' (%i)' %(counter-15)
    
    if counter > 0:
        output += "%s %s\n" %(alpha.upper(), bars)

print output