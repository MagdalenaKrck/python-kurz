znamky_4a = {
    "Petr Novák": 1,
    "Alena Novotná": 3,
    "Pavel Panáček": 2,
    "Adam Konečný": 2,
}

znamky_4b = {
    "Aneta Petrovská": 4,
    "Petr Štastný": 2,
    "Hanka Hrnčířská": 2,
}

# Vytvoření nového slovníku pro sjednocené známky
známky = {}

# Sjednocení slovníků
známky.update(znamky_4a)
známky.update(znamky_4b)

print(známky)
