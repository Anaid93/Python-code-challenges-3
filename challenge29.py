'''write a program that shows a list of movies and 
asks the user to enter the code of a movie and 
the number of days overdue. At the end it 
should show the total amount to be paid. '''

import pandas

data = {
    'Movies': ['Pelicula1', 'Pelicula2', 'Pelicula3', 'Pelicula4'], 
    'Price': [2.50, 3.00, 3.50, 4.00], 
    'Code': [1, 2, 3, 4], 
    'Overdue/Days': [0.50, 0.75, 1.00, 1.50]
}

table = pandas.DataFrame(data)
print(table)

while True:
    
    code = int(input('Enter the code of the movie (if you want to exit press 0): ')) 
    if code != 0:
        overdue = table.loc[code-1,'Overdue/Days']
        price= table.loc[code-1,'Price']
        number_days_overdue = 7       
        total_amount = overdue*number_days_overdue+price
        print(f'The total amount is: ${total_amount}')
    else:
        break
