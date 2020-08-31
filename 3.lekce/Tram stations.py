tram_stations = {
'No.1' : ['Reckovice', 'Semilasso', 'Husitska', 'Jungmannova', 'Kartouzska', 'Sumavska', 'Hrncirska', 'Pionyrska', 'Antoninska', 'Moravske nam.', 'Malinovske nam.', 'Hlavni nadr.', 'Nove sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Vystaviste main', 'Vystaviste G2', 'Lipova', 'Pisarky'],
'No.2' : ['Zidenice', 'Kuldova', 'Vojenska nemocnice', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove Sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Porici', 'Nemocnice UM', 'Celni', 'Hluboka', 'Ustredni hrbitov'],
'No.3' : ['Husovice','Nam. republiky','Vozovna Husovice','Mostecka','Travnickova', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove sady', 'Silingrovo nam.', 'Ceska', 'Komenskeho nam.', 'Obilni trh', 'Uvoz']
}

prvni_linka = set(tram_stations.get('No.1'))
druha_linka = set(tram_stations.get('No.2'))
treti_linka = set(tram_stations.get('No.3'))

prunik = prvni_linka & druha_linka & treti_linka

print(prunik)