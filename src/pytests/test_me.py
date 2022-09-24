import pytest

def test_true ():
    descision = 1
    if descision == "1":
        print ('hello')
    elif descision == "2":
        print("world")
    elif descision == "3":
        print("byebye")
    else:
        print("\nInvalid Character - Please enter either: '1', '2', '3'")
