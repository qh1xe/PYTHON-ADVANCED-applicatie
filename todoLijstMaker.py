""""
To-do lijst maker console app
Chloe Waldron

Bronnen: 
StackOverflow, 
Chatgpt(om te vragen hoe ik bepaalde dingen juist kan implementeren in mijn project, daarbij heb ik m.b.v de uitleg van chatgpt het zelf toegepast in mijn project.)
Google

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
        return f"[{status}] ({self.titel}) - {self.beschrijving} | Deadline:{self.deadline or 'Green'}"
    
    
class ToDoLijst:

    def __init__(self, bestand="todo.json"):
        self.bestand = bestand
        self.taken = self.laden()

    def laden(self):
        """ laad de taken van de json bestand"""
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