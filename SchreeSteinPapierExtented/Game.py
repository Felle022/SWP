from Spieler import Player
from Computer import Computer

def game():
    options = {0: 'Rock', 1: 'Paper', 2: 'Scissors', 3: 'Spock', 4: 'Lizard'}
    game=True
    p=Player(input("Name:"))
    c=Computer()
    while game:
        option=0
        option2=0
        option= p.option()
        option2=c.option()
        winner=check_inputs(option,option2)
        if winner==1:
            print(f"{p.name} hat gewonnen mit {options[option]}")
            print(f"Compter {options[option2]}")
        elif winner==2:
            print(f"{c.name} hat gewonnen mit {options[option2]}")
            print(f"{p.name}: {options[option]}")
        else:
            print("Draw")
        con=input("Continue:Y/N")
        if con == "N" or c=="n":
            game= False
        elif c == "Y" or c== "y":
            game= True


def check_inputs(option1,option2):
    if option1 == option2:
        return 0
    elif ((option2 - option1) % 5) % 2 == 0:
        return 1
    return 2


def main():
    game()

if __name__ =="__main__":
    main()