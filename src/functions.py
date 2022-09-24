from xml.dom import InvalidCharacterErr

yes_variants = ("Y", "y", "Yes", "YES", "yes")
no_variants = ("N", "n", "No", "NO", "no")

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