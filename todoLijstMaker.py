""""
To-do lijst maker console app
Chloe Waldron

Bronnen: 
StackOverflow, 
Chatgpt(om te vragen hoe ik bepaalde dingen juist kan implementeren in mijn project, daarbij heb ik m.b.v de uitleg van chatgpt het zelf toegepast in mijn project.)
Google
Youtube

^ ik durf wel niet te zeggen bij welke delen in mijn code ik deze bronnen heb gebruikt dus ik vermeld het gewoon zo.
"""



import json
import os
import datetime

class Taak:

    """ een taak in de lijst """
    def __init__(self, titel, beschrijving="", deadline=None, categorie="Algemeen"):
        self.titel = titel
        self.beschrijving = beschrijving
        self.deadline = deadline
        self.categorie = categorie
        self.gedaan = False

    def __str__(self):
        """ Format voor de taken als ze worden weergegeven"""
        status = "✓" if self.gedaan else "✗"
        return f"[{status}] ({self.titel}) - {self.beschrijving} | Deadline:{self.deadline}"
    
    
class ToDoLijst:

    def __init__(self, bestand="todo.json"):
        self.bestand = bestand
        self.taken = self.laden()

    def laden(self):
        """ zorgt ervoor dat alles laad van het json bestand"""
        if os.path.exists(self.bestand):
            with open(self.bestand, "r", encoding="utf-8") as f:
                data = json.load(f)
                taken = []
                for taak_data in data:
                    taak = Taak(
                        titel=taak_data["titel"],
                        beschrijving=taak_data["beschrijving"],
                        deadline=taak_data["deadline"],
                        categorie=taak_data["categorie"]
                    )
                    taak.gedaan = taak_data["gedaan"]
                    taken.append(taak)
                return taken
        return[]
    
    def opslaan(self):
        """ Slaat alle taken op in een json bestand """
        data = []
        for taak in self.taken:
            data.append({
                "titel": taak.titel,
                "beschrijving": taak.beschrijving,
                "deadline": taak.deadline,
                "categorie": taak.categorie,
                "gedaan": taak.gedaan
            })
        with open(self.bestand, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def taak_toevoegen(self, titel, beschrijving="", deadline=None, categorie="Algemeen"):
        """ nieuwe taak toevoegen"""
        nieuwe_taak = Taak(titel, beschrijving, deadline, categorie)
        self.taken.append(nieuwe_taak)
        self.opslaan()
        print(f"✓ Taak '{titel}' toegevoegd")

    def taken_tonen(self, categorie=None, alleen_open=False):
        """ Laat de taken zien"""
        print("\n~~~ TakenLijst ~~~")
        for i, taak in enumerate(self.taken):
            if categorie and taak.categorie != categorie:
                continue
            print(f"{i+1}. {taak}")
        print("~~~~~~~~~~~~\n")

    def taak_verwijderen(self, index):
        """ verwijderd de taken"""
        try:
            verwijderd = self.taken.pop(index)
            self.opslaan()
            print(f"Taak '{verwijderd.titel}' verwijderd")
        except IndexError:
            print("Ongeldig taaknummer.")

def hoofdmenu():
    print("\n=== TO-DO LIJST MAKER ===")
    print("1. Taak toevoegen")
    print("2. Taken tonen")
    print("3. Taak markeren als gedaan")
    print("4. Taak verwijderen")
    print("5. Filter op categorie")
    print("6. Filter open taken")
    print("7. Afsluiten")
    keuze = input("Kies een optie: ")
    return keuze

def main():
    todo = ToDoLijst()
    while True:
        keuze = hoofdmenu()
        if keuze == "1":
           titel = input("Titel: ")
           beschrijving = input("Beschrijving: ")
           deadline = input("Deadline (optioneel): ")
           categorie = input("Categorie (optioneel): ")
           todo.taak_toevoegen(titel, beschrijving, deadline or None, categorie or "Algemeen")
        elif keuze == "2":
            todo.taken_tonen()
        elif keuze == "3":
            todo.taken_tonen()
            try:
                num = int(input("Taaknummer om als gedaan te markeren: ")) - 1
                todo.taak_markeren(num, gedaan=True)
            except ValueError:
                print("Voer een geldig nummer in.")
        elif keuze == "4":
            todo.taken_tonen()
            try:
                num = int(input("Taaknummer om te verwijderen: ")) - 1
                todo.taak_verwijderen(num)
            except ValueError:
                print("Voer een geldig nummer in.")
        elif keuze == "5":
            cat = input("Categorie: ")
            todo.taken_tonen(categorie=cat)
        elif keuze == "6":
            todo.taken_tonen(alleen_open=True)
        elif keuze == "7":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

if __name__ == "__main__":
    main()
