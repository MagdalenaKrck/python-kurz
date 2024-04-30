import datetime

def je_otevreno(datum):
    dnes = datetime.date.today()
    rozdil = (datum - dnes).days

# pokud je rozdíl sudý, získáváme ano, jinak ne
    if rozdil % 2 == 0:
        return "Ano"

    else:
        return "Ne"

#test
datum1 =  datetime.date(2024, 4, 28)
print(je_otevreno(datum1))

#     datetime.date.today(): Tato metoda vrátí aktuální datum jako objekt třídy datetime.date. V podstatě získáváte aktuální datum, které lze použít k porovnání s jinými daty.

#     (datum - dnes).days: V tomto kroku se odečítá aktuální datum (dnes) od zadaného data (datum). Výsledkem je časový rozdíl mezi oběma daty, vyjádřený jako objekt třídy datetime.timedelta. Použitím atributu .days získáváte počet dnů v tomto rozdílu. To znamená, že dostanete rozdíl v počtu dnů mezi zadaným datem a aktuálním datem.

#     if rozdil % 2 == 0: return "Ano" else: return "Ne": Tento blok kódu rozhoduje, zda je rozdíl mezi zadaným datem a aktuálním datem sudý či lichý. Operátor % zde provádí operaci modulo, což znamená, že vrátí zbytek po dělení prvního čísla (v tomto případě rozdil) druhým číslem (v tomto případě 2). Pokud je zbytek rovný 0, pak je rozdíl sudý, a tedy funkce vrátí "Ano". Jinak vrátí "Ne".

#     datum1 = datetime.date(2024, 4, 27): Tímto krokem vytváříte nový objekt třídy datetime.date, který představuje zadané datum (27. dubna 2024).

#     print(je_otevreno(datum1)): Nakonec voláte funkci je_otevreno() s datum1 jako argumentem a vypisujete výsledek na obrazovku.

# Takže celý postup získá aktuální datum, spočítej rozdíl mezi zadaným datem a aktuálním datem v počtu dnů a poté rozhodni, zda je tento rozdíl sudý či lichý, a podle toho vrátí "Ano" nebo "Ne".