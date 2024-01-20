from Spieler import Player
from Computer import Computer

import json

def game():
    options = {1: 'Rock', 2: 'Paper', 3: 'Scissors', 4: 'Spock', 5: 'Lizard'}
    game=True
    data_dic = get_data()
    p=Player(input("Name:"))
    if input("Statistik(S)/Play(P)")=="S":
        print(data_dic)
    c=Computer()
    while game:
        option= p.option()
        option2=c.option()
        winner=check_inputs(option,option2)
        if winner==1:
            print(f"{p.name} hat gewonnen mit {options[option]}")
            print(f"Computer {options[option2]}")
            data_dic["Player"]=data_dic["Player"]+1
            data_dic[options[option]]=data_dic[options[option]]+1
            export_data(data_dic)
        elif winner==2:
            print(f"{c.name} hat gewonnen mit {options[option2]}")
            print(f"{p.name}: {options[option]}")
            data_dic["Computer"] = data_dic["Computer"] + 1
            data_dic[options[option]] = data_dic[options[option]] + 1
            export_data(data_dic)
        elif winner==0:
            print("Draw")
            data_dic["Draw"] = data_dic["Draw"] + 1
            data_dic[options[option]] = data_dic[options[option]] + 1
            export_data(data_dic)
        con=input("Continue:Y/N")
        if con == "N" or c=="n":
            game= False
        elif c == "Y" or c== "y":
            game= True


def check_inputs(option1,option2):
    regeln = {
        1: [4, 3],  # Schere schlägt "Echse", "Papier"
        2: [4, 1],  # Stein schlägt "Echse", "Schere"
        3: [2, 5],  # Papier schlägt "Stein", "Spock"
        4: [3, 5],  # Echse schlägt "Papier", "Spock"
        5: [2, 1]  # Spock schlägt "Stein", "Schere"
    }

    if option1 == option2:
       return 0
    elif option1 not in regeln[option2]:
        return 2
    else:
        return 1
    return 99

    '''
    if option1 == option2:
        return 0
    elif ((option2 - option1) % 5) % 2 == 0:
        return 1
    return 2
    '''


def export_data(data):
    with open('Data.json', 'w') as datei:
        json.dump(data, datei, indent=2, ensure_ascii=False)

def get_data():
    with open('Data.json', 'r') as datei:
        daten = json.load(datei)
        return daten

def main():
    game()

if __name__ =="__main__":
    main()