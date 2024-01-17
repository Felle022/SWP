class Player:
    def __init__(self, name):
        self.name= name

    def option(self):
        try:
            incorrectinsert=True
            while incorrectinsert:
                option=int(input("Choose Option:"))
                if option in range(0,5):
                    return option
                else:
                    print("Eingabe ungültig")
        except ValueError:
            print(ValueError)

