tram_stations = {
'No.1' : ['Reckovice', 'Semilasso', 'Husitska', 'Jungmannova', 'Kartouzska', 'Sumavska', 'Hrncirska', 'Pionyrska', 'Antoninska', 'Moravske nam.', 'Malinovske nam.', 'Hlavni nadr.', 'Nove sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Vystaviste main', 'Vystaviste G2', 'Lipova', 'Pisarky'],
'No.2' : ['Zidenice', 'Kuldova', 'Vojenska nemocnice', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove Sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Porici', 'Nemocnice UM', 'Celni', 'Hluboka', 'Ustredni hrbitov'],
'No.3' : ['Husovice','Nam. republiky','Vozovna Husovice','Mostecka','Travnickova', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove sady', 'Silingrovo nam.', 'Ceska', 'Komenskeho nam.', 'Obilni trh', 'Uvoz']
}
# Our goal is to identify which stations are included in each list.
# Stanice, které leží v každém listu
# aneb jak dodat "grammarnazi slovnik" - interpunkce a překlepy

# & intersection
# udělat z linek sety -> linka = název setu, z hodnot slovníků set, klíč jako název fce setu
# rozpracováno

set

namka = set(tram_stations)
print(namka)
