'''Create a function count_vowels(), which receives 
a word and counts how many letters "a" it has, how 
many letters "e" it has and so on until all the 
vowels are complete.'''

def count_vowels(word:str):
    count_a= 0
    count_e= 0
    count_i= 0
    count_o= 0
    count_u= 0
    for vowels in word:
        if vowels == 'a':
            count_a += 1
        elif vowels == 'e':
            count_e += 1
        elif vowels == 'i':
            count_i += 1
        elif vowels == 'o':
            count_o += 1
        elif vowels == 'u':
            count_u += 1
    return f'The word has {count_a} a, {count_e} e, {count_i} i, {count_o} o, {count_u} u'

print(count_vowels('dinosaur'))
