from modul import Firma, Abteilung, Mitarbeiter, Abteilungsleiter

mitarbeiter_backboard = [
    Mitarbeiter("Hermann", "Schlagele", "Hausmeister", False),
    Mitarbeiter("Hermime", "Schlagele", "Techniker", True),
    Mitarbeiter("Sohnemann", "Schlagele", "Matrose", False),
]

kaptiaen = Abteilungsleiter("Rudel", "Frisch", "Bierkapitän", False)

backboard = Abteilung("Backboard", mitarbeiter_backboard, kaptiaen)

mitarbeiter_hafen = [
    Mitarbeiter("Bube", "Blaubarsch", "Reinigungskraft/Superheld", False)
]
hafen_chef = Abteilungsleiter("Mann", "Meerjungfrau", "Superheld", True)
hafen = Abteilung("Hafen", mitarbeiter_hafen, hafen_chef)

firma = Firma("Schiffskartel", [backboard, hafen])


def firmen_ausgabe(firma):
    print(firma.name)
    print(f"  Anzahl Mitarbeiter: {firma.anzahl_mitarbeiter()}")
    print(f"  Anzahl Abteilungen: {firma.anzahl_abteilungen()}")
    groesste_abteilung = firma.groesste_abteilung()
    print(f"  Größte Abteilung: {groesste_abteilung['name']} mit {groesste_abteilung['mitarbeiter']} Mitarbietern")
    print(f"  Frauenquote: {firma.frauenquote()}")


firmen_ausgabe(firma)
