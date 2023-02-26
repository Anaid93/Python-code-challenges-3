'''writes two functions that receive one parameter (width). 
The first function draws the first half of the triangle 
and the other draws the second half.'''

def triangle_1(width):
    for i in range(1, width + 1):
        for j in range(i):
            print("* ", end="")
        print()

triangle_1(4)
# use end= to place a space instead of a new line in the output.


def triangle_2(width):
    for i in range(1, width):
        for j in range(width - i):
            print("* ", end="")
        print()

triangle_2(4)
