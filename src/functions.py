import pixel_art as pa


descision = input("make your choice 1, 2 or 3: ")

def Wrong_number():
    val = int(input('Enter an integer: '))
    if not val in range(1, 3):
        raise NameError(f'{val} is out of range - must be between 1 and 10')

    return val

#prints a blob image
def make_a_choice():
    if descision == int(1):
        print(pa.Fire_Blob ())
    elif descision == int(2):
        print(pa.Water_Blob ())
    elif descision == int(3):
        print(pa.Grass_Blob ())
    return
make_a_choice()
