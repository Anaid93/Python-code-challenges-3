'''Write a program that asks for the width and lenght 
of a rectangle and draws it with product characters (*).'''

def rectangle(width:int, lenght:int):
    for i in range(lenght):
        for j in range(width):
            print("* ", end='')
        print()
        
rectangle(5,3)