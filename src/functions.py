from xml.dom import InvalidCharacterErr

#input variants
yes_variants = ("Y", "y", "Yes", "YES", "yes")
no_variants = ("N", "n", "No", "NO", "no")

#letting the user set the pace
def next(prompt):
    answer = ""
    while True:
        answer = input(f"{prompt}\n'yes' or 'no': ")
        print("")
        if answer in (yes_variants):
            return True
        elif answer not in (no_variants):
            InvalidCharacterErr
            print("InvalidCharacterErr- Please enter either: 'yes', 'no', 'y', 'n'")