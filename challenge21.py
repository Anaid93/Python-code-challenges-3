'''Define a tuple with 10 ages of people.
Print the number of people with ages greater than 20.'''

# the * allows the function to accept multiple parameters 
def tupla(*ages:tuple):
    count = 0
    for age in ages:
        if age > 20:
            count += 1
    return f'Number of people over 20 years of age: {count}'

print(tupla(22,18,15,25,30))