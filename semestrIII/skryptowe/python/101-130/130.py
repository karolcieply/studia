def samogloski(tekst):
    samogloski = "aeiouyAEIOUY"
    ile = 0
    for znak in tekst:
        if znak in samogloski:
            ile += 1
    return ile


print(samogloski("Ala ma kota"))
