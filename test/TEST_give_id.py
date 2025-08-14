import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fonctions import *

from fonctions import *

def main():
    print("Start ok")

    print("Reset id")
    reset_id()
    print("Reset id ok")

    print("Give id")
    a=give_id()
    b=give_id()
    c=give_id()

    print(f"Next id : {a}\n")
    print(f"Next id : {b}\n")
    print(f"Next id : {c}\n")

    print("Reset id")
    reset_id()
    print("Reset id ok")

    print("Give id")
    a=give_id()
    b=give_id()
    c=give_id()
    d=give_id()
    e=give_id()
    f=give_id()
    g=give_id()
    h=give_id()
    i=give_id()

    print(f"Next id : {a}\n")
    print(f"Next id : {b}\n")
    print(f"Next id : {c}\n")
    print(f"Next id : {d}\n")
    print(f"Next id : {e}\n")
    print(f"Next id : {f}\n")
    print(f"Next id : {g}\n")
    print(f"Next id : {h}\n")
    print(f"Next id : {i}\n")

    print("Give id ok")

if __name__ == "__main__":
    main()
