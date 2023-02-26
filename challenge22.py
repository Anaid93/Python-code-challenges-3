'''Define a list with a set of names, print the number 
of names beginning with the letter a'''

def names(names:list):
    names_total = 0
    for name in names:       
        #for letra in nombre: no es necesario colocar esto
        if name[0] == 'a':
            names_total += 1
    return names_total             

print(names(['ana', 'alejandra', 'beto', 'carina', 'alexa', 'amelia']))

