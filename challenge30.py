'''Write a program that asks for two words and tells 
if they rhyme or not. If the last three letters match, 
it has to say that they rhyme. If only the last two 
letters match, it has to say that they rhyme a little 
and if not, that they do not rhyme.'''

word_1 = input('ingresa la primera palabra: ')
word_2 = input('ingresa la segunda palabra: ')

last_three_1 = word_1[-3:]
last_two_1 = word_1[-2:]
last_three_2 = word_2[-3:]
last_two_2 = word_2[-2:]

if last_three_1 == last_three_2:
    print(f'The words rhyme: {last_three_1}')
elif last_two_1 == last_two_2:
    print(f'The words rhyme a little: {last_two_1}')
else:
    print('The words do not rhyme')

