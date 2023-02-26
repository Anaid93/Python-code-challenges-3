'''Write a program that calculates the letter of the DNI from the number. 
The letter is obtained by calculating the remainder of the 
division of the ID number by 23. 
Each result corresponds to a letter: 0=T; 1=R; 2=W; 3=A; 4=G; 5=M; 6=Y; 7=F; 
8=P; 9=D; 10=X; 11=B; 12=N; 13=J; 14=Z; 15=S; 16=Q; 17=V; 18=H; 19=L; 20=C; 21=K; 22=E.

Tell me your DNI (without letter): 31415926
Your DNI (with letter) is: 31415926L'''

def dni():
    question = input('Tell me your DNI (without letter): ')
    result = (int(question))%23
    list_dni = {0:'T', 1:'R', 2:'W', 3:'A', 4:'G', 5:'M', 6:'Y', 7:'F', 8:'P', 9:'D', 10:'X', 
    11:'B', 12:'N', 13:'J', 14:'Z', 15:'S', 16:'Q', 17:'V', 18:'H', 19:'L', 20:'C', 21:'K', 22:'E'}
    for kv in list_dni:
        if result == kv:
            print(f'Your DNI (with letter) is: {question} {list_dni[kv]}')

dni()

