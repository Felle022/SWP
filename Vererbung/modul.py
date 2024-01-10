class Firma:
    def __init__(self, name, abteilungen):
        self.name = name
        self.abteilungen = abteilungen

    def anzahl_mitarbeiter(self):
        anzahl=0
        for a in self.abteilungen:
            if(isinstance(a,Abteilung)):
                anzahl=anzahl+a.anzahl_mitarbeiter_abteilung()
        return anzahl

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        current_groesste_abteilung = {'name': "", 'mitarbeiter': 0}
        for abteilung in self.abteilungen:
            name = abteilung.get_name()
            anzahl = abteilung.anzahl_mitarbeiter_abteilung()
            if anzahl > current_groesste_abteilung['mitarbeiter']:
                current_groesste_abteilung['name'] = name
                current_groesste_abteilung['mitarbeiter'] = anzahl
        return current_groesste_abteilung

    def frauenquote(self):
        anzahl_mitarbeiter = self.anzahl_mitarbeiter()
        return sum([a.anzahl_frauen() for a in self.abteilungen]) / anzahl_mitarbeiter


class Abteilung:
    def __init__(self, name, mitarbeiter, leiter):
        self.name = name
        self.mitarbeiter = mitarbeiter
        self.leiter = leiter

    def get_name(self):
        return self.name

    def anzahl_mitarbeiter_abteilung(self):
        return len(self.mitarbeiter) + 1

    def anzahl_frauen(self):
        return (sum([m.is_weiblich() for m in self.mitarbeiter]) + self.leiter.is_weiblich()) * 100


class Person:
    def __init__(self, vorname, nachname, weiblich):
        self.vorname = vorname
        self.nachname = nachname
        self.weiblich = weiblich

    def is_weiblich(self):
        return self.weiblich


class Mitarbeiter(Person):
    def __init__(self, vorname, nachname, beruf, weiblich):
        self.beruf = beruf
        super().__init__(vorname, nachname, weiblich)

    def get_beruf(self):
        return self.beruf


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, vorname, nachname, beruf, weiblich):
        super().__init__(vorname, nachname, beruf, weiblich)

