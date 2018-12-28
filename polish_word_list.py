#!/usr/bin/env python
# -*- coding: utf-8 -*- 

words = [u"Hollywood",
u"Ekran",
u"Grać",
u"Marmur",
u"Dinozaur",
u"Kot",
u"Smoła",
u"Więź",
u"Grecja",
u"Pokład",
u"Kolec",
u"Środek",
u"Odkurzać",
u"Jednorożec",
u"Właściciel zakładu pogrzebowego",
u"Skarpetka",
u"Loch Ness",
u"Koń",
u"Berlin",
u"Dziobak",
u"Port",
u"skrzynia",
u"Pudełko",
u"Złożony",
u"Statek",
u"Zegarek",
u"Przestrzeń",
u"flet prosty",
u"Wieża",
u"Śmierć",
u"Dobrze",
u"Targi",
u"Ząb",
u"Personel",
u"Rachunek",
u"Strzał",
u"Król",
u"Patelnia",
u"Plac",
u"Bawół",
u"Naukowiec",
u"Pisklę",
u"Atlantyda",
u"Szpieg",
u"Poczta",
u"Orzech",
u"Log",
u"Pirat",
u"Twarz",
u"Kij",
u"Choroba",
u"Dziedziniec",
u"Uchwyt",
u"Ślimak",
u"Kostka do gry",
u"Prowadzić",
u"Hak",
u"Marchewka",
u"Zatruć",
u"Zbiory",
u"Stopa",
u"Pochodnia",
u"Ramię",
u"Postać",
u"Mój",
u"Garnitur",
u"Dźwig",
u"Pekin",
u"Masa",
u"Mikroskop",
u"Silnik",
u"Chiny",
u"Słoma",
u"Spodnie",
u"Europa",
u"Bagażnik",
u"Księżniczka",
u"Połączyć",
u"Szczęście",
u"Oliwa",
u"Palma",
u"Nauczyciel",
u"Kciuk",
u"Ośmiornica",
u"kaptur",
u"Wiązanie",
u"Lekarz",
u"Budzić",
u"Krykiet",
u"Milioner",
u"Nowy Jork",
u"Stan",
u"Bermudy",
u"Park",
u"indyk",
u"Czekolada",
u"Wycieczka",
u"Rakieta",
u"Nietoperz",
u"Strumień",
u"Szekspir",
u"Śruba",
u"Przełącznik",
u"Ściana",
u"Dusza",
u"Duch",
u"Czas",
u"Taniec",
u"Amazonka",
u"wdzięk",
u"Moskwa",
u"Dynia",
u"Antarktyda",
u"Bat",
u"Serce",
u"Stół",
u"Piłka",
u"Wojownik",
u"Zimno",
u"Dzień",
u"Wiosna",
u"Mecz",
u"Diament",
u"Centaur",
u"Marsz",
u"Ruletka",
u"Pies",
u"Krzyż",
u"Fala",
u"kaczka",
u"Wiatr",
u"Miejsce",
u"Wieżowiec",
u"Papier",
u"jabłko",
u"Olej",
u"gotować",
u"latać",
u"Odlew",
u"Niedźwiedź",
u"Kołek",
u"Złodziej",
u"Bagażnik samochodowy",
u"Ameryka",
u"Powieść",
u"Komórka",
u"Łuk",
u"Model",
u"Nóż",
u"Rycerz",
u"Sąd",
u"Żelazo",
u"Wieloryb",
u"Cień",
u"Kontrakt",
u"Rtęć",
u"Konduktor",
u"Foka",
u"Samochód",
u"Pierścień",
u"Dziecko",
u"Fortepian",
u"Laser",
u"Dźwięk",
u"Polak",
u"Superbohater",
u"Rewolucja",
u"Dół",
u"Gaz",
u"Szkło",
u"Waszyngton",
u"Szczekać",
u"Śnieg",
u"kość słoniowa",
u"Rura",
u"Pokrywa",
u"Stopień",
u"Tokio",
u"Kościół",
u"Ciasto",
u"Rura",
u"Blok",
u"Komiczny",
u"Ryba",
u"Most",
u"Księżyc",
u"Część",
u"Aztek",
u"Przemytnik",
u"Pociąg",
u"Ambasada",
u"Uczeń",
u"Nurek",
u"Lód",
u"Kran",
u"Kod",
u"But",
u"serwer",
u"Klub",
u"Rząd",
u"Piramida",
u"Pluskwa",
u"Pingwin",
u"Funt",
u"Himalaje",
u"Czech",
u"Rzym",
u"Oko",
u"Tablica",
u"Łóżko",
u"Punkt",
u"Francja",
u"Mamut",
u"Bawełna",
u"Rudzik",
u"Netto",
u"Dąbrówka",
u"Klon",
u"Anglia",
u"Pole",
u"Robot",
u"Wątek",
u"Afryka",
u"Etykietka",
u"Usta",
u"kiwi",
u"Kret",
u"Szkoła",
u"Tonąć",
u"Pistolet",
u"Opera",
u"Mennica",
u"Korzeń",
u"Pod",
u"Korona",
u"Z powrotem",
u"Samolot",
u"Meksyk",
u"Płaszcz",
u"okrąg",
u"Tablet",
u"Australia",
u"Zielony",
u"Egipt",
u"Linia",
u"Prawnik",
u"Czarownica",
u"Spadochron",
u"Wypadek",
u"Złoto",
u"Uwaga",
u"Lew",
u"Plastikowy",
u"Sieć",
u"Karetka pogotowia",
u"Szpital",
u"Zaklęcie",
u"Zamek",
u"woda",
u"Londyn",
u"Kasyno",
u"Cykl",
u"Bar",
u"Klif",
u"Okrągły",
u"Bomba",
u"Ogromny",
u"Dłoń",
u"Ninja",
u"Róża",
u"Poślizg",
u"Limuzyna",
u"Przechodzić",
u"Teatr",
u"Talerz",
u"Satelita",
u"Keczup",
u"Hotel",
u"Ogon",
u"Kleszcz",
u"Ziemia",
u"Policja",
u"Krasnolud",
u"Wentylator",
u"Sukienka",
u"Saturn",
u"Trawa",
u"Szczotka",
u"Krzesło",
u"Skała",
u"Pilot",
u"Teleskop",
u"Plik",
u"Laboratorium",
u"Indie",
u"Linijka",
u"Gwóźdź",
u"Huśtawka",
u"Olympus",
u"Zmiana",
u"Data",
u"Strumień",
u"Pocisk",
u"Skala",
u"Zespół muzyczny",
u"Anioł",
u"naciśnij",
u"Jagoda",
u"Karta",
u"Czek",
u"Wersja robocza",
u"Głowa",
u"Podołek",
u"Pomarańczowy",
u"Lody",
u"Film",
u"Pralka",
u"Basen",
u"Rekin",
u"Awangarda",
u"Strunowy",
u"Cielę",
u"Jastrząb",
u"Orzeł",
u"Igła",
u"Las",
u"smok",
u"Klawisz",
u"Pas",
u"Czapka z daszkiem",
u"Wiercić",
u"Rękawica",
u"Pasta",
u"Spadek",
u"Ogień",
u"Pająk",
u"Kręgosłup",
u"Żołnierz",
u"Róg",
u"królowa",
u"szynka",
u"Śmieci",
u"Życie",
u"Świątynia",
u"Królik",
u"Przycisk",
u"Gra",
u"Gwiazda",
u"Jowisz",
u"Weterynarz",
u"Noc",
u"Powietrze",
u"Bateria",
u"Geniusz",
u"Sklep",
u"Butelka",
u"stadion",
u"Obcy",
u"Światło",
u"Trójkąt",
u"Cytrynowy",
u"Pielęgniarka",
u"Upuszczać",
u"Tor",
u"Bank",
u"Niemcy",
u"Robak",
u"Promień",
u"Kapitał",
u"Strajk",
u"Wojna",
u"Koncert",
u"kochanie",
u"Kanada",
u"Bryknięcie",
u"Bałwan",
u"Bić",
u"Dżem",
u"Miedź",
u"Plaża",
u"dzwon",
u"Krasnoludek",
u"Pheonix",
u"Siła",
u"Bum",
u"Widelec",
u"Alpy",
u"Słupek",
u"Płot",
u"Kangur",
u"Mysz",
u"Kubek",
u"Podkowa",
u"Skorpion",
u"Agent",
u"Śmigłowiec",
u"Otwór",
u"Organ",
u"Jacek",
u"Opłata"]
