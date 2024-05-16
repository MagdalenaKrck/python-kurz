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
zadej_datum = input("Zadej datum ve formátu YYYY-MM-DD:")
datum =  datetime.datetime.strptime(zadej_datum, "%Y-%m-%d").date()
print(je_otevreno(datum))

#     datetime.date.today(): Tato metoda vrátí aktuální datum jako objekt třídy datetime.date. V podstatě získáváte aktuální datum, které lze použít k porovnání s jinými daty.

#     (datum - dnes).days: V tomto kroku se odečítá aktuální datum (dnes) od zadaného data (datum). Výsledkem je časový rozdíl mezi oběma daty, vyjádřený jako objekt třídy datetime.timedelta. Použitím atributu .days získáváte počet dnů v tomto rozdílu. To znamená, že dostanete rozdíl v počtu dnů mezi zadaným datem a aktuálním datem.

#     if rozdil % 2 == 0: return "Ano" else: return "Ne": Tento blok kódu rozhoduje, zda je rozdíl mezi zadaným datem a aktuálním datem sudý či lichý. Operátor % zde provádí operaci modulo, což znamená, že vrátí zbytek po dělení prvního čísla (v tomto případě rozdil) druhým číslem (v tomto případě 2). Pokud je zbytek rovný 0, pak je rozdíl sudý, a tedy funkce vrátí "Ano". Jinak vrátí "Ne".

